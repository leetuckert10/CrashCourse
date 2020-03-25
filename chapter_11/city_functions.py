# Exercise 11-1: City, Country
#
# Write a function that accepts two parameters: a city name and a country
# name. The function should return a single string of the form City, Country.
# Store the function in a module called city_functions.py

# Exercise 11-2: Population
#
# First, modify the function so that population is a required 3 parameter.
# Run the test class again. I should fail. Now, modify the function such that
# the population parameter is optional.


def get_formatted_city_country(city, country, population=0):
    if population > 0:
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"

    return formatted_name.title()
