# Exercise 9-8: Privileges
#
# Using the code from Exercise 9-7, create a separate class called Privileges
# that has one attribute: a list of privileges. Move set_privilege() and
# remove_privilege() from the Admin class over to the Privileges class.

from user import User


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def set_privilege(self, privileges):
        """This method sets privileges for the admin user."""
        self.privileges = privileges

    def add_privilege(self, privilege):
        """This method appends a privilege to the end of the privileges list."""
        self.privileges.append(privilege)

    def remove_privilege(self, privilege):
        """This method removes privileges from the Admin user."""
        if privilege in self.privileges:
            self.privileges.remove(privilege)

    def show_privileges(self):
        print("Privileges: ", end="")
        for privilege in self.privileges:
            if privilege == self.privileges[-1]:
                print(f"{privilege}.", end="")
            else:
                print(f"{privilege}, ", end="")
        print("")


class Admin(User):
    def __init__(self, userid, first_name, last_name, privileges=[]):
        super().__init__(userid, first_name, last_name)
        self.privileges = Privileges(privileges)

    def describe_user(self):
        """This mehtod displays the information we have on a user."""
        super().describe_user()
        self.privileges.show_privileges()


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
