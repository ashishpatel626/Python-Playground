from student.student_utils import get_full_info
from school.models import Student

if __name__ == '__main__':
    student1 = Student('Raiden', 'El', 'tiger', 20, 'black', 101, 'South Building')
    print(get_full_info(student1))
    print(student1.study('Physics'))