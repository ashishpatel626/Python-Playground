'''
A list is mutable, ordered, has random access and can contain duplicates.
The only difference in a tuple is that it is non mutable and both have a random access of o(1).
You would use a tuple when you have a static dataset.
'''

odd_list = [x for x in range(10) if x%2 != 0]

def odd_num_generator():
    for i in range(1, 11, 2):
        yield i

def filter_string(strings: list[str], min_length: int) -> list[str]:
    string_list = [x for x in strings if len(x) >= min_length]
    return string_list

 


if __name__ == '__main__':
    # print(odd_list)
    # print(list(odd_num_generator()))
    # print(filter_string(['test1', 'test2', 'test3', 'test4', 'te'], 3))