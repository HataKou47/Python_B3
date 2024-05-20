# テキスト問題
# モジュールを用いて、複数の給与の支払い額を計算する（元）

import sys
from text_func_salary import calcsalary
args = sys.argv


for i in args[1:]:
    amount_paid, tax_amount = calcsalary(int(i))
    print(f"給与:{i}、支給額:{amount_paid}、税額:{tax_amount}")