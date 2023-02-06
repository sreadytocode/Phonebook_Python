import unittest

from src.phonebook import Phonebook

class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
    # First contruct instance of unit under test which is Phonebook
        phonebook = Phonebook()
    # Checks to ensure lines within the with statement return an error and if does test will pass
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

