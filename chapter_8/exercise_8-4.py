# Exercise 8-4: Large Shirts
#   Write a function called make_shirt() that accepts a size and a string for
# the text to be printed on the shirt. Call the function twice: once with
# positional arguments and once with keyword arguments. In this version, we
# define default values for both parameters.


def make_shirt(text='I Love Python', size='large'):
    print(f"Making a {size.title()} T-Shirt with the text '{text}'...")


# use keyword arguments: note the order does not matter
make_shirt(size='medium')   # Override default size with keyword argument
make_shirt()    # use default values for both parameters
make_shirt('I Love YOU', 'extra large') # positional arguments
