class Person:
    def __init__(self, first_name: str, last_name: str, **kwargs) -> None:
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(**kwargs)

    def fullName(self) -> str:
        fullName = f'{self.first_name} {self.last_name}'
        return fullName

class Pet:
    def __init__(self, animal: str, age: int, color: str, **kwargs) -> None:
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

if __name__ == '__main__':
    try:
        student1 = Student('Raiden', 'El', 'tiger', 20, 'black', 101, 'South Building')
    except ValueError as e:
        print(f'Error: {e}')

    print(student1.fullName())
    print(student1.petInfo())

