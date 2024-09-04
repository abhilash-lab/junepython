#check palindrome

def is_palindrom(num):
    orginal=num
    result=0
    while(num!=0):
        digit=num%10
        result=result*10+digit
        num=num//10
        if orginal==result:
            return True
    return False

print(is_palindrom(123))
