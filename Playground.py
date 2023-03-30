from dis import dis
from unittest import result
from multipledispatch import dispatch

class car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
    
    @dispatch(int, int)
    def product(self, x: int, y: int):
        result = x * y
        return result
    
    @dispatch(int, int, int)
    def product(self, x: int, y: int, z: int):
        result = x * y * z
        return result


class electricCar(car):
    def __init__(self, make, model, year, battery):
        car.__init__(self, make, model, year)
        self.battery = battery

    
    
Honda = car("Honda", "Insight", 2019)
Tesla = electricCar("Tesla", "Model S", 2020, "LG Smart Phone Battery")

