import sys
sys.path.append('.')

from src.models.base_model import BaseModel
from sqlalchemy.orm import validates
from sqlalchemy import Column, String


class Category(BaseModel):
    __tablename__ = "CATEGORY"
    name = Column("name", String(length=100), nullable=False)
    description = Column("description", String(length=255), nullable=True)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @validates("name")
    def validate_name(self, key, name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("Name must be String")
        if not name.strip():
            raise ValueError("Name can't be empty value")
        if len(name) > 50:
            raise ValueError("Name length us too large")
        return name

    @validates("description")
    def validate_description(self, key, description: str) -> str:
        if not isinstance(description, str):
            raise TypeError("Description must be String")
        if len(description) > 300:
            raise ValueError(
                "Description lenght must not exceed 300 characters.")
        if not description.strip():
            raise ValueError("Description must not be empty")
        return description
