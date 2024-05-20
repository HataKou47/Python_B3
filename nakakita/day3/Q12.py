import sys
args = sys.argv

s = args[1]
num = int(args[2])
s2 = s.split() #分けただけだから代入する
#print(s,s2)

print(s2[num-1],end="")