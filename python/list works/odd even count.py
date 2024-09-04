# find the count of odd and even numbers in the list

num=[1,2,3,4,5,6,7,8,9]

odd_count=0
even_count=0

for i in num:
    if i%2!=0:
        odd_count+=1
print(f"number of odd = {odd_count}")

for i in num:
    if i%2==0:
        even_count+=1
print(f"number of even = {even_count}")
