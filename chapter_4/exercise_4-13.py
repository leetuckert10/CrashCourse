# Buffet
# This is a tuple similar to a list but cannot be changed.
buffet_foods = ('fried chicken', 'maccroni and cheese', 'turnip greens',
                'mashed potatoes', 'slaw')
print("The Menu")
for food in buffet_foods:
    print(f"{food.title()}, ", end="")
print()

# Cannot do this!
# buffet_foods.remove('slaw')

# Oops, gotta change the menu. You can only do that by redfining the tuple.
print("\nThe New Menu")
buffet_foods = ('fried chicken', 'maccroni and cheese', 'green beans',
                'mashed potatoes', 'slaw')
for food in buffet_foods:
    print(f"{food.title()}, ", end="")

print()
