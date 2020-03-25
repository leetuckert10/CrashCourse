# Exercise 10-2: Learning C
#
# Open the text file from the previous example and read the contents into a
# list. Outside the block use the list.replace() method to replace all
# instances of 'Python' with 'C'.
#
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.strip())

