# This function can be called and used multiples times.

__all__ = "extract_upper" # This means if all is extracted for this file, it will only extract the upper phrase

def extract_upper(phrase):  # defined a function to extract a uppercase phrase.
    return list(filter(str.isupper, phrase)) # there's a list, and filter the string with item that is uppercase of the phrase

def extract_lower(phrase):
    return list(filter(str.islower, phrase))