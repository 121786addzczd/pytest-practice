import pytest
from unit.fixtures.calculator_fixture import (
    calculator,
    add_valid_data,
    add_invalid_data,
    subtract_valid_data,
    subtract_invalid_data,
    multiply_valid_data,
    multiply_invalid_data,
    divide_valid_data,
    divide_invalid_data,
)

def test_add_valid_inputs(calculator, add_valid_data):
    """数値と数値または文字列と数値の足し算が正しく計算されること"""
    for left_operand, right_operand, expected in add_valid_data:
        assert calculator.add(left_operand, right_operand) == expected, f"{left_operand} + {right_operand} は {expected} であるべきです"

def test_add_invalid_inputs(calculator, add_invalid_data):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    for left_operand, right_operand in add_invalid_data:
        with pytest.raises(ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"):
            calculator.add(left_operand, right_operand)

def test_subtract_valid_inputs(calculator, subtract_valid_data):
    """数値と数値または文字列と数値の引き算が正しく計算されること"""
    for left_operand, right_operand, expected in subtract_valid_data:
        assert calculator.subtract(left_operand, right_operand) == expected, f"{left_operand} - {right_operand} は {expected} であるべきです"

def test_subtract_invalid_inputs(calculator, subtract_invalid_data):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    for left_operand, right_operand in subtract_invalid_data:
        with pytest.raises(ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"):
            calculator.subtract(left_operand, right_operand)

def test_multiply_valid_inputs(calculator, multiply_valid_data):
    """数値と数値または文字列と数値の掛け算が正しく計算されること"""
    for left_operand, right_operand, expected in multiply_valid_data:
        assert calculator.multiply(left_operand, right_operand) == expected, f"{left_operand} * {right_operand} は {expected} であるべきです"

def test_multiply_invalid_inputs(calculator, multiply_invalid_data):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    for left_operand, right_operand in multiply_invalid_data:
        with pytest.raises(ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"):
            calculator.multiply(left_operand, right_operand)

def test_divide_valid_inputs(calculator, divide_valid_data):
    """数値と数値または文字列と数値の割り算が正しく計算されること"""
    for left_operand, right_operand, expected in divide_valid_data:
        assert calculator.divide(left_operand, right_operand) == expected, f"{left_operand} / {right_operand} は {expected} であるべきです"

def test_divide_invalid_inputs(calculator, divide_invalid_data):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    for left_operand, right_operand in divide_invalid_data:
        with pytest.raises(ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"):
            calculator.divide(left_operand, right_operand)

@pytest.mark.raises
def test_divide_by_zero(calculator):
    """ゼロで割ろうとした時に適切な例外が発生すること"""
    with pytest.raises(ValueError, match="ゼロで割ることはできません"):
        calculator.divide(10, 0)
