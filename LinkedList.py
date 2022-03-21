class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.next == None:
                currentNode.next = node
                break
            currentNode = currentNode.next

    def print(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.value, "->", end=" ")
            currentNode = currentNode.next
        print("None")
        
ll = linkedList()
ll.print()
ll.insert("55")
ll.print()
ll.insert("44")
ll.print()
