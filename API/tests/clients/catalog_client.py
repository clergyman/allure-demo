class CatalogClient:
    def get_product(self, product_id: str) -> dict:
        products = {
            "product-1": {"id": "product-1", "name": "Demo Backpack", "stock": 12},
            "product-2": {"id": "product-2", "name": "Demo Bottle", "stock": 0},
        }

        product = products.get(product_id)
        if product is None:
            return {"status_code": 404, "json": {"error": "Product not found"}}

        return {"status_code": 200, "json": product}

    def search(self, query: str) -> dict:
        if query.lower() == "backpack":
            return {
                "status_code": 200,
                "json": {"items": [{"id": "product-1", "name": "Demo Backpack"}]},
            }

        return {"status_code": 200, "json": {"items": []}}

