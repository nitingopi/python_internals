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
            self.tail = None 

        else:
            current = self.head
            while current.tail is not None:
                current = current.next
            current.next = new_node
            

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.value) 
            current = current.next

ll = LinkedList()
ll.add_to_back(2)
ll.add_to_back(3)
ll.print_forward()                     

