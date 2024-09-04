num=[1,2,3,4,5,6,67,7]

# smallest=num[0]
# second_smallest=num[-1]
# for i in num:
#     if i<smallest and i<second_smallest:
#         second_smallest=smallest
#         smallest=i
#     elif i>smallest and i<second_smallest:
#         second_smallest=i
# print(second_smallest)

num.sort()
print(num[1])