# More Contitional Tests

# equality and inequality with strings
day = 'Monday'
print("day == Monday")
print("Is day == 'Monday'? I predict True.")
print(day.lower() == 'monday')

print("Is day != 'Tuesday'? I predict True.")
print(day.lower() != 'tuesday')

# case matters
print("day == Monday")
print("Is day == 'monday'? I predict False.")
print(day == 'monday')

# test for a certain age group in a list
age_list = [9, 10, 11, 12, 13, 14, 15, 16, 17]
for age in age_list:
    if age < 10:
        print(f"{age} is too young!")
    elif age > 16:
        print(f"{age} is too old!")
    else:
        if age >= 10 and age <= 12:
            print(f"{age} is preferred!")
            if age == 10 or age == 11:
                print(f"We have a {age} year old in the group.")
        else:
            print(f"{age} is acceptable!")

pizza_toppings = ['pepperoni','cheese','italian sausage','green peppers',
    'mushrooms','onion','anchovies']

if 'anchovies' in pizza_toppings:
    print("I hate anchovies!")
if 'pineapple' not in pizza_toppings:
    print("Good, I don't want pineapple on my pizza!")