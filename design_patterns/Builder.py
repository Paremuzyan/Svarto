class Vehicle:

    def __init__(self):
        self.sits_count = None
        self.mark = None
        self.hp = None
        self.color = None
        self.weight = None

    def __str__(self):
        return f"The {self.color} {self.mark} vehicle has \n {self.sits_count} sits, \n {self.hp} horsepower and {self.weight} pounds."


class VehicleBuilder:

    def __init__(self):
        self.vehicle = Vehicle()

    def __str__(self):
        return self.vehicle.__str__()

    def set_sits_count(self, count):
        self.vehicle.sits_count = count

    def set_mark(self, mark):
        self.vehicle.mark = mark

    def set_hp(self, hp):
        self.vehicle.hp = hp

    def set_color(self, color):
        self.vehicle.color = color

    def set_weight(self, weight):
        self.vehicle.weight = weight



v = VehicleBuilder()
v.set_mark('BMW')
v.set_weight(3.400)
v.set_sits_count(5)
v.set_color('black')
v.set_hp(140)
print(v)
