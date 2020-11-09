# inspect and combine omitted
class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # https://docs.python.org/3/library/functions.html#classmethod
    # A class method receives the class as implicit first argument, 
    # just like an instance method receives the instance.

    @classmethod 
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    # A static method does not receive an implicit first argument. 
    # https://docs.python.org/3/library/functions.html#staticmethod

    @staticmethod 
    def name():
        return "Kevin Bacon"

    # https://docs.python.org/3/library/functions.html#property

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"