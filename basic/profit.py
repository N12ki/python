sp = int(input())
cp = int(input())
if sp==cp:
    print("no profit no loss")
elif sp>cp:
    p = sp-cp
    print(p)
else:
    l=cp-sp
    print(l)


