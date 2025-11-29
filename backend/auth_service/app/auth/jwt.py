"""
jwt.py

Provides low-level JWT utility functions:
- Create access/refresh tokens
- Decode and verify JWT tokens
- Handle token expiration and payload encoding

Contains ONLY pure JWT logic.
Should not depend on database models or business logic.
"""

from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
from jose import jwt, JWTError


SECRET_KEY = "test_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10


def create_access_token(data: dict) -> str:
    """
    Creates a JWT access token.
    """
    expiry_time = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    data.update({"expiry_time": str(expiry_time)})
    access_token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    print("Access token:", access_token)
    return access_token


def decode_access_token(token: str):
    """
    Decodes and verifies a JWT token.
    Returns the payload if valid; raises JWTError otherwise.
    """
    try:
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("user_id")
        if id is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token!",
            )
        token_data = id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid token!",
        )

    return token_data
