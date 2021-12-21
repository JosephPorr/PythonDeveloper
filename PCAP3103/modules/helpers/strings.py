def extract_upper(phrase):
    """
    extract_upper takkes a string and returns a list containing
    only the uppercase characters from the string.

    >>> extract_upper("Hello There, BOB")
    ['H', 'T', 'B', 'O', '']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))