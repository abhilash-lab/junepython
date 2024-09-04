number=int(input("enter a number"))

previous=0

current=1

print(f"{previous},{current}",end=" , ")

for i in range (1,number+1):

    next=previous+current
    previous=current
    current=next

    print(f"{next}",end=" , ")


