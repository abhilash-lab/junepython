# wap to find largest number without using methods
number=[1,11,2,3,4,5,5,6]

largest_num=number[0]

for i in number:

    if i>largest_num:

        largest_num=i

print(largest_num)
