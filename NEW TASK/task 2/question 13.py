# Python program to print the elements of an array present on odd position

arr = [1, 2, 3, 4, 5, 6, 78]

arr_len = len(arr)

for i in range(0, arr_len):
    if i % 2 == 0:
        print(arr[i])
