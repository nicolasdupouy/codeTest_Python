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
