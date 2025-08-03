import pytest

from src.task_3 import Factorial, FactorialModel

EXPECTED_FACTORIALS = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}


def test_fatorial_5():
    data = FactorialModel(number=5)
    fatorial_calculado = Factorial(data)
    assert fatorial_calculado.calculate() == EXPECTED_FACTORIALS[5]


def test_fatorial_0():
    data = FactorialModel(number=0)
    fatorial_calculado = Factorial(data)
    assert fatorial_calculado.calculate() == EXPECTED_FACTORIALS[0]


def test_fatorial_1():
    data = FactorialModel(number=1)
    fatorial_calculado = Factorial(data)
    assert fatorial_calculado.calculate() == EXPECTED_FACTORIALS[1]


def test_fatorial_negative():
    with pytest.raises(
        ValueError, match='Input should be greater than or equal to 0'
    ):
        FactorialModel(number=-1)


def test_fatorial_string():
    with pytest.raises(
        ValueError,
        match=(
            'Input should be a valid integer, '
            'unable to parse string as an integer'
        ),
    ):
        FactorialModel(number='string')
