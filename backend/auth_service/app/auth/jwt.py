"""
jwt.py

Provides low-level JWT utility functions:
- Create access/refresh tokens
- Decode and verify JWT tokens
- Handle token expiration and payload encoding

Contains ONLY pure JWT logic.
Should not depend on database models or business logic.
"""

SECRET_KEY = "test_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10


def create_access_token(data: dict) -> str:
    """
    Creates a JWT access token.
    """
    access_token = ""
    return access_token


def decode_token() -> dict:
    """
    Decodes and verifies a JWT token.
    Returns the payload if valid; raises JWTError otherwise.
    """
    decoded_token_data = {}
    return decoded_token_data
