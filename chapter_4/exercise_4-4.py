# Create a list of one million numbers and print out the results.
one_million = [value for value in range(1, 1000001)]		# this syntax is called "list comprehension"

for number in one_million:
	print(number)
print('\nfinished')