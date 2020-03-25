# Exercise 8-15: Modules
#   This file contains a new version of the Exercise 8-14. The functions used in 8-14.

import car_functions as car

auto = car.make_car('Chevrolett',
    'Denali',
    sun_roof=True,
    heated_sterring_wheel=True,
    color='Black',
    towing_package=True,
    )

car.print_car(auto)