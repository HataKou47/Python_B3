import sys

args = sys.argv

salary = int(args[1])

if salary > 1000000:
    salary_tmp = salary - 1000000
    tax = salary_tmp * 0.2 + 100000
else:
    tax = salary * 0.1

if tax - int(tax) >= 0.5:
    tax = int(tax) + 1
else:
    tax = int(tax)

gives_money = salary - tax

print(f"支給額:{gives_money}、税額:{tax}", end = "")