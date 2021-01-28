import sys
sys.path.append(".")

from src.models.category import Category

# TEST NAME
def test_name_not_str():
    try:
        category = Category(10, "é um número, mas não era pra ser")
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, TypeError)


def test_name_length():
    try:
        too_large_name = "".join(["a" for e in range(100)])
        category = Category(too_large_name, "é muito grande")
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, ValueError)

def test_name_not_empty():
    try:
        category = Category("", "valid description")
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, ValueError)

def test_numeric_in_name():
    try:
        category = Category("abc12", "valid description")
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, ValueError)


# TEST DESCRIPTION

def test_description_not_str():
    try:
        category = Category("valid name", 10)
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, TypeError)


def test_description_length():
    try:
        too_large_description = "".join(["a" for e in range(400)])
        category = Category("valid_name", too_large_description)
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, ValueError)

def test_description_not_empty():
    try:
        category = Category("valid name", " ")
        raise NotImplementedError("Exception not raised")
    except Exception as error:
        assert isinstance(error, ValueError)
