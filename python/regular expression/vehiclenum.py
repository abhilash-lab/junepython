#kerala vehicle register number
#two digit
#starts with kl 
#alphabets(one or two)
#4 digits

from re import fullmatch
variable_name=input("eneter vehicle number:")
pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[\d]{4}" #? is for (-) will be optional in one time
matcher=fullmatch(pattern,variable_name)
print("invalid" if matcher==None else "valid")