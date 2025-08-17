from abc import ABC, abstractmethod

class Animals(ABC):
    def __init__(self, name: str, color: str, age: int):
        self.name = name
        self.color = color
        self.age = age

    @abstractmethod
    def sounds():
        ...
    

    @abstractmethod
    def hello():
        ...


if __name__ == "__main__":
    tiger = Animals('asschecks', 'black', 10)

    print(tiger)