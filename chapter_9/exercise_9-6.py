# Exercise 9-6: Ice Cream Stand

# Write a class that inherits the Restaurant class. Add and an attribute 
# called flavors that stores a list of ice cream flavors. Add a method that
# displays the flavors. Call the class IceCreamStand.

from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors=None):
        super().__init__(name, cuisine)
        self.flavors = flavors

    def add_flavor(self, flavor):
        """This method adds an ice cream flavor to the the flavors list."""
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        """This mehtod removes a flavor from the list of ice cream flavors."""
        self.flavors.remove(flavor)

    def show_flavors(self):
        """This method displays all the flavors available at the ice cream
        stand."""
        print("Available ice cream flavors are: ", end="")
        for flavor in self.flavors:
            if flavor == self.flavors[-1]:
                print(f"{flavor.title()}.", end="")
            else:
                print(f"{flavor.title()}, ", end="")
        print("")

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
