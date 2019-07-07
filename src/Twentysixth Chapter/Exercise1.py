# Write an implementation of the Queue ADT using a Python list.
# Compare the performance of this implementation to the ImprovedQueue for a range of queue lengths.


class ListQueue:
    def __init__(self):
        self.list = []

    def insert(self, cargo):
        self.list.append(cargo)

    def is_empty(self):
        return len(self.list) == 0

    def remove(self):
        if self.is_empty():
            return None
        listcargo = self.list[0]
        self.list.remove(self.list[0])
        return listcargo
