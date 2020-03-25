# Checking user names
# create a list of current users
current_users = ['terry', 'CarLee', 'Mike', 'Ricky', 'Linda', 'admin']
# a list of new users
new_users = ['Wilma', 'Admin', 'TERRY', 'joe', 'John']

if not current_users or not new_users:
    print("A user list is empty!")

# create a lower case version of current_users
lower_users = []
for user in current_users:
    lower_users.append(user.lower())

# look for duplicates
for new_user in new_users:
    if new_user.lower() in lower_users:
        print(f"{new_user} has already been taken.")
        print("Please pick a different user name...")
    else:
        print(f"{new_user} is available.")
