import sys

integer = int(sys.argv[1])
repeat_sum = 0

while repeat_sum < 100:
    repeat_sum += integer

if repeat_sum == 100:
    print("Just 100!", end = "")
else:
    print("Over!", end = "")