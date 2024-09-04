# find second largest number

num=[1,1,2,3,4,5,5,6,7]

largest_num=num[0]

second_largest=num[0]

for i in num:

    if i >largest_num and i>second_largest:

        second_largest=largest_num
       
        largest_num=i
         
    elif i<second_largest and i>largest_num:

        second_largest=i
print(second_largest)