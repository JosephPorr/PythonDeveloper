# classmethod means: when this method is called, 
# we pass the class as the first argument instead of the instance of that class (as we normally do with methods).
# classmethod() methods are bound to a class rather than an object. 
# Class methods can be called by both class and object 

class Vehicle:   #Class is a clasifictation of an object.Vehicle is the type.
    """
    Vehicle is a means of transportation
    """

    class_variable = "Joe"
    # Self, customizes the initialization of the object. In this case, Vehicle.
    def __init__(self, distance_traveled=0, unit='miles'):  # Methods are fuctions attached to an object
        self.distance_traveled = distance_traveled
        self.unit = unit
        
    # @classmethod  #converts a function to a class method.
    # def bicycle(cls, tires=None):
    #    if not tires:
    #        tires = [cls.default_tire, cls.default_tire]
    #    return cls(None, tires)

    def description(self):
        return (f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}")
    # A print function would end the script, and not work in other classmethods
    # use return instead.

