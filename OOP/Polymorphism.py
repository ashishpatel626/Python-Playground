from multipledispatch import dispatch
import gc

@dispatch(int, int)
def product(first, second):
    result = first * second
    return result

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    return result



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
        return super().product()

car1 = car("honda", "insight", 2019)
ecar = electricCar("honda", "insight", 2019, "LG")

print(ecar.product())

class Book:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __lt__(self, other):
        return self.price < other.price

book1 = Book(10)
book2 = Book(20)

total_price = book1 + book2
compare = book1 < book2
print (compare)


print(gc.get_threshold())