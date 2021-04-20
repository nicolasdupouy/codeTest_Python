import unittest

from Books.Book_CrakingTheCodingInterview.src.Chapter_01_ArraysAndStrings.IsUnique import is_unique


class IsUniqueTestCase(unittest.TestCase):
    def test_string_longer_than_the_alphabet(self):
        self.assertEqual(False, is_unique("abcdefghijklmnopqrstuvwxyztest"))

    def test_abcd_has_all_unique_characters(self):
        self.assertEqual(True, is_unique("abcd"))

    def test_abcad_has_not_all_unique_characters(self):
        self.assertEqual(False, is_unique("abcad"))
