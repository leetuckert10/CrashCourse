# Hello Admin
# create a list of users and print a special message if the user is admin.
users = ['terry', 'carLee', 'mike', 'ricky', 'linda', 'admin']
users = []      # make an empty list and check for it this version

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin! Would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thanks for logging in!")
else:
    print("The user list is empty!")
    print("We need to find some users!")