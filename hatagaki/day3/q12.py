import sys

args = sys.argv

text = args[1]
word_num = int(args[2])

print(text.split()[word_num-1], end="")