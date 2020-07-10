num1 = float(input("Number: "))
opt = input("Operator: ")
num2 = float(input("Number: "))

if opt == "+":
    print(num1 + num2)
elif opt == "-":
    print(num1 - num2)
elif opt == "*":
    print(num1 * num2)
elif opt == "/":
    print(num1 / num2)
else:
    print("Error")