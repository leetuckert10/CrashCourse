# Extentions
# Extend an example in this program make it somehow better. I took
#   exercise 6.11 and changed the print loop by looping through the embedded
#   dictionary to print out the results.

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
for city, facts in cities.items():      # outter dictionary
    print(f"{city.title()}:")
    for key, value in facts.items():    # inner dictionary
        print(f"\t{key.title()}: ", end="")
        if key == 'country':
            print(f"{value.title()}")
        else:
            print(f"{value}")
    print("")
