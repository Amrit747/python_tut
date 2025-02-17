#simple calculator
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operation = input("Enter + for addition, - for subtraction, / for division and * for multiplicaiton")

if operation == "+":
    print("Addition is", num1 + num2)
elif operation == "-":
    print("Subtraction is", num1 - num2)
elif operation == "/":
    print("Division is", num1 / num2)
elif operation == "*":
    print("Multiplication is", num1 * num2)
else:
    print("Invalid..Please only select mentioned symbols for operation")  