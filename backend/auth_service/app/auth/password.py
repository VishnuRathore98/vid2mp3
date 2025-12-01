"""
password.py

Handles password hashing and verification:
- hash_password() for creating secure hashes
- verify_password() for comparing plaintext to stored hash

Contains ONLY crypto utilities.
"""

from passlib.context import CryptContext
from passlib.exc import UnknownHashError


# `deprecated="auto"` tells Passlib to automatically mark older hashing schemes as deprecated
# when multiple schemes are configured. This means:
#   - If a user logs in with a password hashed using an outdated scheme,
#     Passlib will still verify it, but will tell the application that the
#     hash should be upgraded to the current scheme (here: "bcrypt").
#   - This allows safe, seamless migration from old password hashes to newer,
#     stronger ones without breaking user logins.
# Since we only specify one scheme ("bcrypt"), this simply future-proofs the
# configuration so that if more schemes are added later, older ones will be
# treated as deprecated automatically.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using bcrypt.
    """
    hashed_password = pwd_context.hash(password)
    return hashed_password


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify that a plaintext password matches a stored hash.
    """
    try:
        is_password_varified = pwd_context.verify(password, hashed_password)
    except UnknownHashError as e:
        print("Hasing error: ", e)
        is_password_varified = False
    return is_password_varified
