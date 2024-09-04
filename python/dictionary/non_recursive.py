# print non recursive character

text="ababcde"

word_count={}

for ch in text:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
for k , v in word_count.items():
    if v==1:
        print(k)
