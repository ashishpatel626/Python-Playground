class car():
    def __init__(self, make, model, year):
        self.make = input("Enter Make ")
        self.model = input("Enter Model ")
        self.year = input("Enter year ")

        return (self.make + " " + self.model + " " + self.year)


class electric(car):
    def batteryType(self, type):
        self.type = input("Enter Battery Type ")
        return self.type


el = electric("a", "b", "c")

print(el.batteryType())


