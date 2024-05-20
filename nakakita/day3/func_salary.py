from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    if salary > 1000000:
        tax1 = (salary - 1000000) * 0.2
        tax2 = 1000000 * 0.1
        tax = tax1 + tax2
    else:
        tax = salary * 0.1

    tax =Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

    allowance = salary - tax

    return allowance, tax

    #print ("支給額:" + str(allowance) + "、税額:" + str(tax), end="")