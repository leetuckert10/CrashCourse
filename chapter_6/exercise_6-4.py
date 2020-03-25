# Glossary 2
# Revamp the glossary code in exercise 6-3 and use a for loop to print out the
# results. Then, add five more words to the glossary and run the program 
# again.
glossary = {
    'list': 'a data structure that stores a list of items of any data type',
    'dictionary': 'a data structure that stores data using a set of key/value pairs',
    'print': 'a function use for display information',
    'if': 'a logical construct using if, elif, and else to implement logical branches in the program',
    'del': 'a function used for deleting an item from a list or an item from a dictionary',
    'set': 'a method used to return a unique set of values',
    'keys': 'a mehtod for a dictionary construct which returns a list of all the keys',
    'sorted': 'a funtion which returns a sorted list of values',
    'values': 'a method for a dictionary construct which returns a list of the values',
    'items': 'a method for a dictionary construct which returns a list of the key/value pairs',
}

# Print the words and their definitions with a blank line in between each.
for word, definition in glossary.items():
    print(f"{word}:")
    print(f"\t{definition}\n")

