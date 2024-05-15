import sys
arg =  sys.argv
# arg = int(sys.argv[1])
i = int(arg[1])

total = 0

while total < 100:
    total += i
if total == 100:
        print("Just 100!", end = "")
else:
        print("Over!", end = "")