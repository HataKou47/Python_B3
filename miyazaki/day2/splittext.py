import sys
args = sys.argv

english = args[1]
index = int(args[2])

english = english.split()

print(english[index-1])
