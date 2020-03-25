# Rivers
# Make a dictionary containing three major rivers and the country each river
# runs through.
major_rivers = {
    'sepik': 'new guinea',
    'mississippi': 'united states',
    'volga': 'russia',
    'zambezi': 'africa',
    'mekong': 'cambodia',
    'ganges': 'india',
    'danube': 'europe',
    'yangtze': 'china',
    'nile': 'egypt',
    'amazon': 'brazil',
}

# print a sentence regarding the river and country
for river, country in major_rivers.items():
    if country.lower() == 'united states':
        print(f"The {river.title()} river runs through the {country.title()}.")       
    else:
        print(f"The {river.title()} river runs through {country.title()}.")

# print just the river names
print("\nThe ten major rivers of the world are:")
for river in major_rivers:
    print(f"\t{river.title()}")

# print just the names of the countries through which these rivers flow
print("\n These major rivers flow through these countries:")
for country in major_rivers.values():
    print(f"\t{country.title()}")

