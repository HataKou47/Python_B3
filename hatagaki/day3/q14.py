import sys

args = sys.argv

def odd_even(num):
    if num % 2 == 0:
        print(f"{num}は偶数")
    else:
        print(f"{num}は奇数")

for i in args[1:]:
    odd_even(int(i))