from student import create_student, data

if __name__ == '__main__':
    student_data : data = {'first_name': 'John', 'last_name': 'Adam', 'animal': 'Tiger', 'age': 34, 'color': 'black', 'id': 10, 'dorm': 'falcon'}

    student1 = create_student(data=student_data)


    print(student1.full_name())