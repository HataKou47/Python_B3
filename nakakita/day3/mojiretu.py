s = "abcd"
print(s[-1])


s = "This is a pen." 
print(s.split()) #分けて出力
print(s.split(maxsplit=1)) #


s = "Hello".join(["chihiro","san"])
print(s)


#ハイフンでつなげる
a = ["aaa", "bbb", "ccc"]
print("-".join(a))

s = "This is a pen." 
print(s.replace("pen", "note"))
print(s)