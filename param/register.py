# -*- coding: utf-8 -*-


def can_register(age):
    """年齢を指定して、会員制サイトへ登録できるかを返す

    Args:
        age: 年齢
    Returns:
        18歳異様ならば真、18歳未満ならば偽
    """
    return 18 <= age


"""
| 結果  | 入力値の例 | 備考       |
| ----- | ---------- | ---------- |
| true  | 20         | 18以上の値 |
| false | 10         | 18未満の値 |
"""


def is_special_member(age, is_register_mail_magazine, use_past_month):
    """優待会員かどうかを返す

    Args:
        age: 年齢
        is_register_mail_magazine: メールマガジンに登録している場合に真
        use_past_month: 前月の利用回数
    Returns:
        20歳以上であり、メールマガジンに登録してあり、かつ前月の利用回数が1回以上なら真
    """
    if age < 20:
        return False
    if not is_register_mail_magazine:
        return False
    if use_past_month < 1:
        return False
    return True


"""
入力値の組み合わせと期待値の関係

| 年齢     | メルマガ登録 | 前月の利用回数 | 期待値 |
| -------- | ------------ | -------------- | ------ |
| 20歳以上 | YES          | 1回以上        | true   |
| 20歳以上 | NO           | 1回以上        | false  |
| 20歳以上 | YES          | 0回            | false  |
| 20歳以上 | NO           | 0回            | false  |
| 20歳未満 | YES          | 1回以上        | false  |
| 20歳未満 | NO           | 1回以上        | false  |
| 20歳未満 | YES          | 0回            | false  |
| 20歳未満 | NO           | 0回            | false  |
"""


"""
単項目に着目した入力値の組み合わせと期待値の関係

「プログラムに混入する不具合のほとんどは単項目に関連する不具合である」という性質を踏まえ、
テストの品質を落とさずテストデータを減らす。


| 年齢     | メルマガ登録 | 前月の利用回数 | 期待値 |
| -------- | ------------ | -------------- | ------ |
| 20歳以上 | YES          | 1回以上        | true   |
| 20歳未満 | YES          | 1回以上        | false  |
| 20歳以上 | NO           | 1回以上        | false  |
| 20歳以上 | YES          | 0回            | false  |


---

具体的なテストデータ

| 年齢     | メルマガ登録 | 前月の利用回数 | 期待値 |
| -------- | ------------ | -------------- | ------ |
| 20       | True         | 1              | True   |
| 19       | True         | 3              | False  |
| 25       | False        | 2              | False  |
| 31       | True         | 0              | False  |


---
境界値を適用したテストデータ

| 年齢     | メルマガ登録 | 前月の利用回数 | 期待値 |
| -------- | ------------ | -------------- | ------ |
| 20       | True         | 1              | True   |
| 19       | True         | 1              | False  |
| 20       | False        | 1              | False  |
| 20       | True         | 0              | False  |
"""
