# -*- coding: utf-8 -*-
from __future__ import division


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("divide by zero")
    return x / y
