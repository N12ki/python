first = input("enter first number : ")
opreator = input("enter opretor(+,-,*,/,%) : ")
second = input("enter second number : ")

first = int(first)
second = int(second)

if opreator == "+":
    print(first + second)
elif opreator == "-":
    print(first - second)
elif opreator == "/":
    print(first / second)
elif opreator == "*":
    print(first * second)
elif opreator == "%":
    print(first % second)
else:
    print("Invalid Operation")