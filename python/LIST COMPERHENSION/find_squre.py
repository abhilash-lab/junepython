#find squre

lst=[10,2,3,4,5,6,]
squres=[n**2 for n in lst]
print(squres)
even_num=[n for n in lst if n%2==0]
print(even_num)
odd_num=[n for n in lst if n%2!=0]
print(odd_num)