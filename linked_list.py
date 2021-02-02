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

    def delete_node_by_data(self, data):
        if self.head is None: return None
        n = self.head

        if n.data is not None:
            self.head = self.head.next
            return 

        while n.next is not None:
            if n.next == data:
                n.next = n.next.next
                return self.head
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

    def remove_dups_buffer(self):
        """
        Q 2.1
        Remove duplicates from Linked List
        With temporary buffer
        Time Complexity worst case = O(n) * O(n) = O(n^2)
            best case = O(n) * O(1) = O(n)
        Space Complextiy = Space(linked list) + Space(seen list) = O(n^2)
        """
        if self.head is None: return None
        seen = []
        n = self.head 

        while n.next is not None: # O(n) time complexity
            if n.next.data in seen:
                self.delete_node_by_data(n.next.data) # T(delete): worst case => O(n), best => O(1)
            else:
                seen.append(n.next.data)
            n = n.next

    def remove_dups(self):
        """
        Q 2.1 
        Remove duplicates
        Withouth temporary buffer
        """
        if self.head is None: return None
        n = self.head
        return

"""
Q 2.1 Remove Duplicates
Traverse Linked List and put data into seen array
If data is in seen: delete node
"""
print('Running Question 2.1...')
nums_dup = [2, 4, 1, 2, 5, 1, 4, 9]
ll_dup = LL()
ll_dup = ll_dup.generate(nums_dup)
print("Removing duplicates with buffer")
ll_dup.remove_dups_buffer()
ll_dup.traverse() 

print("Removing duplicates without buffer")
ll_dup.generate(nums_dup)
ll_dup.remove_dups()
ll_dup.traverse()



