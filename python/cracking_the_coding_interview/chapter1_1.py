""" Implement an algorithm to determine if a string has all unique characters. """


def is_unique(string):
    """ Simple implementation using sets. """
    return len(set(string)) == len(string)


assert is_unique("abc") is True
assert is_unique("abb") is False
assert is_unique("abcgdefgh") is False


def is_unique_no_sets(string):
    """ What if you cannot use additional data structures? """
    seen = {}
    for c in string:
        if c in seen:
            return False
        else:
            seen[c] = True
    return True


assert is_unique_no_sets("abc") is True
assert is_unique_no_sets("abb") is False
assert is_unique_no_sets("abcgdefgh") is False


def is_unique_no_additional_data_structures(string):
    """ Literally no additional data structures beyond a sorted copy of the string
        and a loop counter variable.
    """
    string = sorted(string)
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True


assert is_unique_no_additional_data_structures("abc") is True
assert is_unique_no_additional_data_structures("abb") is False
assert is_unique_no_additional_data_structures("abcgdefgh") is False
