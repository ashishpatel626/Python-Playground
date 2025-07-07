from multipledispatch import dispatch
from student.student_utils import get_full_info
from school import models

if __name__ == '__main__':

    student1 = models.Student('Raiden', 'El', 'tiger', 20, 'black', 101, 'South Building')

    # print(len(student1))
    # print(student1.study())
    # print(student1.study('Math'))

    print(get_full_info(student1))

'''
1. Theory: The super() function is used to inherit the parameters of the parent class.
The inhertiable classes need **kwargs because of the arbitrary number of arguments that will be inheritied by a child class.

'''