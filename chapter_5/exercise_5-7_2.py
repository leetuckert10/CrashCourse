# This is my own junk using lists and if, else statements
available_toppings = ['cheese', 'extra cheese', 'pepperoni', 'pineapple',
                      'italian sausage', 'green peppers', 'onion', 'jalapeno',
                      'peppers', 'anchovies', 'mushrooms']
# requested_toppings = []
requested_toppings = ['extra cheese', 'pepperoni', 'mushrooms',
                      'jalapeno peppers', 'french fries']

if requested_toppings:
    for request in requested_toppings:
        if request in available_toppings:
            print(f"Adding {request} to pizza...")
        else:
            print(f"Sorry, we don't have {request} available now...")
else:
    print("Are you sure you want just a plain pizza?")
