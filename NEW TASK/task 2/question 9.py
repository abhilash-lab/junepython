#  Write a program to count words in string

word=input("enter the word:")
 
word_count={}
for w in word:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)