from typing import Optional, Any
from abc import ABC, abstractmethod
from multipledispatch import dispatch

class talk:
    def __init__(self, speak: str) -> None:
        self._speak = speak
    
    def speakInfo(self):
        return self._speak
    
class swim:
    def __init__(self, canSwim: bool, distance: Optional[int]) -> None:
        self.canSwim = canSwim
        self.distance = distance
    
    def swimInfo(self) -> str:
        return f'Can Swim: {self.canSwim} Distance {self.distance}'

class food(ABC):
    def __init__(self, meateater: bool, vegetarian: bool):
        self.meateater = meateater
        self.vegetarian = vegetarian
    
    @abstractmethod
    def info(self):
        return

class animal(talk, swim):
    def __init__(self, firstName: str, lastName: str, speak: str, canSwim: bool, distance: Optional[int]) -> None:
        talk.__init__(self, speak=speak)
        swim.__init__(self, canSwim=canSwim, distance=distance)
        self.firstName = firstName
        self.lastName = lastName
    
    @dispatch(str)
    def info(self) -> str:
         return f'Name: {self.firstName} {self.lastName}'
    
    @dispatch()
    def info(self) -> str:
        return f'speak: {self._speak}'
    
    

if __name__ == '__main__':
    dog = animal('kujo', 'patel', 'woof', True, 10)
    print(dog.info())