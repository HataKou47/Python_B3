import func_salary

import sys
args = sys.argv

for arg in args[1:]:
    func_salary.calcvalue(int(arg))
    # a,t = func_salary.calcvalue
    
# print(args)

# print(a,t)