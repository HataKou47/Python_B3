import sys
args = sys.argv

value = int(args[1])

file_name = "sheep.txt"
with open(file_name, mode="w") as f:
    for i in range(value):
        f.write(f"ひつじが{i+1}匹\n")