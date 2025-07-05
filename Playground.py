'''
A tuple is non-mutable, random access, ordered and allows duplicates.
A list is ordered, has random access, mutable and allows duplicates.

use a tuple when you have a static dataset. Both have a random access of o(1)

odd_num = [x for x in range(10) if x % 2 != 0]

def odd_num_generator():
    y = 0
    while y <= 10:
        if y % 2 != 0:
            yield y
        y += 1


'''
def string(string: list[str] ) -> list[str]:
    pass