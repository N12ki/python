q=int(input())
c=int(input())
t=q*c
if t>=1000:
    d = t*10/100
    e=d-t
    print(e)
else:
    print(t)