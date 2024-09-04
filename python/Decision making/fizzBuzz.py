num=int(input("enter a number:"))

if(num%15==0):
    
    print("the number is fizzbuzz")

elif(num%5==0):

    print("the number is buzz")

elif(num%3==0):
    print("the number is fizz")



else:
    print("the number is not fizz or buzz or fizzbuzz")