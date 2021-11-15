import pytest


# def func(x):
#     return 'hello'
#
#
# def test_answer1():
#     assert func(3) == 'hello'

# def test_even():
#     num = 11
#     assert num % 2 == 0, "Num is odd num, should be even"

# def test_zero_division_1():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0


def test_zero_division_2():
    with pytest.raises(ZeroDivisionError):
        1 / 2
