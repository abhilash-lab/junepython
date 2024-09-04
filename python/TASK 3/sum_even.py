# pgrm to print sum of all even numbers frm 1 to 100

start=1

end=100

sum=0

while(start<=end):

    if(start%2==0):

        sum=start+sum
 
    start=start+1
    
print(sum)

