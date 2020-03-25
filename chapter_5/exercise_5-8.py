# Hello Admin
# create a list of users and print a special message if the user is admin.
users = ['terry', 'carLee', 'mike', 'ricky', 'linda', 'admin']

for user in users:
    if user == 'admin':
        print("Hello admin! Would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thanks for logging in!")