import unittest


def is_unique(string_to_test):
    found_letters = {}
    # If we assume the string is in the english alphabet which contains 26 letters
    # Then there is duplicates in a longer string.
    if len(string_to_test) > 26:
        return False

    for c in string_to_test:
        if c in found_letters.keys():
            return False
        found_letters[c] = True

    return True


class IsUniqueTest(unittest.TestCase):

    def test_string_longer_than_the_alphabet(self):
        self.assertEqual(False, is_unique("abcdefghijklmnopqrstuvwxyztest"))

    def test_abcd_has_all_unique_characters(self):
        self.assertEqual(True, is_unique("abcd"))

    def test_abcad_has_not_all_unique_characters(self):
        self.assertEqual(False, is_unique("abcad"))


#if __name__ == '__main__':
#    unittest.main()
