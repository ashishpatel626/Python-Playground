from functools import singledispatchmethod
from typing import Any

class Person:
    def __init__(self, first_name: str, last_name: str, **kwargs: Any) -> None:
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(**kwargs)

    def full_name(self) -> str:
        fullName = f'{self.first_name} {self.last_name}'
        return fullName

class Pet:
    def __init__(self, animal: str, age: int, color: str, **kwargs: Any) -> None:
        if age < 0:
            raise ValueError("Age can not be a negative number")
        self.animal = animal
        self.age = age
        self.color = color
        super().__init__(**kwargs)

    def pet_info(self) -> str:
        info = f'Type: {self.animal}, Age: {self.age}, Color: {self.color}'
        return info

class Student(Person, Pet):
    def __init__(self, first_name: str, last_name: str, animal: str, age: int, color: str, id: int, dorm: str) -> None:
        super().__init__(first_name=first_name, last_name=last_name, animal=animal, age=age, color=color)
        if not id:
            raise ValueError("id can not be empty")
        self.id = id
        self.dorm = dorm
    
    def __len__(self) -> int:
        return len(self.full_name())

    @singledispatchmethod
    def study(self, none: None) -> str:
        return 'Studying general subjects'
    
    @study.register
    def _(self, subject: str) -> str:
        return f'Studying {subject}'