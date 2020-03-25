# This file contains functions for Exercise 8-15. This is a module.


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
