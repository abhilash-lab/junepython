amount=int(input("enter the amount:"))
annual_intrest=int(input("enter the annual intrest:"))
annual_tenure=int(input("enter the annual tenure:"))

intrest=annual_intrest/12/100

tenure=annual_tenure*12

emi=amount*intrest*(1+intrest)**tenure/((1+intrest)**tenure-1)

total_amount=emi*tenure

total_intrest=total_amount-amount
 
print(f"total intrest={total_intrest}")

print(f"emi={emi}")

print(f"total amount={total_amount}")

