#validate mobile number with country code is mandatory

from re import fullmatch
mobile_number=input("enter mobile number:")
pattern="(91)(-)?[6-9][\d]{9}"
matcher=fullmatch(pattern,mobile_number)
print("invalid" if matcher==None else "valid")