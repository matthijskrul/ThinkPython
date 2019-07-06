class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_list(node):
        while node is not None:
            print(node, end=" ")
            node = node.next
        print()

    def print_backward(list):
        if list is None: return
        head = list
        tail = list.next
        print_backward(tail)
        print(head, end=" ")

    def remove_second(list):
        if list is None: return
        first = list
        second = list.next
        # Make the first node refer to the third
        first.next = second.next
        # Separate the second node from the rest of the list
        second.next = None
        return second

    def print_backward_nicely(list):
        print("[", end=" ")
        print_backward(list)
        print("]")


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1