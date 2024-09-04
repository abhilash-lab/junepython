# read start_limit and end_limit frm the user and print all the odd numbers frm the start_limit to end_limit

start_limit=int(input("enter the starting limit"))

end_limit=int(input("enter the end limit "))

while(start_limit<=end_limit):

    if (start_limit%2!=0):

        print(start_limit)
    
    start_limit=start_limit+1