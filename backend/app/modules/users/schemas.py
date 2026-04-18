from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime, timezone
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"
    client = "client"


class Address(BaseModel):
    street: str = Field(..., example="Av. San Martín 1234")
    city: str = Field(..., example="Guaymallén")
    province: str = Field(..., example="Mendoza")
    country: str = Field(..., example="Argentina")


class UserBase(BaseModel):
    first_name: str = Field(..., max_length=20, example="John")
    last_name: str = Field(..., max_length=20, example="Doe")
    email: EmailStr = Field(..., example="johndoe@mail.com")
    password: str = Field(..., min_length=8, example="Abcd1234")
    phone: str = Field(
        ..., pattern=r"^\+?\d{7,15}$", json_schema_extra={"example": "+5492611234567"}
    )
    address: Address
    role: Role
    registered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active: bool = True

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError("Debe tener al menos una mayúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("Debe tener al menos un número")
        return v


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(
        None,
        min_length=8,
    )
    phone: Optional[str] = Field(None, pattern=r"^\+?\d{7,15}$")
    address: Optional[Address] = None
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


class UserRead(UserBase):
    id: int
