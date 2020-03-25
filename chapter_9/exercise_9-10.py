# Exercise 9-10: Imported Restaurant

from restaurant import IceCreamStand

flavors = ["chocolate","vanilla","strawberry"]
ics = IceCreamStand("Terry's Ice Cream Shop", "Ice Cream", flavors)

ics.show_flavors()

print("\nAdding new flavors!")
ics.add_flavor("butter pecan")
ics.add_flavor("cookie dough")
ics.add_flavor("carmal")
ics.show_flavors()

print("\nOops! Out of Butter Pecan because Terry ate it all!\n")
ics.remove_flavor("butter pecan")
ics.show_flavors()

ics.set_number_served(238_449)
# Showing that we have this attribute from Restaurant.
print(f"We have served {ics.number_served} customers!")
