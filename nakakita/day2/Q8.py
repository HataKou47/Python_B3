import sys
args = sys.argv
sheep = int(args[1])

for i in range(sheep):
    print("ひつじが" + str(i+1) + "匹")

""" 参考
import sys
sheep = int(sys.argv[1])
for i in range(sheep):
    print(f"ひつじが{i+1}匹")
    #教科書p73の.formatの別の書き方
"""