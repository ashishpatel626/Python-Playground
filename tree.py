from typing import Optional

class Node:
    def __init__(self, val: int, right: Optional['Node'] = None, left: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Node: (val: {self.val} left: {self.left} right: {self.right})"   
    
class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        if root is None:
            return 0
        
        x = self.maxDepth(root.left) + 1

        y = self.maxDepth(root.right) + 1

        return max(x, y)

    def create_tree(self) -> Node:
        root = Node(10)

        root.left = Node(2)
        root.right = Node(20)

        root.left.left = Node(1)
        root.left.right = Node(3)

        root.right.left = Node(15)
        root.right.right = Node(30)

        root.left.right.right = Node(39)

        return root

if __name__ == '__main__':
    s = Solution()
    s.maxDepth(s.create_tree())