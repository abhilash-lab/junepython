lst="[a, b, c,d]"
n={}
for i in lst:
    if i in n:
        n[i]+=1
        print(n)
    else:
        n[i]=1
        print(i)