class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_back(self, value):
        new_node = Node(value)
        if None is self.head:
            self.head = new_node
            self.tail = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.tail = current.next
            

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.value) 
            current = current.next

ll = LinkedList()
ll.add_to_back(2)
ll.add_to_back(3)
ll.add_to_back(4)
ll.add_to_back(5)

ll.print_forward()                     

