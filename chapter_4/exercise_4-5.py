# Summing a million numbers...
# using functions min(), max(), and sum()
one_million = []
for value in range(1, 1000001):
	one_million.append(value)

print(f"Mininum value is {min(one_million)}")
print(f"Maximum value is {max(one_million)}")
print(f"The sum of adding one million numbers together is {sum(one_million)}!")
print("\nfinished")