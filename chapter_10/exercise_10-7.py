# Exercise 10-7: Addition Calculator:
#
# Wrap the code from Exercise 10-6 in a while loop so the user can continue
# entering numbers even if they make a mistake and enter text instead of a
# number.

while True:
    first_number = input("Enter the 1st number to be added ['q' to quit]: ")
    if first_number == 'q':
        break
    second_number = input("Ender the 2nd number to be added ['q' to quit]: ")
    if second_number == 'q':
        break

    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print(f"Invalid input: {first_number} + {second_number}.")
    else:
        print(f"The sum of {first_number} + {second_number} is {sum}.")
