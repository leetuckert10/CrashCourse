# Exercise 8-10: Sending Messages
#   Make a list of several short messages and pass the list to a function
# that prints each message and removes it from the original list and
# appends it to another list that contains the printed messages.


def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(message)
        sent_messages.append(message)


def print_messages(messages, header_text=None):
    if header_text:
        print(f"{header_text}:")

    for message in messages:
        print(message)


unsent_messages = [
    "hey what r u doing",
    "stop by for sum fun",
    "i have your wallet :D",
    "i love u"]
sent_messages = []

send_messages(unsent_messages, sent_messages)

print("")
print_messages(unsent_messages, 'List of unsent messages')

print("")
print_messages(sent_messages, 'List of sent messages')
