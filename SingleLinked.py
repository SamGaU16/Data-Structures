class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def appendLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        present_node = self.head
        while present_node.next is not None:
            present_node = present_node.next
        present_node.next = new_node
        self.size +=1

    def getNode(self,pos: int):
        if pos > self.size:
            return None
        i = 1
        present_node = self.head
        while i < pos:
            present_node = present_node.next
            i +=1
        return present_node

    def unlink(self, pos):
        if self.head is None:
            return
        present_node = self.head
        self.size -= 1

        if pos == 1:
            self.head = present_node.next
            return
        
        i = 2
        while i < pos:
            present_node = present_node.next
            i +=1
        unlink_node = present_node.next
        present_node.next = unlink_node.next