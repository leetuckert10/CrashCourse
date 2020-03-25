# Exercise 10-11-1: Favorite Number (writes the number)
#
# Write a program that prompts for the user's favorite number. Use json.dump()
# to store this number in a file. Write a separate program that reads in
# this value and prints the message, "I know your favorite number! It is ___".

import json

favorite_number = input("What is your favorite number? ")
filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
