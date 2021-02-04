import sys
sys.path.append(".")
import pytest
from src.controller.base_controller import BaseController
from src.dao.category_dao import CategoryDao


class TestBaseController():

    @pytest.mark.parametrize('model_type', ([CategoryDao]))
    def test_instance(self, model_type):
        dao = BaseController(model_type)
        assert isinstance(dao, BaseController)
