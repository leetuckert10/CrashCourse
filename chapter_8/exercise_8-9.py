# Exercise 8-9: Messages
#   Make a list of several short messages and pass the list to a function
# that prints each message.


def show_messages(messages):
    for message in messages:
        print(f"{message}")


unread_messages = [
    "hey what r u doing",
    "stop by for sum fun",
    "i have your wallet :D",
    "i love u"]

show_messages(unread_messages)