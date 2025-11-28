"""
user_repository.py

Database operations related to the User model.
Contains pure CRUD + query functions.
Does not include business logic.
"""

from sqlalchemy.orm import Session
from app.models.user_models import User
from app.auth.password import hash_password


async def get_user_by_id(user_id: int, db: Session):
    """Fetch a user by ID."""
    user = db.query(User).filter(User.id == user_id).first()
    return user


async def get_user_by_email(email: str, db: Session):
    """Fetch a user by email."""
    user = (
        db.query(User).filter(User.email == email).first()
    )  # sql model needs to be first as sqlalchemy overloads == operator and it expects sql model to be first
    return user


async def create_user(user_data, db: Session):
    """Insert a new user into the database."""
    print("simple_password: ", user_data)
    hashed_password = hash_password(user_data.password)
    user_data.password = hashed_password
    print("hashed_password: ", user_data)
    new_user = User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_user(user_id: int, update_data):
    """Update an existing user."""
    pass


async def delete_user(user_id: int):
    """Delete a user by ID."""
    pass
