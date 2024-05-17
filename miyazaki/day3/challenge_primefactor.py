# チャレンジ問題（1）
# 入力された数を素因数分解して要素を出力する

import sys
args = sys.argv

num = int(args[1])

def prime_factorize(n):
    element = []
    for i in range(2, n+1):
        while (n % i == 0):
            element.append(i)
            n //= i
    return element

ans = prime_factorize(num)

print(ans, end="")