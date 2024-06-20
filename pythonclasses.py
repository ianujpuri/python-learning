
#examles of classess in python

class Vehicle():
    def __init__(self, bodyStyle):
        self.bodyStyle = bodyStyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, engineType):
        super().__init__("Car")
        self.engineType = engineType
        self.wheels = 4
        self.door = 4

    def drive(self, speed):
        super().drive(100)
        print("Driving my ", self.engineType + " car at speed", self.speed)


class Motorcycle(Vehicle):
    def __init__(self, engineType, hasSideCar):
        super().__init__("Motorcycle")
        if(hasSideCar):
            self.wheels = 3
        else:
            self.wheels = 2

        self.door = 0
        self.engineType = engineType

        def drive(self, speed):
            super().drive(100)
            print("Driving my ", self.engineType + " motorcycle at speed", self.speed)

car1 = Car("Gas")
car1.drive(30)

car2 = Car("Electric")
car2.drive(50)

mc1 = Motorcycle("gas", True)
mc1.drive(80)

print("Motorcycle has", mc1.wheels, "wheels")
print("car1 engine type is", car1.engineType)
print("car2 has ",car2.door,"doors")
