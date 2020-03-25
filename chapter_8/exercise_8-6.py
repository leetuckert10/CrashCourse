# Exercise 8-6: City Names
#   Define a function 'city_country()' which takes two parameters: city
# name, and country. Return a formatted string as in 'New York, USA'.


def city_country(city_name, country):
    name = f"{city_name.title()}, {country.title()}"
    return name


formatted_names = []
formatted_names.append(city_country("new york", "united states"))
formatted_names.append(city_country("tokyo", "japan"))
formatted_names.append(city_country("paris", "france"))

for formatted_name in formatted_names:
    print(f"{formatted_name}")

