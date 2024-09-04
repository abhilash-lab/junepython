#print number s of object in numbers 
#print length og numbers 
#print even numbers from numbers 
#print total numbers 
# print total odd from numbers 

numbers=[10,11,12,34,43,54,19,78,42]
total_odd=0
print(numbers)
number_object=len(numbers)
print(number_object)
for i in range(0,number_object):
    if numbers[i]%2==0:
        print(numbers[i])
for i in range(0,len(numbers)):
    if numbers[i]%2!=0:
        total_odd+=numbers[i]
        print(total_odd)
            