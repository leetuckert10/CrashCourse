# Exercise 10-8: Cats and Dogs
#
# Make two files, cats.txt and dogs.txt. Store at least three names of cats
# in the first file and three names of dogs in the second. Write a program
# that tries to read these files and print the contents. Wrap the code in a
# try-except block to catch the FileNotFound error and print a friendly
# message if the file is missing.

cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

try:
    with open(cats_file) as cats:
        contents = cats.read()
except FileNotFoundError:
    print(f"File {cats_file} does not exist in the current file path.")
else:
    print(contents)

try:
    with open(dogs_file) as dogs:
        contents = dogs.read()
except FileNotFoundError:
    print(f"File {dogs_file} does not exist in the current file path.")
else:
    print(contents)