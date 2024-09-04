#armstrong or not

def is_armstrong(num):
    orginal=num
    sum=0
    digit_count=len(str(num))
    while(num!=0):
        digit=num%10
        exponent=digit**digit_count
        sum=sum+exponent
        num=num//10
        if orginal==sum:
            return True
    return False
print(is_armstrong(123))
