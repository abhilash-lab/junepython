num1=int(input("Enter number1 "))
num2=int(input("Enter number2 "))
HCF=1

for i in range(1,num1+1,1):    
    if num1%i==0 and num2%i==0:
        HCF=i
print(HCF)