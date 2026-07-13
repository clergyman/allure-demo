class IdentityClient:
    def login(self, email: str, password: str) -> dict:
        if email == "buyer@example.com" and password == "correct-password":
            return {
                "status_code": 200,
                "json": {
                    "token": "demo-token",
                    "user": {"id": "user-1", "email": email},
                },
            }

        return {
            "status_code": 401,
            "json": {"error": "Invalid credentials"},
        }

