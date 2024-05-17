def calcsalary(salary):
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

    return gives_money, tax