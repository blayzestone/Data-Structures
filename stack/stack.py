"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from linkedList import Node, LinkedList


# Stack with array (list)
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)
#         return value

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop(0)


# Stack with Singly Linked List
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def push(self, value):

        newHead = Node(value)
        newHead.set_next(self.storage.head)
        self.storage.head = newHead
        self.size = self.size + 1
        return value

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.remove_head()
