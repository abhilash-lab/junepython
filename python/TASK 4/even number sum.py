# pgrm to print sum of all even numbers frm 1 to 100

sum=0

for num in range(1,101):

    if(num%2==0):

        sum=num+sum

print(sum)