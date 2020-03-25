# Exercise 10-6: Addition:
#
# Write a program that prompts for two numbers. Add them together and print
# the result. Catch the ValueError if either input value is not a number and
# print a friendly error message. Test your program by entering two numbers
# and then by entering some text instead of a number.

first_number = input("Enter the first number to be added: ")
second_number = input("Ender the second number to be added: ")

try:
    sum = int(first_number) + int(second_number)
except ValueError:
    print(f"Invalid input: {first_number} + {second_number}.")
else:
    print(f"The sum of {first_number} + {second_number} is {sum}.")
