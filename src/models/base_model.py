from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id_ = Column("ID", Integer, nullable=False, primary_key=True)
    
    @validates("id_")
    def validate_id_(self, key, id_: str):
        if isinstance(id_, int) or not id_:
            raise ValueError("Id must be int or none")
        return id_
