# Exercise 10-5: Programming Poll
#
# Write a while loop that asks people why they like programming. Each time
# someone enters a reason, add their reason to a file that stores all the
# responses.

from datetime import datetime as dt

flag = True
filename = "programming_poll.txt"

with open(filename, 'a') as file_object:
    print("This is a poll about why people like programming.")
    print("Follow the prompts and enter your answers.")
    while flag:
        name = input("Please enter your name ['q' to quit]: ")
        if name == 'q':
            flag = False
        else:
            print(f"Welcome {name}! Thank you for taking my poll!")
            reason = input("Why do like being a programmer:\n")
            file_object.write(f"{name} polled at {dt.now()}\n")
            file_object.write(f"{reason}\n\n")

with open(filename, 'r') as file_object:
    contents = file_object.read()

print(contents.strip())

