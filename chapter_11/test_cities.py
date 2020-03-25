# Exercise 11-1: City, Country
#
# Create a file called test_city.py that tests the function you just wrote.
# Write a method called test_city_country() in the class you create for testing
# the function. Make sure it passes the test.
#
# Remember to import unittest and the function you are testing. Remember that
# the test class should inherit unittest.TestCase. Remember that the test
# methods in the class need to begin with the word 'test' to be automatically
# executed.

import unittest
from city_functions import get_formatted_city_country


class CityCountryNameTestCase(unittest.TestCase):
    """Tests get_formatted_city_country()."""
    def test_city_country(self):
        """Do names like santiago chile work?"""
        formatted_city_country = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, "Santiago, Chile")

    def test_city_country_population(self):
        """Does a city name, a country name, and a population work?"""
        formatted_city_country = get_formatted_city_country('santiago',
                                                            'chile', 50_000_000)
        self.assertEqual(formatted_city_country, "Santiago, Chile - "
                                                 "Population 50000000")


if __name__ == '__main__':
    unittest.main()
