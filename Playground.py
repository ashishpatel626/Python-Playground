from functools import singledispatchmethod
from typing import Callable

class addition:
    def __init__(self, a: int, b:int, z:int) -> None:
        self.a = a
        self.b = b
        self.z = z

    @singledispatchmethod
    def __add__(self, other: 'addition'):
        return self.a + other.a, self.b + other.b, self.z + other.z

    @__add__.register(int)
    def _(self, other: int):
        return self.a + other, self.b + other, self.z + other

x : Callable[[int, int], int] = lambda x, y : x + y

if __name__ == '__main__':
    addition1 = addition(2, 4, 5)
    addition2 = addition(3, 5, 6)

    print(addition1 + addition2)
    print(addition1 + 1)

    print(x(5, 4))