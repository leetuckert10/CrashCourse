# Exercise 8-12: Sandwiches
#   Write a function that accepts an arbitrary number of arguments from which
# it builds a sandwich.

# The parameter *fixings tells Python to put the list of arguments in a tuple.
# Remember, a tuple is immutable.


def build_sandwich(name, *fixings):
    print(f"Making a sandwich for {name.title()} with:")

    for stuff in fixings:
        print(f"\t-{stuff}")

build_sandwich('john', 'rye bread', 'mayonnaize', 'gray poupon', 'lettuce',
               'tomato', 'cheddar cheese', 'bacon')
build_sandwich('carlee', 'no bread', 'hamburger patty', 'american cheese')
build_sandwich("terry", "hamburger bun", "mayonnaise", "lettuce", "tomato",
               "onion", "hamburger patty", "cheddar cheese")
