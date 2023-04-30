class Node:
    def __init__(self, data, down=None):
        self.data = data
        self.down = down

class Queue:
    def __init__(self, size):
        self.ceil = None
        self.floor = None
        self.count = 0
        for  i in range(1, size+1):
            self.enqueue(i)

    def is_empty(self):
        return self.ceil == None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
           self.ceil = new_node
           self.floor = new_node
        else:
            self.floor.down = new_node
            self.floor = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dequeue_node = self.ceil
        if self.ceil.down:
            self.ceil = self.ceil.down
        else:
            self.ceil = None
            self.floor = None
        self.count -= 1
        return dequeue_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue vacío - Error peek")
        return self.ceil.data

    def size(self):
        return self.count