import pytest

from stargazers import InvariantViolation, invariant


def test_invariant():
    assert invariant(2 + 2 == 4)  # pylint: disable=E1120
    assert invariant(object, lambda x: x is not None)

    with pytest.raises(InvariantViolation):
        invariant(None, lambda x: x is not None)
    assert True
