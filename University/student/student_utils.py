from typing import TypedDict
from school import Student

def get_full_info(student: Student) -> str:
    return f'Full Name: {student.full_name()} Pet Info: {student.pet_info()}'

data = TypedDict('data', {
    'first_name': str,
    'last_name': str,
    'animal': str,
    'age': int,
    'color': str,
    'id': int,
    'dorm': str
})

def create_student(data: data) -> Student:
    first_name = data['first_name']
    last_name = data['last_name']
    animal = data['animal']
    age = data['age']
    color = data['color']
    id = data['id']
    dorm = data['dorm']

    return Student(first_name, last_name, animal, age, color, id, dorm)