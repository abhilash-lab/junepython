#check pangrams or not

text="Two driven jocks help fax my big qui."

text=text.lower()

alphabets="abcdefghijklmnopqrstuvwxyz"


is_pangram=True
for ch in alphabets:
    if text.count(ch)==0:
        is_pangram=False
        break
print(is_pangram)