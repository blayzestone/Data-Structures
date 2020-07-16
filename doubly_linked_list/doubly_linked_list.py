"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        if self.length < 0:
            self.length = 0

        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        self.length += 1

        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(value)
            current_head = self.head

            new_node.next = current_head
            current_head.prev = new_node

            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        self.length -= 1

        if self.head.next is None:
            self.tail = None

        old_head = self.head

        self.head = self.head.next

        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        self.length += 1

        if self.head is None and self.tail is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(value)
            old_tail = self.tail

            self.tail = new_node
            self.tail.prev = old_tail
            self.tail.next = None

            old_tail.next = self.tail

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        self.length -= 1

        old_tail = self.tail

        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None

        return old_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node is not None:
            prev_node.next = next_node

        if next_node is not None:
            next_node.prev = prev_node

        old_head = self.head

        new_head = node
        new_head.prev = None
        new_head.next = old_head

        self.head = new_head

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value

        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            prev_node = node.prev
            next_node = node.next

            prev_node.next = node.next
            next_node.prev = node.prev

            self.length -= 1
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        self.length -= 1

        if (
            node.prev is None and node.next is None
        ):  # delete node when only one node is in the list
            node = None
            self.head = node
            self.tail = node
        elif (
            node.prev is None and node.next is not None
        ):  # delete node that is the head of the list
            self.head = node.next
            self.head.prev = None
            node = None
        elif (
            node.prev is not None and node.next is None
        ):  # delete node that is the tail of the list
            self.tail = node.prev
            self.tail.next = None
            node = None
        else:  # delete node that is neither the head or tail of the list
            prev_node = node.prev
            next_node = node.next

            node = None

            prev_node.next = next_node
            next_node.prev = prev_node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        node = self.head
        greatestValue = node.value if node is not None else 0

        while node.next is not None:
            node = node.next

            if greatestValue < node.value:
                greatestValue = node.value

        return greatestValue
