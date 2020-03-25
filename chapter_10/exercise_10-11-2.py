# Exercise 10-11-2: Favorite Number (reads the number)
#
# Write a program that prompts for the user's favorite number. Use json.dump()
# to store this number in a file. Write a separate program that reads in this
# value and prints the message, "I know your favorite number! It is ___".

import json

filename = 'favorite_number.json'

with open(filename, 'r') as f:
    favorite_number = json.load(f)

print(f"I know what your favorite number is! It is {favorite_number}!")