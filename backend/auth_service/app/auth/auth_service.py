"""
auth_service.py

Contains business logic related to user authentication:
- Validating user credentials
- Issuing access tokens after successful login
- Coordinating with repositories and security utilities

This is the use-case layer for authentication.
"""

from app.auth.jwt import create_access_token


def authenticate_user():
    """
    Attempts to authenticate a user.

    Returns:
        user  -> if authentication successful
        None  -> if failed
    """
    user = ""
    return user


def create_user_token():
    """
    Creates the JWT access token for a user.
    """
    access_token = create_access_token()
    return access_token
