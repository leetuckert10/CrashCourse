# Cube Comprehension
# Make a list of the first 10 cubes using list comprehension.

cubes = [value**3 for value in range(1, 11)]	# list comprehension
for value in cubes:
	# check out this syntax for suppressing a new line.
	print(value, " ", end="")
print("\nfinished")