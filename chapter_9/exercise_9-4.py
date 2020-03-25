# Exercise 9-4: Number Served
# This version of Restaurant from 9-1 explorers a new attribute added to the
# the Restaurant class.

import restaurant as r

restaurant = r.Restaurant("Billy Bob's Grill", "American")

restaurant.set_number_served(28_952)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Set number_served to a new value and print again.
restaurant.set_number_served(32_995)
print(f"\nNew value for number served: {restaurant.number_served}.")

restaurant.increment_number_served(378)
print(f"\nAfter serving 378 customers toady our new value for number served:"
      f" {restaurant.number_served}.")
