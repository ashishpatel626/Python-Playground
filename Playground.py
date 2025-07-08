def generator():
    for i in range(10):
        yield i

if __name__ == '__main__':
    output = [x for x in generator()]
    print([x for x in range(1, 10, 2)])