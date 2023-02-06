import unittest

from src.phonebook import Phonebook

class PhoneBookTest(unittest.TestCase):

    # First contruct instance of unit under test which is Phonebook in setup
    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_by_name(self):
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
    # Checks to ensure lines within the with statement return an error and if does test will pass
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

# Unit test skip so will skip test
    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        phonebook = Phonebook()
    # Using assertTrue which means should return true for an empty phonebook
        self.assertTrue(phonebook.is_consistent())


