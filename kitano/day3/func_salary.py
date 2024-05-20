# import sys
# args = sys.argv

from decimal import Decimal, ROUND_HALF_UP

# # salary = int(args[1])

# # tax = (salary - 1000000)*0.2 + 100000


def calcvalue(num):
    if num >= 1000000:
        tax = (num - 1000000)*0.2 + 100000
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
        sikyu = num - tax
        print("支給額:" +  str(sikyu) + "、", end="")
        print("税額:" + str(tax), end="")
    else:
        tax = num * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding= ROUND_HALF_UP)
        sikyu = num - tax
        print("支給額:" + str(sikyu) + "、", end="")
        print("税額:" + str(tax), end="")




# for arg in args[1:]:
#     calcvalue(int(arg))