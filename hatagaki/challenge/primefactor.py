import sys

target_num = int(sys.argv[1])

range_num = int(target_num ** 0.5)

prime_list = []

now_v = 2

while target_num != 1:
    if target_num % now_v == 0:
        prime_list.append(now_v)
        target_num /= now_v
    else:
        now_v += 1

print(prime_list, end = "")