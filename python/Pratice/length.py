num=int(input("enter a number" ))
orginal=num
sum=0
digit_count=len(str(num))
while(num!=0):
    digit=num%10
    exponent=digit**digit_count
    sum=sum+exponent
    num=num//10

print(f"given number is armstrong" if sum==orginal else f"not armstrong" )



