from school.models import Student

def get_full_info(student: Student) -> str:
    return f'Full Name: {student.full_name()} Pet Info: {student.pet_info()}'