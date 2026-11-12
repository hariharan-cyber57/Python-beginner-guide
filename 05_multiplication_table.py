"""Project 5: Print a multiplication table."""

number = int(input("Enter a number: "))

print("Multiplication table for", number)

for multiplier in range(1, 11):
    answer = number * multiplier
    print(number, "x", multiplier, "=", answer)
