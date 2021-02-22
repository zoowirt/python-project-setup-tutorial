from arithmetics.adding_numbers import add_numbers


def test_adding_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(1, 2) == 3


import pytest


# @pytest.mark.parametrize('x', [1.0, 2.0])
# @pytest.mark.parametrize('y', [3.0, 4.0])
# @pytest.mark.parametrize('y', [3.0, 4.0])