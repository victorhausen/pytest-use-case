import sys
sys.path.append(".")
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.controller.category_controller import CategoryController
from src.models.category import Category
import pytest


class TestCategory():

    @pytest.fixture()
    def create_instance_model(self):
        obj = Category('name', 'description')
        return obj

    @pytest.fixture()
    def create_instance_controller(self):
        controller = CategoryController
        return controller

    def test_save(self, create_instance_model, create_instance_controller):
        result = create_instance_controller().save(create_instance_model)

        assert result is not None

        create_instance_controller().delete(result)

    def test_not_save(self, create_instance_controller):
        with pytest.raises(UnmappedInstanceError) as error:
            create_instance_controller().save('invalid_model')

    def test_delete(self, create_instance_model, create_instance_controller):
        result = create_instance_controller().save(create_instance_model)
        id_ = result.id_

        create_instance_controller().delete(result)
        result = create_instance_controller().read_by_id(id_)

        assert result is None

    def test_not_delete(self, create_instance_model, create_instance_controller):
        result = create_instance_controller().save(create_instance_model)
        id_ = result.id_

        with pytest.raises(UnmappedInstanceError) as error:
            create_instance_controller().delete('result')
        result = create_instance_controller().read_by_id(id_)

        assert result is not None

    def test_read_all(self, create_instance_model, create_instance_controller):
        result = create_instance_controller().read_all()

        assert isinstance(result, list)

    def test_read_by_id(self, create_instance_model, create_instance_controller):
        result = create_instance_controller().save(create_instance_model)
        final_result = create_instance_controller().read_by_id(result.id_)

        assert isinstance(final_result, Category)

        create_instance_controller().delete(final_result)

    def test_not_read_by_id(self, create_instance_model, create_instance_controller):
        result = create_instance_controller().read_by_id('invalid_id')
        assert result is None