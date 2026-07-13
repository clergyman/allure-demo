ROLE_PERMISSIONS = {
    "guest": {"catalog:read"},
    "customer": {"catalog:read", "cart:write", "order:create"},
    "admin": {"catalog:read", "cart:write", "order:create", "product:write"},
}


def can(role: str, permission: str) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, set())

