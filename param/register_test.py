# -*- coding: utf-8 -*-
import pytest

from param.register import *


@pytest.mark.parametrize("age,expected", [
    (20, True),
    (19, False),  # !!!
])
def test_can_register(age, expected):
    assert can_register(age) is expected


@pytest.mark.parametrize(
    "age,  is_register_mail_magazine,  use_past_month,  expected" , [
    (25  , True                      , 5              , False)     ,   # !!!
    (26  , False                     , 3              , False)    ,
    (31  , True                      , 0              , False)    ,
    (53  , False                     , 0              , False)    ,
    (17  , True                      , 2              , False)    ,
    (15  , False                     , 1              , False)    ,
    (9   , True                      , 0              , False)    ,
    (18  , False                     , 0              , False)    ,
])
def test_is_special_member(age, is_register_mail_magazine, use_past_month, expected):
    assert is_special_member(age, is_register_mail_magazine, use_past_month) is expected



"""
1. 単項目に着目した入力値の組み合わせと期待値の関係 を参考にパラメータを減らしてみよう
2. 境界値を適用したパラメータに修正してみよう
"""
