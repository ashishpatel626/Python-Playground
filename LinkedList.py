class Node:
    def __init__(self, data: int, next: 'Node | None') -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_front(self, data: int):
        self.head = Node(data, self.head)      

    def add_at_end(self, data: int):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        if not self.head:
            return None
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.is_empty())

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodeLen = 0
        currNode = head
        while currNode != None:
            nodeLen += 1
            currNode = currNode.next
            
        l = (nodeLen - k) + 1
        
        currNode = head
        for i in range(1, nodeLen):
            if i == k:
                swap1 = currNode
            if i == l:
                swap2 = currNode
            if currNode != None:
                currNode = currNode.next
        
        currNode = head
        for i in range(1, nodeLen):
            if i == k:
                currNode = swap2
            if i == l:
                currNode = swap1
            if currNode != None:
                currNode = currNode.next
        
        return head
'''