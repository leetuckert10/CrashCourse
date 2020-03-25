# Contitional Tests

day = 'Monday'
print("day == Monday")
print("Is day == 'Monday'? I predict True.")
print(day.lower() == 'monday')

print("Is day != 'Tuesday'? I predict True.")
print(day.lower() != 'tuesday')

day = 'Tuesday'
print("day == Tuesday")
print("Is day != 'Tuesday'? I predict False.")
print(day.lower() != 'tuesday')

print("Is day == 'Monday'? I predict False.")
print(day.lower() == 'monday')
