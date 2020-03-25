# Exercise 10-10: Common Words
#
# Write a program that reads a large file and determines how many times the
# word 'the' appears in the text. This will be an approximation because it
# will also count words such as 'then' and 'there'. Try counting 'the ',
# with a space in the string, and see how much lower your count is.

file = '../resources/chapter_10/little_women.txt'
word = 'the'
count = 0

try:
    with open(file) as f:
        for line in f:
            line_count = line.count(word.lower())

            if line_count > 0:
                print(f"{line}")
                count += line_count
                line_count = 0
        print(f"There are {count} occurances of the word '{word}' in {file}.")
except FileNotFoundError:
    print(f"The file {file} does not exist in the current file path!")