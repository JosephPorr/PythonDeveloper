# Composition over inheritance.  
# Inheritance allows us to create new classes that add or modify the behavior of existing classes.   
# Makes existing classes more detailed.  
# As below, the “SnowTire” is a class inheritance of the existing class “Tire"
# Super() calls the implementation of the parent class, Tire.
# Return prints to the REPL
# repr returns a string that holds a printable representation of an object.
# Self is used everytime we use a method in a variable initialization

import math  # This is built in Python package for the math below

class Tire:
    """
    Tire represents a tire that would be used with an automobile.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def circumference(self):
        """
        The circumference of the tire in inches.

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        side_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
      """
      Represent the tire's information in the standard notation present
      on the side of the tire. Example: 'P215/64R15'
      """
      return(f"{self.tire_type}{self.width}/{self.ratio}"
             + f"{self.construction}{self.diameter}")
             
class snowTire(Tire):  # Inheritance a class, tire
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R')
        Tire,__init__(self, tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        The circumference of a tire w/ show chains in inches.

        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = (side_wall_inches + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self): #reper will return the string from the return of the 
        return super().__repr__() + " (Snow)  
        
