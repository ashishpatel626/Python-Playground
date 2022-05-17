from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first * second
    return result

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    return result

print(product(3, 3))

class car:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
    
    def product(self):
        return 10
    
class electricCar(car):
    def __init__(self, make, model, year, battery):
        car.__init__(self, make, model, year)
        self.battery = battery
    
    def product(self):
        x = car.product(self)
        return x

car1 = car("honda", "insight", 2019)
ecar = electricCar("honda", "insight", 2019, "LG")
print(ecar.product())