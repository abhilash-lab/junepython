#fibonacci series
number=int(input("enter number "))

prevoius=0

current=1


isfibo=False

if number==0 or number==1:
      isfibo=True

else:

    next=prevoius+current

    while(next<=number):

        next=prevoius+current
    
        prevoius=current

        current=next

        if(next==number):

            isfibo=True

            break
print(isfibo)