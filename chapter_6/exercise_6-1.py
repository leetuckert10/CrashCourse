# Person
# Use a dictionary to store various pieces of information about a person.
person = {
    'first_name': 'Terry',
    'middle_name': 'Lee',
    'last_name': 'Tucker',
    'dob': '03/28/1952',
    'age': 67,
    'job': 'tour bus driver',
}

print(person)

print(f"\nName: {person['first_name']} {person['middle_name']}"
      f" {person['last_name']}")
print(f"DOB: {person['dob']}")
print(f"Age: {person['age']}")
print(f"Job: {person['job']}")
