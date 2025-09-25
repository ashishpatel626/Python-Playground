from typing import Optional, Any

class Solution:
    def max_depth(self, Tree: 'Node'):

        depth = 0
        queue : list[Any] = []
        queue.append(Tree)
        counter = 0

        while queue:
            x = queue.pop(0)
            
            print(f'{x} \n')
            if x.left:
                print(f'left {x.left}')
                queue.append(x.left)
            if x.right:
                print(f'right {x.right} \n')
                queue.append(x.right)
            
            if counter == 0:
                depth += 1
                counter = len(queue)

            counter -= 1

        print(depth)

    def create_tree(self) -> 'Node':
        root = Node(10)

        root.left = Node(2)
        root.right = Node(20)

        root.left.left = Node(1)
        root.left.right = Node(3)

        root.right.left = Node(15)
        root.right.right = Node(30)

        return root

class Node:
    def __init__(self, val: int, right: Optional['Node'] = None, left: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Node: (val: {self.val} left: {self.left} right: {self.right})"   


if __name__ == '__main__':
    s = Solution()
    s.max_depth(s.create_tree())
    print(s)