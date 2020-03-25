# Just more practice with for loops and printing.
my_foods =['pinto beans', 'corn bread', 'cheese burger', 'bacon', 'eggs']
carlees_foods = my_foods[-3:]	# CarLee only likes the last three in my list

# print results using for loops
print(f"My favorite foods are:")
for food in my_foods:
	print(f"{food}, ", end="")
print('\n')

print(f"CarLee's favorite foods from my list are:")
for food in carlees_foods:
	print(f"{food}, ", end="")
print('\n')