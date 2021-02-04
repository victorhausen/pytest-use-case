import sys
sys.path.append(".")
import pytest
from src.models.base_model import BaseModel


class TestBaseModel():
    @pytest.fixture()
    def create_instance(self):
        obj = BaseModel()
        return obj

    def test_base_model(self, create_instance):
        assert isinstance(create_instance, BaseModel)
