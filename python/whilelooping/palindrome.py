# pgrm to check a number is palindrome or not

num=int(input("enter the number "))
original=num
result=0
while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10
print(result)
print("palindrome" if result==original else "not palindrome")