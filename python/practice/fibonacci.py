
num=int(input("enter the number"))

current=1
previous=0  
print(f"{previous} ,{current}",end=",")

for i in range(1,num+1):
    next=current+previous
    previous=current
    current=next

    print(f"{next}",end=",")