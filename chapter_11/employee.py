# Exercise 11-3: Employee
#
# Write a class called Employee. Attributes include first name, last name,
# annual salary. Write a method called give_raise with a default parameter of
# $5,000 but also accepts a different amount.


class Employee:
    """This class is a very simple representation of an employee."""
    def __init__(self, first_name, last_name, salary, middle_name=""):
        """Three attributes: first_name, last_name, salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.middle_name = middle_name

    def give_raise(self, amount=5000):
        self.salary += amount

    def get_first_name(self):
        """Return the value of first_name."""
        return self.first_name

    def get_last_name(self):
        """Return the value of last_name."""
        return self.last_name

    def get_formatted_name(self):
        """Return a formatted name as in "Terry Tucker"""
        if self.middle_name:
            formatted_name = f"{self.first_name} {self.middle_name}" \
                             f" {self.last_name}"
        else:
            formatted_name = f"{self.first_name} {self.last_name}"
        return formatted_name

    def get_salary(self):
        """Return the value of salary."""
        return self.salary

