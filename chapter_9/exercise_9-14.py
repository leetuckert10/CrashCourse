# Exercise 9:14: Lottery
#
# Create a list or tuple contain 10 numbers and 5 letters. Using choice(),
# randomly select 4 values to generate a lottery ticket.

from random import choice

lottery_numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                   'c', 'd')

ticket = ""
for x in range(1, 7):
    ticket += choice(lottery_numbers)

print(f"The winning number is: {ticket.upper()}...")