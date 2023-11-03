H = int(input())
C = int(input())
E = int(input())
M = int(input())
S = int(input())
sum = H+C+E+M+S
p = sum/500*100
if p>=90:
    print("A Grade")
elif p>=80:
    print("B Grade")
elif p>=70:
    print("C Grade")
elif p>=60:
    print("D Grade")
else:
    print("E Grade")