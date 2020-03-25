# Exercise 9-1: Restaurant
#   Make a class called Restaurant that has two attributes: restaurant name
#   and restaurant cuisine. Define two methods: one that describes the
#   restaurant and another that opens the restaurant.

import restaurant as rest

restaurant = rest.Restaurant("Billy Bob's Grill", "American")

print("")
restaurant.describe_restaurant()
restaurant.open_restaurant()