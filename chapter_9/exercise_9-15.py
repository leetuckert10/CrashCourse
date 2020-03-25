# Exercise 9-15: Lottery Analysis
#
# Using the code from the previous example, define your lottery ticket and
# run a loop until you get a match. Keep count of the number of attempts and
# display that at the end.
from random import choice

lottery_numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                   'c', 'd')

my_ticket = "a934"
ticket = ""
count = 0
while my_ticket != ticket:
    ticket = ""
    for x in range(1, 5):
        ticket += choice(lottery_numbers)
    count += 1

print(f"The odds of winning with just 4 numbers out of 15 is: {count}!")