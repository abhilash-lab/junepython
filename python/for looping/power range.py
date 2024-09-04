# print the power range of a number

num=int(input("Enter a number "))
pattern=0
sum=0
for i in range(1,num+1,1):
    pattern=pattern*10+num
    sum=sum+pattern
print(sum)
    















# power range
# 
# 2 [2+22] 24
# 3 [3+33+333] 369   