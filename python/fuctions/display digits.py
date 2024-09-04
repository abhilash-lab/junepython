word= "i have 2 bike and 1 car"

#print alphabets

for ch in word:

    if ch.isalpha():
        print(ch,end=" , ")
#print digits

for dig in word:
    if dig.isdigit():
        print(dig,end=" , ")

#print alpabhabets and digit

for chdig in word:
    if chdig.isalnum():
        print(chdig,end=" , ")