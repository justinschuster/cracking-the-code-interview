"""
Linked List chapter from the book.
Single Linked List
Node implementation and questions answers
"""

class Node:
    next = None
    data = None 

    def __init__(self, d):
        self.data = d

class LL:
    head = None

    def __init__(self, head=None):
        self.head = head

    def delete_node(self, data):
        if self.head is None: return None
        n = self.head

        if n.data is not None:
            return head.next

        while n.next is not None:
            if n.next == data:
                n.next = n.next.next
                return head
            n = n.next
        
        return head

    def add_node(self, data):
        if self.head is None:
            self.head = Node(data)
        n = self.head

        while n.next is not None:
            n = n.next
        n.next = Node(data)

    def generate(self, arr):
        for n in arr:
            self.add_node(n) 
        return self

    def traverse(self):
        if self.head is None: 
            print('Empty Linked List')
            return None
        n = self.head
        
        while n.next is not None:
            print(n.next.data)
            n = n.next

# Create a linked list
nums = [2, 3, 4, 1, 6, 7]
l = LL() # create empty Linked List

print('Generating Linked List...')
l = l.generate(nums)

print('Traversing Linked List...')
l.traverse()

# Q 2.1
# Remove duplicates from Linked List
