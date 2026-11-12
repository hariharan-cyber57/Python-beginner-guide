"""Project 2: A simple calculator for two numbers."""

first_number = float(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
    print("Result:", result)
elif operator == "-":
    result = first_number - second_number
    print("Result:", result)
elif operator == "*":
    result = first_number * second_number
    print("Result:", result)
elif operator == "/":
    if second_number == 0:
        print("Error: You cannot divide by zero.")
    else:
        result = first_number / second_number
        print("Result:", result)
else:
    print("Invalid operator. Please choose +, -, * or /.")
