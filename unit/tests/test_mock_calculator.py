import pytest
from unit.mocks.calculator import MockCalculator

@pytest.fixture
def mock_calculator():
    return MockCalculator()

def test_mock_add(mock_calculator):
    """モックされた add メソッドが常に 42 を返すことを確認する"""
    assert mock_calculator.add(1, 2) == 42, "モックされた add メソッドが正しく動作していません"
    assert mock_calculator.add(10, 20) == 42, "モックされた add メソッドが正しく動作していません"

def test_mock_subtract(mock_calculator):
    """モックされた subtract メソッドが常に 42 を返すことを確認する"""
    assert mock_calculator.subtract(5, 3) == 42, "モックされた subtract メソッドが正しく動作していません"
    assert mock_calculator.subtract(100, 50) == 42, "モックされた subtract メソッドが正しく動作していません"

def test_mock_multiply(mock_calculator):
    """モックされた multiply メソッドが常に 42 を返すことを確認する"""
    assert mock_calculator.multiply(2, 4) == 42, "モックされた multiply メソッドが正しく動作していません"
    assert mock_calculator.multiply(6, 7) == 42, "モックされた multiply メソッドが正しく動作していません"

def test_mock_divide(mock_calculator):
    """モックされた divide メソッドが常に 42 を返すことを確認する"""
    assert mock_calculator.divide(10, 2) == 42, "モックされた divide メソッドが正しく動作していません"
    assert mock_calculator.divide(100, 20) == 42, "モックされた divide メソッドが正しく動作していません"
