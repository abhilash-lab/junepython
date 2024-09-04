# read a number print sum of digit
sum=0

num=int(input("enter a number"))

while(num!=0):

    digit=num%10

    sum=digit+sum

    num=num//10

print(sum)