#print palindromic above words 
word=["madam","aba","bcb","hello","python"]

for i in range(0,len(word)):

    reverse_str=word[i][::-1]

    if word[i]==reverse_str:

        print(f"{word[i]},is palindrome") 




   