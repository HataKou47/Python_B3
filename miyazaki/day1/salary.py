import sys
args = sys.argv

salary = int(args[1])

tax_amount = 0.0
amount_paid = 0.0

if (salary > 1000000):
    tax_amount = round((salary - 1000000) * 0.2 + 100000)
    amount_paid = salary - tax_amount
else:
    tax_amount = round(salary * 0.1)
    amount_paid = salary - tax_amount

print("支給額:" + str(amount_paid) + "、" + "税額:" + str(tax_amount), end="")
