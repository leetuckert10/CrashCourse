# Exercise 7-10: Dream Vacation
#   Write a program that prompts users about their dream vacation. When the
# input stops, print out the results of the poll.

poll = {}
flag = True

print("This poll is gathering data regarding what would be your dream "
      "vacation. Please follow the prompts to enter your data. Type 'quit' to"
      "finish the poll.\n")
while flag:
    name = input("Name: ")
    if name == 'quit':
        flag = False
    else:
        dream = input("Describe your Dream Vacation: ")
        # Store the data
        poll[name] = dream
    print("")

print("Poll results:")
for name, dream in poll.items():
    print(f"{name.title()}'s Dream Vacation is:")
    print(f"{dream}\n")
