#count the vovels

text="psych"

vovels="A E I O U"
consonants="b c d f g j k l m n p q s t v x z"

text=text.upper()

vovel_count=0
ch_count=0

for ch in text:
    if vovels.count(ch)!=0:
        vovel_count+=1
    else:
        ch_count+=1
print(vovel_count)
print(ch_count)