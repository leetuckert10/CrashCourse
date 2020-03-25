# Exercise 10-1: Learning Python
#
# Create a file called learning_python.txt and write what you are learning
# going through the crash course. Write a program that opens the file and
# prints what you wrote three times: once by reading in the whole file, once
# by reading the file line by line, once by reading each line of the file
# into a list.

filename = 'learning_python.txt'

# Using 'with' opens the file and automatically closes it when the block
# is finished executing.
with open(filename) as file_object:
    contents = file_object.read()   # reads whole file & stores in contents

print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
