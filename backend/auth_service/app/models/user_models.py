from sqlalchemy import Column
from sqlalchemy.sql import text
from sqlalchemy.types import TIMESTAMP, String, Uuid
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Uuid,
        primary_key=True,
        nullable=False,
        server_default=text("uuid_generate_v4()"),
    )
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )
