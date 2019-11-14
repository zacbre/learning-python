#!/usr/bin/env python
from random import seed
from random import randint
from random import shuffle
import time

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%"
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%


def generate_password(length, all_letters):
    print("Generating password with length: %s" % length)
    password = ""
    char_list = list(all_letters)
    for i in range(length):
        shuffle(char_list)
        random_number = randint(0, len(char_list) - 1)
        password = password + char_list[random_number]
    return password


def main():
    password_characters = lowercase + uppercase

    numbers_in_password = input("Do you want numbers in your password? (Y/N): ")
    if numbers_in_password.lower() == "y":
        password_characters = password_characters + numbers

    symbols_in_password = input("Do you want symbols in your password? (Y/N): ")
    if symbols_in_password.lower() == "y":
        password_characters = password_characters + symbols

    length = input("How long would you like your password to be? ")
    seed(time.time())
    password = generate_password(int(length), password_characters)
    print("Here is your randomly generated password: %s" % password)


if __name__ == "__main__":
    main()