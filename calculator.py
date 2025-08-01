#!/usr/bin/env python3

# Basic Calculator Program

# Ask for the first number
num1 = float(input("Enter the first number: "))

# Ask for the operator
operator = input("Enter an operator (+, -, *, /): ")

# Ask for the second number
num2 = float(input("Enter the second number: "))

# Do the math
if operator == '+':
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operator == '-':
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operator == '*':
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("You can't divide by zero!")
else:
    print("Invalid operator.")