#enter a number and check it armstrong
sum=0

num=int(input("enter a number "))

original_num=num

digit_count=len(str(num))

while(num!=0):


    digit=num%10

    exponent=digit**digit_count

    sum=sum+exponent

    num=num//10

print(sum)

print("numer is armstrong " if sum==original_num else"number is not armstrong")


