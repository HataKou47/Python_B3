# マジックナンバーを避け、定数を用いた
# 目的ごとにを関数にまとめた
# 関数の動作をdocstringで追記し、関数内の動作を明確にした

import sys

def calc_tax(salary):
    """
    給与額から税額を求める関数

    Parameters
    ----------
    salary : int
        給与額

    Returns
    -------
    tax : float
        税額
    """
    if salary > THRESHOLD:
        salary_tmp = salary - THRESHOLD
        tax = salary_tmp * PROGRESSIVE_TAX_UP_RATE \
            + THRESHOLD * PROGRESSIVE_TAX_DOWN_RATE
    else:
        tax = salary * PROGRESSIVE_TAX_DOWN_RATE

    return tax


def round_int(number):
    """
    与えられた浮動小数点型の数字の小数第1位を四捨五入し、整数型に変換する関数

    Parameters
    ----------
    number : float
        float型の小数
    
    Returns
    -------
    number : int
        引数numberの小数第1位を四捨五入した値
    """
    if number - int(number) >= 0.5:
        number = int(number) + 1
    else:
        number = int(number)

    return number


THRESHOLD = 1000000  # 税率が20%となる閾値
PROGRESSIVE_TAX_UP_RATE = 0.2  # THRESHOLDを超えた際の税率 
PROGRESSIVE_TAX_DOWN_RATE = 0.1  # THRESHOLDを超えなかった際の税率

args = sys.argv
salary = int(args[1])

tax = calc_tax(salary)
tax = round_int(tax)

gives_money = salary - tax

print(f"支給額:{gives_money}、税額:{tax}", end = "")