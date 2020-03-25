# Exercise 10-3: Guest
#
# Write a program that prompts a user for their name. When they respond,
# write their name to a file called guest.txt.
#

flag = True
filename = "guests.txt"

with open(filename, 'a') as file_object:
    print("Enter each users name. Type 'q' to quit.")
    while flag:
        name = input("Please enter your name: ")
        if name == 'q':
            flag = False
        else:
            file_object.write(f"{name}\n")

with open(filename, 'r') as file_object:
    contents = file_object.read()

print(contents.strip())
