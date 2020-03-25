# Exercise 7-9: No Pastrami
#   Make a list of sandwich order and as you loop through the list, print
# a message stating that the sandwich is being made. Also remove for the
# original list and add each complete sandwich to the completed list. When
# finished, print out the list of fulfilled orders. Use a 'while' loop to
# modify the lists and use a 'for' loop to print out the results.
#   This time, put pastrami in the list three times. When you come across
# print a message that you are out of pastrami and then, use a while loop to
# remove all occurrences of pastrami.
orders = ['hot dog', 'pastrami', 'tuna sandwich', 'pastrami',
          'double cheese burger', 'cheese burger', 'pastrami', 'BLT sandwich']
finished_orders = []

while orders:
    sandwich = orders.pop()
    # out of pastrami
    if sandwich == 'pastrami':
        print("*** I am sorry but we are out of Pastrami! ***")
        while 'pastrami' in orders:
            orders.remove('pastrami')
    else:
        finished_orders.append(sandwich) 
        print(f"Making your {sandwich.title()}...")

print("\nI have made these sandwiches:")
for order in finished_orders:
    print(f"\t{order.title()}")