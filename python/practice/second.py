num=[1,3,2,5,7,9,10,4]

second_largest=num[0]

largest_num=num[0]

for i in num:
    

    if i>largest_num and i>second_largest:

        second_largest=largest_num

        largest_num=i   

    elif i<second_largest and i>largest_num:

        second_largest=i

print(second_largest)





