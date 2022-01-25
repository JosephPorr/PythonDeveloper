class Vehicle:   #Class is a clasifictation of an object.Vehicle is the type.
    """
    Vehicle is a means of transportation
    """

    class_variable = "Joe"
    # Self, customizes the initialization of the object. In this case, Vehicle.
    def __init__(self, engine, tires):  # Methods are fuctions attached to an object
        self.engine = engine
        self.tires = tires
        
    @classmethod  #converts a function to a class method.
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")
    

