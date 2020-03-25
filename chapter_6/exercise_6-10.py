# Favorite Numbers Modified
# Store the favorite number of five people in a dictionary using their
# name as the key. In this version we have added a list of numbers.

favorite_nums = {
    'terry': [18, 21, 41, 60],
    'carLee': [12, 16, 21, 25],
    'linda': [16, 12, 44],
    'rebekah': [21],
    'nathan': [42, 25, 30, 35],
}

for name, numbers in favorite_nums.items():
    if numbers:
        print(f"{name.title()}'s favorite numbers are:")
        print("\t", end="")     # print tab with no newline 
        for number in numbers:
            # doing trailing comma control...
            if number == numbers[-1]:   # [-1] returns last item in list
                print(f"{number}", end="")
            else:
                print(f"{number}, ", end="")
    else:
        print(f"{name} has no favorite numbers defined.")

    print("\n")
