#   Make a class called Restaurant that has two attributes: restaurant name and restaurant cuisine. Define two methods: one that describes the restaurant and another that opens the restaurant.

# In Exercise 9-4 add a new attribute called number_served with a default
# value of zero. Add a method called set_number_served(num) that sets the
# using the argument passed. Add a method called increment_number_served(inc)
# that increments the value accordingly.


class Restaurant:
    """ A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine):
        """Iniitialize restaurant name and cuisine."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant with a simple headline."""
        print(f"This is {self.name} featuring {self.cuisine} cuisine.")
        if (self.number_served > 0):
            print(f"We have served {self.number_served} customers!")

    def open_restaurant(self):
        """Print a line that states the restaurant is open for business."""
        print(f"{self.name} is now open for business!")

    def set_number_served(self, num):
        """This method sets the number_served attribute ensuring that the
        number passed is not a negative number."""
        if num < 0:
            print(f"{num}: Invalid input. Cannot be a negative number.")
        else:
            self.number_served = num

    def increment_number_served(self, num):
        """This method increments the number_served attribute ensuring that
        the number passed is not a negative number."""
        if num < 0:
            print(f"{num}: Invalid input. Cannot be a negative number.")
        else:
            self.number_served += num


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

