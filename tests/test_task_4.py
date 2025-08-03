import pytest

from src.task_4 import SumMultiples, SumMultiplesModel

EXPECTED_SUMS = {
    10: 23,
    20: 78,
    100: 2318,
    0: 0,
    -10: 'The limit must be a non-negative integer.',
    'string': 'An integer is required',
}


def test_sum_multiple_10():
    """Test with a multiple of 10."""
    data = SumMultiplesModel(number=10)
    sum_calculated = SumMultiples(data)
    assert sum_calculated.calculate() == EXPECTED_SUMS[10]


def test_sum_multiple_20():
    """Test with a multiple of 20."""
    data = SumMultiplesModel(number=20)
    sum_calculated = SumMultiples(data)
    assert sum_calculated.calculate() == EXPECTED_SUMS[20]


def test_sum_multiple_100():
    """Test with a multiple of 100."""
    data = SumMultiplesModel(number=100)
    sum_calculated = SumMultiples(data)
    assert sum_calculated.calculate() == EXPECTED_SUMS[100]


def test_sum_multiple_0():
    """Test with zero."""
    data = SumMultiplesModel(number=0)
    sum_calculated = SumMultiples(data)
    assert sum_calculated.calculate() == EXPECTED_SUMS[0]


def test_sum_multiple_negative():
    """Test with a negative limit."""
    with pytest.raises(
        ValueError,
        match='Input should be greater than or equal to 0',
    ):
        SumMultiplesModel(number=-10)


def test_sum_multiple_negative_string():
    """Test with a string limit."""
    with pytest.raises(
        ValueError,
        match=(
            'Input should be a valid integer, '
            'unable to parse string as an integer'
        ),
    ):
        SumMultiplesModel(number='string')
