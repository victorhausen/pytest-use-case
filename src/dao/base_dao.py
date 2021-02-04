from src.models.base_model import BaseModel
from src.dao.session import Session


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def save(self, model: BaseModel) -> BaseModel:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()

    def read_by_id(self, id_: int) -> BaseModel:
        with Session() as session:
            obj = session.query(self.__type_model).filter_by(id_=id_).first()
        return obj

    def read_all(self) -> list:
        with Session() as session:
            model_list = session.query(self.__type_model).order_by('id').all()
        return model_list
