#write a program to calculate emi

#loan amount
#intrest
#Loan Tenure

amount=5000000
intrest=9/12/100
tenure=20*12


emi=amount*intrest*(1+intrest)**tenure/((1+intrest)**tenure-1)

total_amount=emi*tenure

total_intrest=total_amount-amount
 
print(f"total intrest={total_intrest}")

print(f"emi={emi}")

print(f"total amount={total_amount}")
