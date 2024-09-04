#logest palindromic substring from given string

text="racecar"

length=len(text) 

longest_palindrome=""

for i in range(0,length):

    left=i 

    right=i
    while (left>=0 and right<length and text[left]==text[right] ) :


        current_palindrome=text[left:right+1]


        if len(current_palindrome)>len(longest_palindrome):

            longest_palindrome=current_palindrome

        left=left-1

        right=right+1

print(longest_palindrome)


