# Exercise 9-7: Admin
#
# Create a class called Admin that extends class User. Create a list of
# privileges that and adminstrator has. Create a method to show privileges.

from user import User


class Admin(User):
    def __init__(self, userid, first_name, last_name, privileges=None):
        super().__init__(userid, first_name, last_name)
        self.privileges = privileges

    def set_privilege(self, privileges):
        """This method set privileges for the admin user."""
        self.privileges = privileges

    def remove_privilege(self, privilege):
        """This method removes privileges from the Admin user."""

    def describe_user(self):
        super().describe_user()
        print("Privileges: ", end="")
        for privilege in self.privileges:
            if privilege == self.privileges[-1]:
                print(f"{privilege}.", end="")
            else:
                print(f"{privilege}, ", end="")
        print("")


privileges = "can add post","can delete post","can ban user"
admin = Admin("terry","Terry","Tucker", privileges)
admin.address_2 = "1690 Macedonia Church Rd"
admin.city = "Sparta"
admin.state = "NC"
admin.zip = "28675"
admin.describe_user()

