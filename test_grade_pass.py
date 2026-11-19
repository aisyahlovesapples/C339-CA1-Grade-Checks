import pytest
from grade_pass import has_passed


def test_score_49():
    assert has_passed(49) is False


def test_score_50():
    assert has_passed(50) is True


def test_score_51():
    assert has_passed(51) is True


def test_score_100():
    assert has_passed(100) is True


@pytest.mark.parametrize(
    "score",
    [
        "50",
        None,
        True
    ]
)
def test_type_errors(score):
    with pytest.raises(TypeError):
        has_passed(score)


@pytest.mark.parametrize(
    "score",
    [
        -1,
        101
    ]
)
def test_value_errors(score):
    with pytest.raises(ValueError):
        has_passed(score)