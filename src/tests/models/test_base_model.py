import sys
sys.path.append(".")

from src.models.base_model import BaseModel

def test_id_():
    try:
        base_model = BaseModel()
        base_model.id_ = "a"
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, ValueError)