numbers = [151, 153, 154, 370, 371, 372, 373, 16341, 1635]

for number in numbers:
    original = number
    sum = 0
    digit_count = len(str(number))
    
    while number > 0:
        digit = number % 10
        sum += digit ** digit_count
        number //= 10
    
    if sum == original:
        print(original)
 