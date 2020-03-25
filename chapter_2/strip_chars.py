# This program demonstrates several aspects of striping spaces from strings.
Oldest_daughter = "hannah "
Oldest_son = ' nathan'
youngest_daughter = ' rebekah '
carlee = "    carLee  "

print("My children are:")
print(f"\t{Oldest_daughter.rstrip().title()}")
print(f"\t{Oldest_son.lstrip().title()}")
print(f"\t{youngest_daughter.strip().title()}")
print(f"\t{carlee.strip().title()}")
