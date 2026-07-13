from api_logging import log_api_call


class OrdersClient:
    def create_order(self, user_id: str, product_id: str, quantity: int) -> dict:
        if quantity <= 0:
            response = {
                "status_code": 400,
                "json": {"error": "Quantity must be positive"},
            }
            log_api_call(
                service="orders",
                operation="create_order",
                method="POST",
                path="/orders",
                status_code=response["status_code"],
                user_id=user_id,
                product_id=product_id,
                quantity=quantity,
            )
            return response

        response = {
            "status_code": 201,
            "json": {
                "id": "order-1",
                "user_id": user_id,
                "product_id": product_id,
                "quantity": quantity,
                "status": "created",
            },
        }
        log_api_call(
            service="orders",
            operation="create_order",
            method="POST",
            path="/orders",
            status_code=response["status_code"],
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
            order_id=response["json"]["id"],
        )
        return response

    def get_order(self, order_id: str) -> dict:
        if order_id != "order-1":
            response = {"status_code": 404, "json": {"error": "Order not found"}}
            log_api_call(
                service="orders",
                operation="get_order",
                method="GET",
                path=f"/orders/{order_id}",
                status_code=response["status_code"],
                order_id=order_id,
            )
            return response

        response = {
            "status_code": 200,
            "json": {"id": "order-1", "status": "created"},
        }
        log_api_call(
            service="orders",
            operation="get_order",
            method="GET",
            path=f"/orders/{order_id}",
            status_code=response["status_code"],
            order_id=order_id,
        )
        return response
