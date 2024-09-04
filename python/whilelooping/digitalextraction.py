#read a number abd extract 

num=int(input("enter a number"))

while(num!=0):

    digits=num%10

    print(digits)
    
    num=num//10
    

    