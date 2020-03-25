# Multiples of 10 - expanded to be multiples of 2 - 10.
# Promt the user for a number and then report where it is a multiple of 10.

input_string = input("Please enter a number: ")
number = int(input_string);

if number % 10 == 0:
    print(f"{number} is a multiple of 10!")
elif number % 9 == 0:
    print(f"{number} is a multiple of 9!")
elif number % 8 == 0:
    print(f"{number} is a multiple of 8!")
elif number % 7 == 0:
    print(f"{number} is a multiple of 7!")
elif number % 6 == 0:
    print(f"{number} is a multiple of 6!")
elif number % 5 == 0:
    print(f"{number} is a multiple of 5!")
elif number % 4 == 0:
    print(f"{number} is a multiple of 4!")
elif number % 3 == 0:
    print(f"{number} is a multiple of 3!")
elif number % 2 == 0:
    print(f"{number} is a multiple of 2!")
else:
    print(f"{number} is NOT a multiple of the range 2 to 10!")
