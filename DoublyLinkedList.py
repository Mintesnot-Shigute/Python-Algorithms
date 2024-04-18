class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
            new_node.prev_node = current_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev_node:
                    current_node.prev_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node

                if current_node.next_node:
                    current_node.next_node.prev_node = current_node.prev_node

                return  

            current_node = current_node.next_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next_node
        print("None")


# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.display()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None

dll.delete(2)
dll.display()  # Output: 0 <-> 1 <-> 3 <-> None
