'''
**kwargs is used for inhertiance to pass down arguments to the child
*args is used for overloading functions


'''
import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Method Name: {func.__name__} Arguments {args[1:]}, keyword Arguments: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

class Sports:
    def __init__(self, sport: str, division: int, **kwargs):
        self.sport = sport
        self.division = division
        super().__init__(**kwargs)

class Student(Sports):
    def __init__(self, first_name: str, last_name: str, sport: str, division: int, *courses: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.courses = list(courses)
        super().__init__(sport=sport, division=division)
    
    @log_call
    def student_info(self) -> str:
        return f'Name: {self.first_name} {self.last_name} Sport: {self.sport} '

def multiply_and_add(x: int, y: int, multiplier: int = 2, offset: int = 0) -> int:
    return (x * y * multiplier) + offset

def multiply_and_add2(x: int, y: int, multiplier: int, offset: int) -> int:
    return (x * y * multiplier) + offset


if __name__ == '__main__':
    student1 = Student('Ashish', 'Patel', 'Football', 10, 'Spanish', 'Gym', 'History', 'Biology')
    print(multiply_and_add(4, 5))
    print(multiply_and_add2(4, 5, 6, 3))
    print(student1.student_info())
    