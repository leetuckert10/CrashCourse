# Exercise 9-2: Users
#   Create a class called User. Create two attributes called first_name and
# last_name. Create several other attributes that are associated with a user
# profile. Create a method called describe_user() that displays information
# about the user. Create a method called greet_user() that prints out a 
# personalized greeting.
        
# Class definition moved to user.py.

import user as u

u1 = u.User("leetuckert", "terry", "tucker")
u1.address_2 = "1690 Macedonia Church Rd."
u1.city = "Sparta"
u1.state = "NC"
u1.zip = "28675"
u1.describe_user()
u1.greet_user()

