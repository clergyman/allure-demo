from api_logging import log_api_call


class IdentityClient:
    def login(self, email: str, password: str) -> dict:
        if email == "buyer@example.com" and password == "correct-password":
            response = {
                "status_code": 200,
                "json": {
                    "token": "demo-token",
                    "user": {"id": "user-1", "email": email},
                },
            }
            log_api_call(
                service="identity",
                operation="login",
                method="POST",
                path="/auth/login",
                status_code=response["status_code"],
                email=email,
            )
            return response

        response = {
            "status_code": 401,
            "json": {"error": "Invalid credentials"},
        }
        log_api_call(
            service="identity",
            operation="login",
            method="POST",
            path="/auth/login",
            status_code=response["status_code"],
            email=email,
        )
        return response
