#!/usr/bin/env python
secret_number = 7

def get_input():
    return input("Please input a number: ")

print("Welcome to the guessing game!")
for tries in range(3):
    try:
        guess = int(get_input())
        if guess > secret_number:
            print("The number you selected was too high! Guess again!")
        elif guess < secret_number:
            print("The number you selected was too low! Guess again!")
        else:
            print("Congratulations! That's the correct number!")
            break
    except ValueError:
        print("The value you specified was not a number!")
else:
    print("You failed!")
