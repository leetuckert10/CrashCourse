# Exercise 10-13: Verify User
#
# This is a version of remember_my.py which, if a user name is found,
# will prompt the current user to determine if this is the right user name.
# If it is not the right user name then overwrite the file with a new user name.

import json

filename = 'username.json'


def prompt_for_username():
    """This function prompts the user for a user name."""
    username = input("Please enter your user name: ")
    print(f"{username}, I will remember you next time!")
    return username


def greet_user(username):
    """This function greets a user by name."""
    print(f"Greetings {username}! Thanks for stopping by!")


def write_username(username):
    """This function writes a user's favorite number to a file."""
    with open(filename, 'w') as f:
        json.dump(username, f)


def verify_user(username):
    """This function verifies whether the current user name is the same as
    the one that is stored in the file."""
    answer = input(f"Is {username} your user name? [y/n]: ")
    if answer == 'n':
        new_username = prompt_for_username()
        write_username(new_username)
        username = new_username
    return username


def get_stored_username():
    """This function attempts to read a favorite number from the file. If the
    file does not exist, prompt_for_username() is called followed by
    write_username()."""
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        username = prompt_for_username()
        write_username(username)
    else:
        greet_user(verify_user(username))


get_stored_username()
