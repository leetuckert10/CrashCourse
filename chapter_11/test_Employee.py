# Exercise 11-3: Test Employee
#
# Wrtie a test case for Employee that tests every method especially
# give_raise() which can have a default value as well as specific value.

import unittest
from employee import Employee


class TestEmployeeClass(unittest.TestCase):
    """This is the test class for the Employee class."""

    # When you define a setUp() method, Python runs setUp() each time before
    # it executes a test_* method.
    def setUp(self):
        self.employee = Employee("Terry", "Tucker", 50_000, "Lee")

    def test_give_raise_default(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.get_salary(), 55_000)

    def test_give_raise(self):
        self.employee.give_raise(10_000)
        self.assertEqual(self.employee.get_salary(), 60_000)

    def test_get_formatted_name(self):
        self.assertEqual(self.employee.get_formatted_name(), "Terry Lee Tucker")

    def test_get_first_name(self):
        self.assertEqual(self.employee.get_first_name(), "Terry")

    def test_get_last_name(self):
        self.assertEqual(self.employee.get_last_name(), "Tucker")


if __name__ == '__main__':
    unittest.main()
