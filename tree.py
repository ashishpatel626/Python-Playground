from typing import Optional

class Node:
    def __init__(self, val: int, right: Optional['Node'] = None, left: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right



if __name__ == '__main__':
    root = Node(10)
    