# 関数の外側でvalueに100を代入
value = 100

def changeValue():
    global value
    value = 20

print(value)

changeValue()
print("value=",value) # <--- はたしてこの値は？
