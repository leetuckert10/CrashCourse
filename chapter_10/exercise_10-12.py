# Exercise 10-12: Favorite Number Remembered
#
# Combine the two programs from Exercise 10-11.

import json

filename = 'favorite_number.json'


def prompt_for_number():
    number = input("What is your favorite number? ")
    print(f"I will remember your favorite number is {number} next time!")
    return number


def display_number(number):
    print(f"Your favorite number is {number}!")


def write_number(number):
    with open(filename, 'w') as f:
        json.dump(number, f)


def get_stored_number():
    try:
        with open(filename, 'r') as f:
            number = json.load(f)
    except FileNotFoundError:
        number = prompt_for_number()
        write_number(number)
    else:
        print("in else block................")
        display_number(number)


get_stored_number()
