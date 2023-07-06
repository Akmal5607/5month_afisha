

while True:
а = int(input("Enter first number: "))
b = (input("Enter first opiration: "))
c = int(input("Enter second number: "))

if b == "+":
    print(a + c)

elif b == "-":
    print(a - c)


elif b == "*":
    print(a * c)

elif b == "/" and c == 0:
    print("на ноль делить нельзя!!!")

elif b == "/":
    print(a / c)

else:
    print("Error!!")