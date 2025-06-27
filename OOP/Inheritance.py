class Person:
    def __init__(self, firstName, lastName, **kwargs):
        super().__init__(**kwargs)
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        fullName = self.firstName + " " + self.lastName
        return fullName

class Pet:
    def __init__(self, animal, age, color, **kwargs):
        super().__init__(**kwargs)
        self.animal = animal
        self.age = age
        self.color = color

    def petInfo(self):
        info = f'Type: {self.animal}, Age: {self.age}, Color: {self.color}'
        return info

class Student(Person, Pet):
    def __init__(self, firstName, lastName, animal, age, color, id, dorm):
        super().__init__(firstName=firstName, lastName=lastName, animal=animal, age=age, color=color)
        self.id = id
        self.dorm = dorm

if __name__ == '__main__':
    Name = Person("Solid", "Snake")
    student1 = Student('Raiden', 'El', 'tiger', 20, 'black', 101, 'South Building')

    print(student1.petInfo())
    
