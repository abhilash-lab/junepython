# . Python program to determine whether the given number is a Harshad Number

num=int(input("enter a number:"))
og_num=num
sum=0
while (num!=0):    
    digit=num%10
    sum+=digit
    num=num//10
if og_num%sum==0:
    print(f"{og_num} is harshad number")
else:
    print(f"{og_num} is not harshad number")



    


