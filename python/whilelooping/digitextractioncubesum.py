# sum of cube of each digit
sum=0

num=int(input("enter a number"))

while(num!=0):

    digit=num%10

    exponet=digit**3

    sum=exponet+sum

    num=num//10

print(sum)




