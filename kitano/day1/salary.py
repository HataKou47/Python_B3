import sys
arg = sys.argv

from decimal import Decimal, ROUND_HALF_UP

salary = int(arg[1])

tax = (salary - 1000000)*0.2 + 100000



if salary >= 1000000:
    tax = (salary - 1000000)*0.2 + 100000
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
    sikyu = salary - tax
    print("支給額:" + sikyu + "、", end="")
    print("税額:" + tax, end="")
else:
    tax = salary * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
    sikyu = salary - tax
    print("支給額:" + sikyu + "、", end="")
    print("税額:" + tax, end="")

