import pytest
from quickcalc.core import add, subtract, multiply, divide, DivisionByZeroError


def test_addition_basic():
    assert add(5, 3) == 8.0


def test_subtraction_basic():
    assert subtract(10, 4) == 6.0


def test_multiplication_basic():
    assert multiply(6, 7) == 42.0


def test_division_basic():
    assert divide(8, 2) == 4.0


def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)


def test_negative_numbers():
    assert subtract(-5, -3) == -2.0


def test_decimals():
    assert add(2.5, 0.75) == 3.25


def test_large_numbers():
    assert multiply(1_000_000, 3_000_000) == 3_000_000_000_000.0