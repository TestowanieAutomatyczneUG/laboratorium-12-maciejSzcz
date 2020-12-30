# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from src.user_api.random_user import RandomUser


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_random_user_get_user_returns_dict(self):
        user = self.temp.get_user()
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_has_name(self):
        user = self.temp.get_user()
        self.assertIsInstance(user["name"]["first"], str)

    def test_random_user_get_user_with_gender_returns_dict(self):
        user = self.temp.get_user_with_gender("male")
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_with_gender_male_returns_male_user(self):
        user = self.temp.get_user_with_gender("male")
        self.assertEqual(user["gender"], "male")

    def test_random_user_get_user_with_gender_integer_raises_typeError(self):
        self.assertRaises(TypeError, self.temp.get_user_with_gender, 123)

    def test_random_user_get_user_with_gender_incorrect_raises_valueError(self):
        self.assertRaises(ValueError, self.temp.get_user_with_gender, "andrzej")

    def test_random_user_get_user_with_nationality(self):
        user = self.temp.get_user_with_nationality("AU")
        self.assertIsInstance(user, dict)

    def test_random_user_get_user_with_nationality_returns_correct_nationality(self):
        user = self.temp.get_user_with_nationality("AU")
        self.assertEqual(user["location"]["country"], "Australia")

    def test_random_user_get_user_with_nationality_integer_raises_typeError(self):
        self.assertRaises(TypeError, self.temp.get_user_with_nationality, 123)

    def test_random_user_get_user_with_nationality_incorrect_raises_valueError(self):
        self.assertRaises(ValueError, self.temp.get_user_with_nationality, "PL")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
