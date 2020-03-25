# Cities
# Make dictionary called cities with the names of three cities as the keys.
# Create a dictionary of information about each city. This is a dictionary
#   withing a dictionary.

cities = {
    'london': {
        'country': "united kingdom",
        'population': "7.1 million",
        'fact': "London is the capital city of England and the United Kingdom.",
    },
    'paris': {
        'country': "france",
        'population': "2.34 million",
        'fact': "Paris is the home of the Eiffel Tower.",
    },
    'tokyo': {
        'country': "japan",
        'population': "36 million",
        'fact': "Tokyo is the largest metropolitan area in the world!",
    },
}

# Loop through the day printing out all the information you have.
for city, facts in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {facts['country'].title()}")
    print(f"\tPopulation: {facts['population']}")
    print(f"\tFun fact: {facts['fact']}\n")
