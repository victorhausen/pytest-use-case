import sys
sys.path.append('.')

from src.models.category import Category
from src.dao.base_dao import BaseDao


class CategoryDao(BaseDao):
    def __init__(self) -> None:
        self.__type_model = Category
        super().__init__(self.__type_model)
