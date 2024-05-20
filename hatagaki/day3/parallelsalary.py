import sys
import func_salary

args = sys.argv

for i in args[1:]:
    given_money, tax = func_salary.calcsalary(int(i))

    print(f"給与:{i}、支給額:{given_money}、税額:{tax}")