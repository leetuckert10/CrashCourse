# Pizza Toppings
#   Write a loop that prompts a user for toppings to add to their pizza and
# print a message for each input value. Continue the loop until 'quit' is
# entered.

toppings = []
flag = True

print("Please enter the toppings you would like for your pizza.")
print("Type 'quit' when you are finished.\n")
while flag:
    topping = input("Topping: ")
    if topping == 'quit':
        flag = False
    else:
        print(f"Adding {topping} to your pizza!\n")
        toppings.append(topping)

print("\nYour pizza has the following toppings:")
print("\t", end="")
for topping in toppings:
    if toppings[-1] == topping:
        print(f"{topping}")
    else:
        print(f"{topping}, ", end="")
