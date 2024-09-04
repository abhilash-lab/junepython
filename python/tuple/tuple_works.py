#add an element
numbers=[1,2,[3,(100,200,300),4],5,6]

# new_num=numbers[2]
# num=numbers[2][1]
# lst=list(num)
# lst.insert(1,150)
# tup=tuple(lst)
# numbers[2][1]=tup
# new=new_num.pop()
# add=new_num.insert(1,new)



num=numbers[2]                        # [3,(100,200,300),4]
poped_ele=num.pop()                   # poped_ele=4
num.insert(1,poped_ele)               # [3,4,(100,200,300)]
new_num=numbers[2][2]                 # (100,200,300)
lst=list(new_num)                     # [100,200,300]
lst.insert(1,150)                     # [100,150,200,300]
tup=tuple(lst)                        # (100,150,200,300)
numbers[2][2]=tup

print(numbers)                        # [1,2,[3,4,(100,150,200,300)],5,6]

