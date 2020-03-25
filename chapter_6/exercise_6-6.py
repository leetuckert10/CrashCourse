# People
# Create 3 dictionaries of people and store them in a list called people.
# Loop through the list accessing the dictionary items and print out the
# information.
terry = {
    'first_name': 'Terry',
    'middle_name': 'Lee',
    'last_name': 'Tucker',
    'dob': '03/28/1952',
    'age': 67,
    'job': 'tour bus driver',
}
carlee = {
    'first_name': 'CarLee',
    'middle_name': 'Nicole',
    'last_name': 'Billings',
    'dob': '04/25/2007',
    'age': 12,
    'job': 'student',
}
caylee = {
    'first_name': 'Caylee',
    'middle_name': 'Marie',
    'last_name': 'Billings',
    'dob': '08/18/2006',
    'age': 13,
    'job': 'student',
}

people = [terry, carlee, caylee]

for person in people:
    print(f"{person['first_name']} {person['middle_name']} {person['last_name']}:")
    print(f"\tDate of Birth: {person['dob']}")
    print(f"\tAge: {person['age']}")
    print(f"\tJob: {person['job'].title()}\n")

#print(f"\nName: {person['first_name']} {person['middle_name']} {person['last_name']}")
#print(f"DOB: {person['dob']}")
#print(f"Age: {person['age']}")
#print(f"Job: {person['job']}")
