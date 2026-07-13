class OrdersClient:
    def create_order(self, user_id: str, product_id: str, quantity: int) -> dict:
        if quantity <= 0:
            return {"status_code": 400, "json": {"error": "Quantity must be positive"}}

        return {
            "status_code": 201,
            "json": {
                "id": "order-1",
                "user_id": user_id,
                "product_id": product_id,
                "quantity": quantity,
                "status": "created",
            },
        }

    def get_order(self, order_id: str) -> dict:
        if order_id != "order-1":
            return {"status_code": 404, "json": {"error": "Order not found"}}

        return {
            "status_code": 200,
            "json": {"id": "order-1", "status": "created"},
        }

