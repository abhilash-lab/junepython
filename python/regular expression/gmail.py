#validate gmail

from re import fullmatch

mail=input("eneter mail:")

pattern="\\w[\\w\\._]*@gmail.com"

matcher=fullmatch(pattern,mail)

print("invalid" if matcher==None else "valid")