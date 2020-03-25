# Exercise 8-3: T-Shirt
#   Write a function called make_shirt() that accepts a size and a string for
# the text to be printed on the shirt. Call the function twice: once with
# positional arguments and once with keyword arguments.


def make_shirt(text, size):
    print(f"Making a {size.title()} T-Shirt with the text '{text}'...")


make_shirt('Love You', 'large')     # positional arguments
# use keyword arguments: note the order does not matter
make_shirt(text="Love YOU", size='Medium')
make_shirt(size='extra large', text='Love YOU')