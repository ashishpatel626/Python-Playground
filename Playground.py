from typing import Any
from collections import deque
from queue import Queue


def queue():

    stack : deque[int] = deque()

    stack.append(1)

    q : Queue[int] = Queue(3)

    q.put(10)
    q.put(10)
    q.put(10)


    [print(x) for x in q.queue]


if __name__ == '__main__':
    queue()