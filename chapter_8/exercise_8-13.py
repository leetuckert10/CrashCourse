# Exercise 8-13: User Profile
# Define a function that creates a list of key-value pairs for all the
# arbitrary arguments. The syntax **user_info tell Python to create a
# dictionary out of the arbitrary parameters.


def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


def show_user_profile(user_profile):
    """ Print out key/value pairs in the user profile dictionary."""
    for key, value in user_profile.items():
        print(f"{key}: {value}")


user_profile = build_profile('terry', 'tucker', location='sparta',
                             field='software developer')
show_user_profile(user_profile)