#wap to swap first and last element in  a list

num=[1,2,3,4,5,6,7,8]

# num[-1],num[0]=num[0],num[-1]

# print(num)
numbers=num.pop()
num=num.insert(0,numbers)
print(num)