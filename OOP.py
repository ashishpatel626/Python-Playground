from abc import ABC, abstractmethod
from typing import Any, Optional
from functools import singledispatchmethod
from multipledispatch import dispatch

class fly(ABC):
    def __init__(self, distance: int, wingspan: int, speed: int, **kwargs: Any):
        self.distance = distance
        self.wingspan = wingspan
        self.speed = speed
        super().__init__(**kwargs)
    
    @abstractmethod
    def stamina(self):
        ...

class swim:
    def __init__(self, depth: int, breath: int, **kwargs: Any):
        self.depth = depth
        self.breath = breath
        super().__init__(**kwargs)
    
    def swim_info(self):
        print(f'Breath: {self.breath}, Depth: {self.depth}')

class animals():
    def __init__(self, name: str, color: str, age: int, **kwargs: Any):
        self.name = name
        self.color = color
        self.age = age
        super().__init__(**kwargs)

    @dispatch()
    def greet(self):
        print(f'{self.name} says hi!')
    
    @dispatch(str)
    def greet(self, custom_sound: str):
        print(f'{self.name} says {custom_sound}')
    

class dog(animals, swim):
    def __init__(self, breed1: str, breed2: Optional[str], name: str, color: str, age: int, depth: int, breath: int):
        self.breed1 = breed1
        self.breed2 = breed2
        super().__init__(name=name, color=color, age=age, depth=depth, breath=breath)

    def dog_info(self):
        print(f'Breed: {self.breed1, self.breed2}')


if __name__ == "__main__":
    molly = dog('lab', None, 'Molly', 'black', 3, 30, 50)
    
    molly.greet('test')