# test_python_repos.py
#
# Write a program called test_python_repos.py that uses unittest to assert
# that the value of status_code is 200. Figure out some other assertions to
# make.

import unittest
import requests
from python_repos import get_data, get_dicts
from typing import List


class TestPythonRepos(unittest.TestCase):
    """This is the test class for python_repos.py."""
    def test_status_code(self):
        """Make sure that we are getting a status code of 200."""
        r: requests.models.Response = get_data()
        self.assertEqual(r.status_code, 200)

    def test_number_dicts_returned(self):
        """Make sure the number of dictionaries in the last is greater than
        zero."""
        r: requests.models.Response = get_data()
        repo_dicts: List = get_dicts(r)
        self.assertGreater(len(repo_dicts), 0)


if __name__ == '__main__':
    unittest.main()
