# Write an implementation of the Priority Queue ADT using a linked list.
# You should keep the list sorted so that removal is a constant time operation.
# Compare the performance of this implementation with the Python list implementation.


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)


class PriorityLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.head == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            self.head = node
        elif self.head.next is None:
            if self.head.cargo < node.cargo:
                node.next = self.head
                self.head = node
            else:
                self.head.next = node
        else:
            last = self.head
            while last.next is not None:
                if last.next.cargo > node.cargo:
                    last = last.next
                else:
                    node.next = last.next
                    last.next = node
                    break
        self.length += 1

    def remove(self):
        if self.head is None:
            return None
        else:
            optimum = self.head
            self.head = self.head.next
            return optimum


linked = PriorityLinkedList()
linked.insert(10)
linked.insert(2)
linked.insert(3)
linked.insert(7)
linked.insert(2)