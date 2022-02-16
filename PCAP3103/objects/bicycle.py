#  Instead re=writing the same code, this will inherit the classmethod "vehicle."

from vehicle import Vehicle

class Bicycle(Vehicle):  #this will directly inherit the classmethod.
    default_tire = 'tire'

# the Vehicle class requuired two positions, 'engine' & 'tires'.

    def __init__(self, tires=None, distance_traveled=0, unit='miles'):  # Self always refers to the instance.  __init__ is a hook
        super().__init__(distance_traveled, unit)
        if not tires:
            tires = [self.default_tire,self.default.tire]
        self.tires = tires

    def description(self):
        initial = super().description()
        return f"{initial} on {len(self.tires)} tires"

if __name__ == "__main__":
    bike = Bicycle()
    print(bike.drescription())