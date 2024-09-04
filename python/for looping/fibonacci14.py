#fibonacci number
number=int(input("enter a number"))
current=1
previous=0
next=previous+current
isfib=False

for i in range(1,number):
    next=previous+current
    if(next==number):
        isfib=True
        break
    previous=current
    current=next
print(f"is fibonacci "if isfib==True else f"is not fibonacci")
  

