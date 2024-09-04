# Write program for a simple calculator 

num1=int(input("enter the first number="))
operator=input("enter the operator=(+, -, *, /,%)")
num2=int(input("enter the second number="))

if operator=="+":
   add= num1+num2
   print(f"result={add}")

elif operator=="-":
   subtraction=num1-num2
   print(f"result={subtraction}")

elif operator=="*":
   multiplication=num1*num2
   print(f"result={multiplication}")

elif operator=="/":
   division=num1/num2
   print(f"result={division}")


elif operator=="%":
   mod=num1%num2
   print(f"result={mod}")



else:
   print("invalid")