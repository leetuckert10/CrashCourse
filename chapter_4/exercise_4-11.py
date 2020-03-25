# My Pizza Toppings

# use splicing to create a list of my favorite toppings
my_toppings = ["mushrooms", "pepperoni", "extra cheese", "green peppers",
    "onion"]

# Make a totally new list with splicing:
#   carlees_toppings = my_toppings does not work!
carlees_toppings = my_toppings[:]	# this will make a totally new list

print(f"My favorite pizza toppings are: {my_toppings}")
print(f"CarLee's favorite pizza toppings are: {carlees_toppings}")

print("\nCarlee doesn't like all that!")
print("I will have to fix that!\n")

# remove items that CarLee does like
carlees_toppings.remove('onion')
carlees_toppings.remove('green peppers')
carlees_toppings.remove('mushrooms')

# now print the lists to prove they are two separate lists
print("My favorite pizza toppings are:")
for topping in my_toppings:
	print(f"{topping}, ", end="")
print('\n')
print("CarLee's favorite pizza toppings are:")
for topping in carlees_toppings:
	print(f"{topping}, ", end="")
print()

print()