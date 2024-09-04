#validate pancard number
#first 3 character are alphabets
#4th place PCAFHT
#5th place alphabet
#4 digit
#1 alphabaet

from re import fullmatch

pan_card=input("enter pan card number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]\d[A-Z]"

matcher=fullmatch(pattern,pan_card)

print("invalid" if matcher==None else "valid")