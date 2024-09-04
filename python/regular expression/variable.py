from re import fullmatch
variable_name=input("enter name:")
pattern="[k-m][369][a-zA-Z@]*"
matcher=fullmatch(pattern,variable_name)
print("invalid" if matcher==None else "valid")
