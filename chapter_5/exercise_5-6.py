# Stages of Life
# demonstrates use of if, elif, else logic chain

ages = [1, 2, 3, 10, 15, 21, 67]

for age in ages:
    if age < 2:
        print(f"Person at {age} is a baby.")
    elif 2 <= age < 4:
        print(f"Person at {age} is a toddler.")
    elif 4 <= age < 13:
        print(f"Person at {age} is a kid.")
    elif 13 <= age < 20:
        print(f"Person at {age} is a teenager.")
    elif 20 <= age < 65:
        print(f"Person at {age} is a adult.")
    else:
        print(f"Person at {age} is a elder.")
