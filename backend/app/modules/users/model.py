from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"
    client = "client"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    email: str = Field(unique=True)
    password: str
    phone: str
    street: str
    city: str
    province: str
    country: str
    role: Role = Field(default=Role.user)
    registered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active: bool = Field(default=True)
