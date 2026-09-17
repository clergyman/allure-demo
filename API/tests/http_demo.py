import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.error import HTTPError
from urllib.parse import parse_qsl, urlsplit
from urllib.request import ProxyHandler, Request, build_opener
from uuid import uuid4

import allure


# Deterministic service defects for triage; no public API is contacted.
ROUTES = {
    ('GET', '/catalog/categories'): (200, {'categories': ['bags', 'bottles']}),
    ('GET', '/catalog/products/product-1/reviews'): (200, {'rating': 4.7, 'count': 38}),
    ('GET', '/catalog/products/product-1/availability'): (200, {'available': True, 'stock': 12}),
    ('GET', '/catalog/products/product-1/price'): (200, {'amount': 79.99, 'currency': 'USD'}),
    ('GET', '/catalog/recommendations'): (503, {'error': 'Recommendation index unavailable', 'dependency': 'search-index'}),
    ('GET', '/catalog/products/product-1/media'): (200, {'images': None}),
    ('POST', '/identity/password-reset'): (202, {'accepted': True}),
    ('GET', '/identity/profile'): (200, {'id': 'user-1', 'roles': ['buyer']}),
    ('POST', '/identity/logout'): (200, {'revoked': True}),
    ('POST', '/identity/mfa/verify'): (200, {'verified': False, 'reason': 'Expired challenge cache'}),
    ('POST', '/identity/token/refresh'): (502, {'error': 'Signing key provider unavailable', 'dependency': 'key-vault'}),
    ('GET', '/identity/sessions'): (200, {'sessions': [{'id': 'session-1'}]}),
    ('POST', '/orders/quote'): (200, {'subtotal': 49.99, 'shipping': 5.00, 'total': 54.99}),
    ('POST', '/orders/order-1/cancel'): (200, {'status': 'cancelled'}),
    ('GET', '/orders/order-1/tracking'): (200, {'carrier': 'Demo Courier', 'status': 'in_transit'}),
    ('POST', '/orders/order-1/refund'): (200, {'amount': 39.99, 'currency': 'EUR'}),
    ('POST', '/orders/order-1/payment'): (504, {'error': 'Payment authorization timed out', 'dependency': 'payment-gateway'}),
    ('GET', '/orders/order-1/invoice'): (200, {'invoice': {'id': 'invoice-1'}}),
}


class DemoHandler(BaseHTTPRequestHandler):
    def handle_request(self):
        self.rfile.read(int(self.headers.get('Content-Length', '0')))
        status, payload = ROUTES.get((self.command, urlsplit(self.path).path),
                                     (404, {'error': 'Route not found'}))
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('X-Request-ID', self.headers.get('X-Request-ID', 'unknown'))
        self.send_header('X-Service', self.path.split('/')[1])
        self.end_headers()
        self.wfile.write(body)

    do_GET = handle_request
    do_POST = handle_request

    def log_message(self, *_args):
        pass


def start_server():
    server = ThreadingHTTPServer(('127.0.0.1', 0), DemoHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def redact(value):
    sensitive = {'authorization', 'cookie', 'set-cookie', 'password', 'token',
                 'refresh_token', 'access_token', 'otp'}
    if isinstance(value, dict):
        return {key: '[REDACTED]' if key.lower() in sensitive else redact(item)
                for key, item in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value


def captured_body(value):
    text = json.dumps(redact(value), indent=2)
    return {'contentType': 'application/json', 'encoding': 'utf8',
            'value': text, 'size': len(text.encode()), 'truncated': False}


class HttpDemoClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.opener = build_opener(ProxyHandler({}))

    def request(self, method, route, body=None):
        headers = {'Accept': 'application/json', 'X-Request-ID': str(uuid4()),
                   'Authorization': 'Bearer demo-secret'}
        if body is not None:
            headers['Content-Type'] = 'application/json'
        url = self.base_url + route
        request = Request(url, data=json.dumps(body).encode() if body is not None else None,
                          headers=headers, method=method)
        exchange = {'schemaVersion': 1, 'start': int(time.time() * 1000),
                    'request': {'method': method, 'url': url,
                                'headers': [{'name': key, 'value': value}
                                            for key, value in redact(headers).items()],
                                'query': [{'name': key, 'value': value}
                                          for key, value in parse_qsl(urlsplit(url).query)]}}
        if body is not None:
            exchange['request']['body'] = captured_body(body)
        with allure.step(f'{method} {route}'):
            try:
                try:
                    response = self.opener.open(request, timeout=5)
                except HTTPError as error:
                    response = error
                with response:
                    payload = json.loads(response.read())
                    exchange['response'] = {
                        'status': response.code, 'statusText': response.reason,
                        'headers': [{'name': key, 'value': value}
                                    for key, value in redact(dict(response.headers)).items()],
                        'body': captured_body(payload),
                    }
                return {'status_code': response.code, 'json': payload}
            except Exception as error:
                exchange['error'] = {'name': type(error).__name__, 'message': str(error)}
                raise
            finally:
                exchange['stop'] = int(time.time() * 1000)
                allure.attach(json.dumps(exchange, indent=2), name='HTTP exchange',
                              attachment_type='application/vnd.allure.http+json',
                              extension='httpexchange')
                for section in ('request', 'response', 'error'):
                    if section in exchange:
                        allure.attach(json.dumps(exchange[section], indent=2),
                                      name=f'HTTP {section}', attachment_type=allure.attachment_type.JSON)


def metadata(feature, story, component):
    allure.dynamic.epic('Demo Shop')
    allure.dynamic.feature(feature)
    allure.dynamic.story(story)
    allure.dynamic.label('component', component)
    allure.dynamic.label('microservice', feature.lower())
    allure.dynamic.tag('http-exchange')
    allure.dynamic.severity(allure.severity_level.CRITICAL)


def expect_status(response, expected):
    with allure.step(f'Expect HTTP {expected}'):
        assert response['status_code'] == expected, response['json']
