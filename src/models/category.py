import re

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates

Base = declarative_base()

class Category(Base):
    __tablename__ = "CATEGORY"
    id_ = Column("ID", Integer, nullable=False, primary_key=True)
    name = Column("NAME", String(length=50), nullable=False)
    description = Column("DESCRIPTION", String(length=300), nullable=False)

    def __init__(self, name: str, description: str, id_: int = None):
        self.id_ = id_
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
            raise ValueError("Description lenght must not exceed 300 characters.")
        if not description.strip():
            raise ValueError("Description must not be empty")
        return description