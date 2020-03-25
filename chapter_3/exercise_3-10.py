fruits = ['oranges', 'pears', 'apples', 'peaches', 'strawberries', 'blueberries']
print(f"My original list of fruits: {fruits}")

# replace last one using -1 subscript that will always address the last entry
fruits[-1] = 'cranberries'
print(f"\nMy updated list of fruits: {fruits}")

# print something from the list using an index
print(f"I really like {fruits[4]}!")
print(f"I REALLY like {fruits[4].title()}!!!")

# using the append method to add something to the end of the list
fruits.append('cranberries')
print(f"I appended {fruits[-1]}.")
print(f"My current list of fruits: {fruits}")

# use del to remove an item by index; this call can be used with or without parens
del(fruits[1])
print(f"\nI removed pears from the list using the del function: {fruits}.")

# use the insert method to add one I forgot
fruits.insert(1, 'bananas')
print(f"\nI inserted bananas at position 2: {fruits}.")

# pop off cranberries because it is in the list twice
pop_off_fruit = fruits.pop()
print(f"\nI 'popped off' {pop_off_fruit} from the end of the list: {fruits}.")

# remove a list item by item value; only removes the first occurrance of matching item
fruits.append('blueberries')
print(f"\nI inserted blueberries at the end of the list: {fruits}.")
fruits.remove('cranberries')
print(f"I removed cranberries from the list with the remove method: {fruits}.")

# determine length of completed list
fruit_len = len(fruits)
print(f"My final list now contains {fruit_len} entries.")

# time to display my fruit list in a sorted manner, but NOT actually manipulating the list
# this is a function, NOT a method
print(f"\nMy fruit list displayed as a sorted list: {sorted(fruits)}")

# time to display my fruit list in a reverse sorted manner
print(f"\nMy fruit list displayed as a reverse sorted list: {sorted(fruits, reverse=True)}")

# time to permanently sort the list saving a copy of the original; however,
# this does not work! 
original_fruits = fruits
fruits.sort()
print(f"\nPermanently sorted list: {fruits}")
fruits.sort(reverse=True)
print(f"Permanently reverse sorted list: {fruits}")

# reverse it with the list.reverse() method
fruits.reverse()
print(f"Permanently reverse sorted list with the reverse() method: {fruits}\n")

# When you see the output, you will see that the copy of the fruits list
# is now sorted!!! Very interesting...
print(f"The original_fruits variable with {len(original_fruits)} elements is now sorted as well:\n {original_fruits}.")
