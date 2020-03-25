# Exercise 9-11: Imported Admin
#
from user import User
from user import Privileges
from user import Admin

privileges = ["can add post","can delete post","can ban user"]
admin = Admin("terry","Terry","Tucker", privileges)
admin.address_2 = "1690 Macedonia Church Rd"
admin.city = "Sparta"
admin.state = "NC"
admin.zip = "28675"
admin.describe_user()

# This code works too.
#admin.privileges.set_privilege(privileges)
#print("")
#admin.describe_user()

admin.privileges.add_privilege("can lay my wife")
print("")
admin.describe_user()

admin.privileges.remove_privilege("can lay my wife")
print("")
admin.describe_user()
