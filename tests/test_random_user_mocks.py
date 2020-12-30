# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from unittest.mock import Mock, patch
from unittest.mock import *

from src.user_api.random_user import RandomUser
from tests.random_user_mock_results import random_user_result, random_user_with_gender_result, random_user_with_nationality_result


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_random_user_get_user(self):
        self.temp.get_user = MagicMock(return_value=random_user_result)
        self.assertEqual(self.temp.get_user(), random_user_result)

    def test_random_user_get_user_with_gender(self):
        self.temp.get_user_with_gender = MagicMock(return_value=random_user_with_gender_result)
        self.assertEqual(self.temp.get_user_with_gender(), random_user_with_gender_result)

    def test_random_user_get_user_with_nationality(self):
        self.temp.get_user_with_nationality = MagicMock(return_value=random_user_with_nationality_result)
        self.assertEqual(self.temp.get_user_with_nationality(), random_user_with_nationality_result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
