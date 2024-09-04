# find the recursive word
text = "abcabdd"

new_text = {}

for ch in text:
    if ch in new_text:
        print(ch)
        break
    else:
        new_text[ch] = 1

