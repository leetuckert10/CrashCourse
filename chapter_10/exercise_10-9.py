# Exercise 10-9: Silent Cats and Dogs
#
# Modify the except block in Exercise 10-8 to fail silently if either file is
# missing.

cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

try:
    with open(cats_file) as cats:
        contents = cats.read()
except FileNotFoundError:
    pass
else:
    print(contents)

try:
    with open(dogs_file) as dogs:
        contents = dogs.read()
except FileNotFoundError:
    pass
else:
    print(contents)