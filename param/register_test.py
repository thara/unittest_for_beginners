# -*- coding: utf-8 -*-
import pytest

from param.register import *


@pytest.mark.parametrize("age,expected", [
    (19, True),
    (18, True),
    (17, False),
])
def test_can_register(age, expected):
    assert can_register(age) is expected


@pytest.mark.parametrize(
    "age , is_register_mail_magazine , use_past_month , expected" , [
    (20  , True                      , 1              , True)     ,
    (19  , True                      , 1              , False)    ,
    (20  , False                     , 1              , False)    ,
    (20  , True                      , 0              , False)    ,
])
def test_is_special_member(age, is_register_mail_magazine, use_past_month, expected):
    actual = is_special_member(age, is_register_mail_magazine, use_past_month)
    assert actual is expected



"""
1. 単項目に着目した入力値の組み合わせと期待値の関係 を参考にパラメータを減らしてみよう
2. 境界値を適用したパラメータに修正してみよう
"""
