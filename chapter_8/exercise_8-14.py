# Exercise 8-13: Cars
#   Define a function that creates a list of key-value pairs for all the
# arbitrary arguments. The syntax **user_info tell Python to create a
# dictionary out of the arbitrary parameters.


def make_car(manufacturer, model, **car):
    """ Make a car using a couple positional parameters and and arbitrary
    number of arguments as car. """
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car


def print_car(car):
    """ Print out key/value pairs in the user profile dictionary."""
    for key, value in car.items():
        print(f"{key}: {value}")


car = make_car('Chevrolett',
    'Denali',
    sun_roof=True,
    heated_sterring_wheel=True,
    color='Black',
    towing_package=True,
    )

print_car(car)