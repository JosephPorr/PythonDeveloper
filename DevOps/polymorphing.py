 # Polymorphism in python defines methods in the child class that have the same name 
 # as the methods in the parent class.
 # len() returns the lenth of the string

 class  Car:
     """
     Car models a car w/ tires and an engine
     """

     def __init__(self, enginem tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with a {self.engine} engine, and {self.tires} tires")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0