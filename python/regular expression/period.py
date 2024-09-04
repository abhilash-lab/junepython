# ends with "at" returns that word and print

from re import findall

text="the fat cat run faster to catch the rat"

pattern=".at"

matcher=findall(pattern,text)

print(matcher)

