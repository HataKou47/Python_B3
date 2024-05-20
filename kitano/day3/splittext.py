import sys

arg = sys.argv

s = arg[1]
i = int(arg[2])

s2 = s.split()

print(s2[i - 1])