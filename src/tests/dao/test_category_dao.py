import sys
sys.path.append(".")
from sqlalchemy.orm.exc import UnmappedInstanceError
import pytest
from src.dao.category_dao import CategoryDao
from src.models.category import Category


class TestCategory():

    @pytest.fixture()
    def create_instance_model(self):
        obj = Category('name', 'description')
        return obj

    @pytest.fixture()
    def create_instance_dao(self):
        dao = CategoryDao
        return dao

    def test_save(self, create_instance_model, create_instance_dao):
        result = create_instance_dao().save(create_instance_model)

        assert result is not None

        create_instance_dao().delete(result)

    def test_not_save(self, create_instance_dao):
        with pytest.raises(UnmappedInstanceError) as error:
            create_instance_dao().save('invalid_model')

    def test_delete(self, create_instance_model, create_instance_dao):
        result = create_instance_dao().save(create_instance_model)
        id_ = result.id_

        create_instance_dao().delete(result)
        result = create_instance_dao().read_by_id(id_)

        assert result is None

    def test_not_delete(self, create_instance_model, create_instance_dao):
        result = create_instance_dao().save(create_instance_model)
        id_ = result.id_

        with pytest.raises(UnmappedInstanceError) as error:
            create_instance_dao().delete('result')
        result = create_instance_dao().read_by_id(id_)

        assert result is not None

    def test_read_all(self, create_instance_model, create_instance_dao):
        result = create_instance_dao().read_all()

        assert isinstance(result, list)

    def test_read_by_id(self, create_instance_model, create_instance_dao):
        result = create_instance_dao().save(create_instance_model)
        final_result = create_instance_dao().read_by_id(result.id_)

        assert isinstance(final_result, Category)

        create_instance_dao().delete(final_result)

    def test_not_read_by_id(self, create_instance_model, create_instance_dao):
        result = create_instance_dao().read_by_id('invalid_id')
        assert result is None
