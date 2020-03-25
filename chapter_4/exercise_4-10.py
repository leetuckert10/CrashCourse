# Slices
# Use list splicing to print various parts of a list.
cubes = [value**3 for value in range(1, 11)]	# list comprehension
print("The entire list:")
for value in cubes:
	# check out this syntax for suppressing a new line.
	print(value, " ", end="")
print('\n')

# display first 3 items
print(f"The first three items are: {cubes[:3]}")

# display items from the middle of the list
print(f"Three items beginning at index 3 are: {cubes[3:6]}")

# display last three items in list
print(f"The last three items are: {cubes[-3:]}")
print()