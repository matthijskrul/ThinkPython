# Reversing linked list.


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)


class SimpleLinkedList:
    def __init__(self, init_values=[]):
        self.length = 0
        self.head = None
        if len(init_values) > 0:
            for value in init_values:
                self.insert(value)

    def is_empty(self):
        return self.head == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.length += 1

    def remove(self):
        if self.head is None:
            return None
        else:
            top = self.head
            self.head = self.head.next
            self.length -= 1
            return top

    def reverse(self):
        previous = None
        current = self.head
        if self.head is None:
            return None
        while current.next:
            next = current.next
            current.next = previous
            previous = current
            current = next
        current.next = previous
        self.head = current


linked_list = SimpleLinkedList(init_values=[1, 2, 3, 4, 5])
linked_list.reverse()
