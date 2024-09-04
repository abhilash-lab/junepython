numbers=[1,2,[3,(100,200,300),4],5,6]
num=numbers[2]
poped=num.pop()
num.insert(1,poped)
ele=num[2]
lst=list(ele)
lst.insert(1,150)
tup=tuple(lst)
numbers[2][2]=tup




print(numbers)


