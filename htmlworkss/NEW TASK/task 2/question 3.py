# Python Program to Make a Simple Calculator

num1=int(input("enter the first number"))
operator=input("enter the operator")
num2=int(input("enter the second number"))

if operator=="+":
    result=num1+num2
    print(f"result={result}")
elif operator=="*":
    result=num1*num2
    print(f"result={result}")
elif operator=="-":
    result=num1-num2
    print(f"result={result}")
elif operator=="%":
    result=num1%num2
    print(f"result={result}")
elif operator=="/":
    result=num1/num2
    print(f"result={result}")
else:
    print("invalid")
