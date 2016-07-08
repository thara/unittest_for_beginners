# -*- coding: utf-8 -*-

from tutorial.calc import *


def test_multiply_should_return_result_of_3_and_4():
    expected = 12
    actual = multiply(3, 4)
    assert actual == expected


def test_multiply_should_return_result_of_5_and_7():
    expected = 35
    actual = multiply(5, 7)
    assert actual == expected


def test_divide_should_return_result_of_3_and_2():
    expected = 1.5
    actual = divide(3, 2)
    assert actual == expected   # !!! -> use 'from __future__ import division'
