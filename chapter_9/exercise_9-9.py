# Exercise 9-9: Battery Upgrade

# Using the example in the text defining a Car class and a Battery class,
# create a new method that upgrades the battery from 75kWh to 100kWh.


class Car:
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoeter = 0
        print("Car constructor...")

    def get_descriptive_name(self):
        """Return a long descriptive name of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Display the miles on the car."""
        print(f"This car has {self.odomoeter} miles on it.")

    def update_odometer(self, miles):
        """Update the odometer insuring that we are not rolling the odometer
        back."""
        if miles < self.odomoeter:
            print("You cannot roll back the odomoeter!")
        else:
            self.odomoeter += miles

    def increment_odomoter(self, miles):
        """Increment the odomoter by the miles argument insuring that the
        mileage passed is not negative."""
        if miles > 0:
            self.odomoeter += miles
        else:
            print("You cannot roll back the odometer with a negative number!")


class ElectricCarBattery:
    """A simple attempt to model an electric car battery."""
    def __init__(self, size=75):
        self.size = size
        print("ElectricCarBattery constructor...")

    def describe_battery(self):
        """Print a message describing the battery."""
        print(f"The battery size is {self.size}-kWh.")

    def upgrade_battery(self, size):
        """Upgrade the battery size insuring that the input we are getting is
        valid."""
        if size != 100:
            print("Upgrade size can only be 100-kWh.")
        elif self.size == 100:
            print("Battery all upgraded to 100-kWh.")
        else:
            print("Battery upgraded to 100-kWh.")

    def show_range(self):
        """Display the mileage range of the car based on the battery size."""
        if self.size == 75:
            range = 260
        elif self.size == 100:
            range = 315

        print(f"Range with {self.size}-kWh battery is {range} miles.")


class ElectricCar(Car, ElectricCarBattery):
    """This class uses multiple inheritance to make a simple attempt to model
    and electric car."""
    def __init__(self, make, model, year, battery_size=75):
        print("ElectricCar constructor...")
        Car.__init__(self, make, model, year)

        # doing it this way calls the Car constructor
#       super().__init__(make, model, year)
        ElectricCarBattery.__init__(self, battery_size)


def test_car():
    """Function for testing the Car class."""
    car = Car("gmc", "denali yukon xl", 2012)
    description = car.get_descriptive_name()
    print(description)

    print("")
    car.read_odometer()

    print("")
    car.update_odometer(85_927)
    car.read_odometer()

    print("")
    print("Try to roll back the odomoeter to 60,999:")
    car.update_odometer(60_999)

    print("")
    print("Increment miles by 75 miles:")
    car.increment_odomoter(75)
    car.read_odometer()

    print("")
    print("Increment miles by a negative number:")
    car.increment_odomoter(-75)


def test_electric_car():
    """Function for testing the ElectricCar class."""
    electric_car = ElectricCar("gmc", "denali yukon xl", 2012, 100)
    electric_car.describe_battery()

    print("")
    print("Try to upgrade to a value not recognized by ElectricCarBattery.")
    electric_car.upgrade_battery(60)

    print("")
    electric_car.show_range()


#test_car()
test_electric_car()
