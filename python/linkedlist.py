class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

    def display(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.value))
            curr = curr.next
        print(" -> ".join(vals))
