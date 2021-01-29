import sys
sys.path.append(".")

import pytest
from src.models.category import Category


# TEST NAME
@pytest.mark.parametrize("name, description", [
                            (10, 'é um número, mas não era pra ser'),
                            (None, 'é um número, mas não era pra ser')
                        ])
def test_name_not_str(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)


def test_name_length():
    with pytest.raises(ValueError):
        category = Category("Name"*100, "é muito grande")
 

def test_name_not_empty():
    with pytest.raises(ValueError):
        category = Category("", "valid description")


# TEST DESCRIPTION
@pytest.mark.parametrize("name, description", [
                            ("valid name", 10),
                            ("valid name", None)
                        ])
def test_description_not_str(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)


def test_description_length():
    with pytest.raises(ValueError):
        category = Category("valid_name", "too large description"*300)


def test_description_not_empty():
    with pytest.raises(ValueError):
        category = Category("valid name", " ")
