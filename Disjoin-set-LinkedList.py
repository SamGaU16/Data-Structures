class Node:
    def __init__(self, data=None, next=None, head=None):
        self.data = data
        self.next = next
        self.head = head

class LinkedList:
    def __init__(self, data):
        new_node = Node(data=data)
        self.head = new_node
        self.tail = new_node

    def find(self):
        return self.head

    def union(self, set1, set2):
        #Por implementar x agrega a y
        return

    def print_list(self):
        present_node = self.head
        while present_node is not None:
            print(present_node.data)
            present_node = present_node.next