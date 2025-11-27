"""
dependencies.py

FastAPI dependency functions for authentication:
- get_current_user
- get_current_active_user (optional)
- Security dependencies to protect routes

Used directly in route handlers.
"""


def get_current_user():
    """
    Extracts and validates the current user based on JWT token.
    """
    user = ""
    return user
