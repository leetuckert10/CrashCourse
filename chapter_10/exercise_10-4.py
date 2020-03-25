# Exercise 10-4: Guest Book
# Write a while loop that prompts users for their name. When they enter their
# name print a personalized greeting to the screen then write a line to a
# file called guest_book.txt that records their visit.

from datetime import datetime as dt

flag = True
filename = "guest_book.txt"

with open(filename, 'a') as file_object:
    print("Let each guest enter their name. Type 'q' to quit.")
    while flag:
        name = input("Please enter your name: ")
        if name == 'q':
            flag = False
        else:
            print(f"Welcome {name}! Thank you for stopping by!")
            file_object.write(f"{name} registered at {dt.now()}\n")

with open(filename, 'r') as file_object:
    contents = file_object.read()

print(contents.strip())
