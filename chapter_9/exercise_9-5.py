# Exercise 9-5: Login Attempts

# This program uses the User class in user.py. Added the attribute
# login_attempts and a method for increment by one. Also added a method to
# rest to zero.

from user import User
#import user as u


u1 = User("leetuckert", "terry", "tucker")
u1.address_2 = "1690 Macedonia Church Rd."
u1.city = "Sparta"
u1.state = "NC"
u1.zip = "28675"

u1.describe_user()
print("")

u1.increment_login_attempts()   # One attempt.
u1.describe_user()
print("")

u1.increment_login_attempts()   # Two attempts.
u1.increment_login_attempts()   # Three attempts, max for you buddy...
u1.increment_login_attempts()   # Class will generate an error.

print("")
u1.describe_user()
print("")

u1.reset_login_attempts()
u1.describe_user()
print("")

u1.greet_user()
