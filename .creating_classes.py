class Car:  # Classes define your own object.  There built in objects like boolean, float or strig etc. Names start with capital letter
    """
    Docstring decribing the class, gives your object functionality called a method.
    Car models a car w/ tires and an engine.
    """

    def __init__(self, engine, tires): # def defines the method, and init points to the current object created, car.
        self.engine = engine
        self.tires = tires
        """
        "__init__" is a reseved method in python classes. 
        It 'initializes' the attributes to the class created.
        It is known as a constructor in object oriented concepts. 
        This method called when an object is created from the class 
        and it allow the class to initialize the attributes of a class.
        """
        # Pass means it not going to be immediately implemented.

    def description(self):  # Methods and functions are the same thing, just methods ae attached to objects
        print(f"A Car with an {self.engine} engine, and {self.tires} tires")

        # NOTES self represents the instance of the class. 
        # By using the “self” keyword we can access the attributes 
        # and methods of the class in python. 
        # It binds the attributes with the given arguments. 
        # self is parameter in function and user can use another parameter name in place of it.
        # The reason why we use self is that Python does not use the '@' syntax 
        # to refer to instance attributes. In Python, we have methods that make 
        # the instance to be passed automatically, but not received automatically.

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0   



