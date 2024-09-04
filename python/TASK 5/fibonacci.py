#fibonacci or not

def is_fibonacci(num):
    current=1
    previous=0
    next=current+previous
    while(next<=num):
        next=current+previous
        previous=current
        current=next
        if num==next:
            return True
    return False
print(is_fibonacci(169))