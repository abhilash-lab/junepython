text="hello hai hello hai hai hello"
words=text.split(" ")
print(words)
word_count={}
for ch in words:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
    print(word_count)
