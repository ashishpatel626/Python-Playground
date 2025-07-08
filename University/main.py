from student.student_utils import get_full_info
from school import models

if __name__ == '__main__':

    student1 = models.Student('Raiden', 'El', 'tiger', 20, 'black', 101, 'South Building')

    # print(len(student1))
    # print(student1.study())
    # print(student1.study('Math'))

    print(get_full_info(student1))