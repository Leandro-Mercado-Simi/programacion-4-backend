from sqlmodel import SQLModel
from pydantic import Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"
    client = "client"


class UserCreate(SQLModel):
    first_name: str = Field(..., max_length=20, example="John")
    last_name: str = Field(..., max_length=20, example="Doe")
    email: EmailStr = Field(..., example="johndoe@mail.com")
    password: str = Field(..., min_length=8, max_length=150, example="Abcd1234")
    phone: str = Field(
        ..., pattern=r"^\+?\d{7,15}$", json_schema_extra={"example": "+5492611234567"}
    )
    street: str = Field(..., max_length=50, example="Av. Bandera de los Andes 11548")
    city: str = Field(..., max_length=50, example="Godoy Cruz")
    province: str = Field(..., max_length=50, example="Mendoza")
    country: str = Field(..., max_length=50, example="Argentina")
    role: Role = Field(default=Role.user)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError("Debe tener al menos una mayúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("Debe tener al menos un número")
        return v


class UserRead(SQLModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    street: str
    city: str
    province: str
    country: str
    role: Role
    registered_at: datetime
    is_active: bool


class UserUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
    phone: Optional[str] = Field(None, pattern=r"^\+?\d{7,15}$")
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    role: Optional[Role] = None
    is_active: Optional[bool] = None

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if not any(c.isupper() for c in v):
            raise ValueError("Debe tener al menos una mayúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("Debe tener al menos un número")
        return v
