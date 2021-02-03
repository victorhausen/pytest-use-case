import sys
sys.path.append(".")
import pytest
from src.dao.base_dao import BaseDao
from src.models.category import Category


class TestBaseDao():

    @pytest.mark.parametrize('model_type', ([Category]))
    def test_instance(self, model_type):
        dao = BaseDao(model_type)
        assert isinstance(dao, BaseDao)
