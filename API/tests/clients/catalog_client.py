from api_logging import log_api_call


class CatalogClient:
    def get_product(self, product_id: str) -> dict:
        products = {
            "product-1": {"id": "product-1", "name": "Demo Backpack", "stock": 12},
            "product-2": {"id": "product-2", "name": "Demo Bottle", "stock": 0},
        }

        product = products.get(product_id)
        if product is None:
            response = {"status_code": 404, "json": {"error": "Product not found"}}
            log_api_call(
                service="catalog",
                operation="get_product",
                method="GET",
                path=f"/products/{product_id}",
                status_code=response["status_code"],
                product_id=product_id,
            )
            return response

        response = {"status_code": 200, "json": product}
        log_api_call(
            service="catalog",
            operation="get_product",
            method="GET",
            path=f"/products/{product_id}",
            status_code=response["status_code"],
            product_id=product_id,
        )
        return response

    def search(self, query: str) -> dict:
        if query.lower() == "backpack":
            response = {
                "status_code": 200,
                "json": {"items": [{"id": "product-1", "name": "Demo Backpack"}]},
            }
            log_api_call(
                service="catalog",
                operation="search",
                method="GET",
                path="/products/search",
                status_code=response["status_code"],
                query=query,
                result_count=len(response["json"]["items"]),
            )
            return response

        response = {"status_code": 200, "json": {"items": []}}
        log_api_call(
            service="catalog",
            operation="search",
            method="GET",
            path="/products/search",
            status_code=response["status_code"],
            query=query,
            result_count=len(response["json"]["items"]),
        )
        return response
