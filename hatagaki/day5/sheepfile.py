import sys

sheep_nums = int(sys.argv[1])

with open("./day5/sheep.txt", "w") as f:
    for i in range(sheep_nums):
        f.write(f"ひつじが{i+1}匹\n")