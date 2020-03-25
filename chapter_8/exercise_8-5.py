# Exercise 9-5: Cities
#   Define a function with two parameters for the name of the city and the
# country in which it is located. Define with a default value for country.
# Call it 3 time one of which uses the default value for country.


def describe_city(name, country='USA'):
    print(f"{name} is located in {country}...")


describe_city("New York")
describe_city("Tokyo", "Japan")
describe_city("Paris", "France")