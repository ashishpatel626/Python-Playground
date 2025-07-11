from functools import singledispatchmethod
import gc

@singledispatchmethod
def product(first: int, second: int) -> int:
    return first * second

@product.register
def _(first: int, second: int, third: int) -> int:
    return first * second * third

class car:
    def __init__(self, model: str, make: str, year: int):
        self.model = model
        self.make = make
        self.year = year
    
    def product(self):
        return 10
    
class electricCar(car):
    def __init__(self, make: str, model: str, year: int, battery: str):
        car.__init__(self, make, model, year)
        self.battery = battery
    
    def product(self):
        return super().product()

car1 = car("honda", "insight", 2019)
ecar = electricCar("honda", "insight", 2019, "LG")

print(ecar.product())

class Book:
    def __init__(self, price: int) -> None:
        self.price = price

    def __add__(self, other: int) -> int:
        return self.price + other

    def __lt__(self, other: int) -> int:
        return self.price < other

book1 = Book(10)
book2 = Book(20)

total_price = book1.price + book2.price
Compare = book1.price < book2.price

print(f'Total Price: {total_price}, Compare: {Compare}')