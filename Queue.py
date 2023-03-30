class Node:
    def __init__(self, data=None, down=None, up=None):
        self.data = data
        self.up = up
        self.down = down

class Queue:
    def __init__(self):
        self.ceil = None
        self.floor = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data):
        new_node = Node(data)
        if not self.is_empty:
            self.floor.down = new_node
        self.floor = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue vacío - Error dequeue")
        dequeue_node = self.ceil
        self.ceil = self.ceil.down
        self.count -= 1
        return dequeue_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue vacío - Error peek")
        return self.ceil.data

    def size(self):
        return self.count