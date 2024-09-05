# Write a program to determine largest of three numbers 

num1=int(input(f"enter first number="))
num2=int(input(f"enter second number="))
num3=int(input(f"enter thirdnumber="))

if num1>num2 and num1>num3:
    print(f"{num1} is largest")

elif num2>num1 and num2>num3:
    print(f"{num2} is largest")

elif num3>num1 and num3>num2: 
    print(f"{num3} is largest")
else:
    print("three numbers are equal")