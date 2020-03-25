# Restaurant Seating
# Write a program that prompts a user for the number of people in their
#   party at a restaurant. If the number is greater than 8, print a message
#   saying they will have to wait; otherwise, print a message saying their
#   table is ready.

number_in_party = input("How many people are in your party? ")
count = int(number_in_party)

if count > 8:
    print("You are going to have to wait for a table.")
else:
    print("Your table is ready!")