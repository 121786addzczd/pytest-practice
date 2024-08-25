import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture
def add_valid_data():
    return [
        (1, 2, 3),
        ("1", 2, 3),
    ]

@pytest.fixture
def add_invalid_data():
    return [
        ("1", "two"),
    ]

@pytest.fixture
def subtract_valid_data():
    return [
        (5, 3, 2),
        ("5", 3, 2),
    ]

@pytest.fixture
def subtract_invalid_data():
    return [
        ("five", 3),
    ]

@pytest.fixture
def multiply_valid_data():
    return [
        (2, 4, 8),
        ("2", 4, 8),
    ]

@pytest.fixture
def multiply_invalid_data():
    return [
        ("two", 4),
    ]

@pytest.fixture
def divide_valid_data():
    return [
        (10, 2, 5),
        ("10", 2, 5),
    ]

@pytest.fixture
def divide_invalid_data():
    return [
        (10, "two"),
    ]
