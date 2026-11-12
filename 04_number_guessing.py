"""Project 4: Guess the secret number."""

import random

secret_number = random.randint(1, 10)
guess = 0

print("I am thinking of a number from 1 to 10.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low. Try again!")
    elif guess > secret_number:
        print("Too high. Try again!")
    else:
        print("Correct! You guessed the number.")
