#print armstrong from numbers 
numbers=[151,153,154,370,371,372,373,16341,1635]


for i in range(0,len(numbers)):
    sum=0
    orginal=numbers[i]
    digit_count=len(str(numbers[i]))
    while numbers[i]>0:
        digit=numbers[i]%10
        exponent=digit**digit_count
        sum=sum+exponent
        numbers[i]=numbers[i]//10
    if sum==orginal:
        print(orginal)



