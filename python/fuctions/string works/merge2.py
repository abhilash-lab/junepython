#merge string

word1="pqrst"
word2="abc"
merge_string=""
smallest_word=word1 if len(word1)<len(word2) else word2
for i in range(0,len(smallest_word)):
    merge_string=merge_string+word1[i]+word2[i]
    if len(word1)>len(word2):
        balance=word1[len(word2):]
    else:
        balance=word2[len(word1):]
merge_string=merge_string+balance
print(merge_string)
 

    
    


