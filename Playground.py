from functools import singledispatchmethod


class addition:
    def __init__(self, a: int, b:int, z:int) -> None:
        self.a = a
        self.b = b
        self.z = z

    @singledispatchmethod
    def __add__(self, other) -> int:
        return addition(self.a + other.a, self.b + other)

    @__add__.register(int)
    def __add__(self, other) -> int:
        return addition(self.a + other.a, self.b, self.z + other)

odd_list = [x for x in range(10) if x%2 != 0]

def odd_num_generator():
    for i in range(1, 11, 2):
        yield i

def filter_string(strings: list[str], min_length: int) -> list[str]:
    string_list = [x for x in strings if len(x) >= min_length]
    return string_list




if __name__ == '__main__':
    addition1 = addition(2, 4, 5)
    addition1.__add__
    # print(odd_list)
    # print(list(odd_num_generator()))
    # print(filter_string(['test1', 'test2', 'test3', 'test4', 'te'], 3))