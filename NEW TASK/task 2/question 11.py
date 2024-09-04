#  Python program to print the duplicate elements of an array

arr=[1,2,3,4,5,6,6,6,7,8,8]

array={}
for i in arr:
    if i in array:
        print(i)
    else:
        array[i]=1

   