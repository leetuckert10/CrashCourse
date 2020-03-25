# Pets
# Make several dictionaries where each dictionary stores information about
# a pet. Then store the disctionaries in a list and print out the data.
pet_1 = {
    'name': 'fido',
    'kind': 'dog',
    'owner_name': 'carLee',
    'age': 8,
}
pet_2 = {
    'name': 'Sheba',
    'kind': 'cat',
    'owner_name': 'linda',
    'age': 20,
}
pet_3 = {
    'name': 'piggy woo',
    'kind': 'pig',
    'owner_name': 'linda',
    'age': 3,
}

# create a list of dictionaries
pets = [pet_1, pet_2, pet_3]

# print out the results
print("Pet Info:")
for pet in pets:
    print(f"{pet['name'].title()}:")
    print(f"\tKind: {pet['kind'].title()}")
    print(f"\tOwner: {pet['owner_name'].title()}")
    print(f"\tAge: {pet['age']}\n")