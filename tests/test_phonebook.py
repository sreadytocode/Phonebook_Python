import unittest

from src.phonebook import Phonebook

class PhoneBookTest(unittest.TestCase):

    # First contruct instance of unit under test which is Phonebook in setup
    # Setup called before every test method
    def setUp(self):
        self.phonebook = Phonebook()

    # Called after every test method. Do not need it at present but can be used
    # to clear up after test.
    # def tearDown(self):
    #     pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
    # Checks to ensure lines within the with statement return an error and if does test will pass
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

# Unit test skip so will skip test
    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
    # Using assertTrue which means should return true for an empty phonebook
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Maya", "1389100")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("John", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("John", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Susie", "34872")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("34872", self.phonebook.get_numbers())


