# テキスト問題
# モジュールを用いて、複数の給与の支払い額を計算する（モジュール）

def calcsalary (salary):
    tax_amount = 0.0
    amount_paid = 0.0

    if (salary > 1000000):
        tax_amount = round((salary - 1000000) * 0.2 + 100000)
        amount_paid = salary - tax_amount
    else:
        tax_amount = round(salary * 0.1)
        amount_paid = salary - tax_amount

    return amount_paid, tax_amount