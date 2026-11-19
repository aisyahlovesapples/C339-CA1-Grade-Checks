import pytest
from grade_average import calculate_average


def test_average_zero():
    assert calculate_average(0, 0) == 0


def test_average_hundred():
    assert calculate_average(100, 100) == 100


def test_average_boundary():
    assert calculate_average(0, 100) == 50


def test_average_fraction():
    assert calculate_average(50, 51) == 50.5


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        ("50", 50),
        (50, "50"),
        (None, 50),
        (50, None),
        (True, 50)
    ]
)
def test_average_type_errors(mark_one, mark_two):
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),
        (50, -1),
        (101, 50),
        (50, 101)
    ]
)
def test_average_value_errors(mark_one, mark_two):
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)