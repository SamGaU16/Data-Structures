class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def appendLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        present_node = self.head
        while present_node.next is not None:
            present_node = present_node.next
        present_node.next = new_node

    def appendFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        present_node = self.head
        while present_node.next is not None:
            if present_node.next.data == data:
                present_node.next = present_node.next.next
                return
            present_node = present_node.next

    def print_list(self):
        present_node = self.head
        while present_node is not None:
            print(present_node.data)
            present_node = present_node.next