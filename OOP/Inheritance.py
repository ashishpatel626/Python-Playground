from multipledispatch import dispatch 

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @dispatch(int, int)
    def mak(a, b):
        result = a * b
        return result

class electricCar(car):
    def __init__(self, make, model, year, battery):
        car.__init__(self, make, model, year)
        self.battery = battery
    
    @dispatch(int)
    def mak(a):
        return a

car1 = car("honda", "insight", 2019)

ecar = electricCar("honda", "insight", 2019, "LG")

print(ecar.mak(4, 5))
