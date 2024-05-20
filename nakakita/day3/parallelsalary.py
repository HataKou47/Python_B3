import func_salary

import sys
args = sys.argv

for i in args[1:]:
    func_salary.calcsalary(int(i))
    a, t = func_salary.calcsalary(int(i))

print("給与:" + str(i) + "、支給額:" + str(a) + "、税額:" + str(t))
#print(args)