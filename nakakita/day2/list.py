a = [10, 22, 30, 45]

a[1] = 555 #置き換え

print (len(a)) #要素数
print(a)
print(a[1])
print(type(a))



b = [10, "あいうえお", 30, 45]

print(b)

for i in b:
    print(type(i))


x = [10, 555, 30, 45]

print(x[1:3]) #実際は1と2
print(x[1:]) #省略すると1から残り全部
print(x[:2]) #前を全部


nums = [0, 1, 2, 3, 4]
print(nums)

del nums[2]
print(nums)

del nums[2:4]
print(nums)