# Exercise 7-8: Deli
#   Make a list of sandwich order and as you loop through the list, print
# a message stating that the sandwich is being made. Also remove for the
# original list and add each complete sandwich to the completed list. When
# finished, print out the list of fulfilled orders. Use a 'while' loop to
# modify the lists and use a 'for' loop to print out the results.
orders = ['hot dog', 'tuna sandwich', 'double cheese burger', 'cheese '
          'burger', 'BLT sandwich']
finished_orders = []

while orders:
    finished_orders.append(orders.pop()) 
    print(f"Making your {finished_orders[-1].title()}...")

print("\nI have made these sandwiches:")
for order in finished_orders:
    print(f"\t{order.title()}")