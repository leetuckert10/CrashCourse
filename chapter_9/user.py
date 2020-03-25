"""A set of clases that can be used to represent users, specialized users and
privileges."""


class User:
    """The User class is a simple attempt to model a computer user."""
    def __init__(self, user_id, first_name, last_name,
            address_1=None,
            address_2=None,
            city=None,
            state=None,
            zip=None):
        """Initialize User attributes."""
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zip = zip
        self.login_attempts = 0

    def describe_user(self):
        """Print out a description of User attributes."""
        print(f"The user's id is: {self.user_id}.")
        print(f"Full name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"{self.first_name.title()} lives in {self.city} in {self.state}")
        print(f"\tat {self.address_2}")
        if self.address_1:
            print(f"\tat {self.address_1}")
        print(f"Login attempts: {self.login_attempts}.")

    def greet_user(self):
        """Greet the user with a personalized message."""
        print(f"Greetings {self.first_name.title()}! Glad to see you!")

    def increment_login_attempts(self):
        """This method increments the value of login_attempts by one."""
        if self.login_attempts == 3:
            print(f"Maximum number of login attempts has been reached. "
                  f"Please contact your system administrator.")
        else:
            self.login_attempts += 1

    def reset_login_attempts(self):
        """This method resets the value of login_attempts to zero."""
        self.login_attempts = 0


class Privileges:
    """This class models privileges that a user can have."""
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
    """This class inherits User and is used to represent the specialized user
    Admin."""
    def __init__(self, userid, first_name, last_name, privileges=[]):
        super().__init__(userid, first_name, last_name)
        self.privileges = Privileges(privileges)

    def describe_user(self):
        """This method displays the information we have on a user."""
        super().describe_user()
        self.privileges.show_privileges()

