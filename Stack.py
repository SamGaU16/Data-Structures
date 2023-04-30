class Node:
    def __init__(self, data, down=None):
        self.data = data
        self.down = down

class Stack:
    def __init__(self, size):
        self.top = None
        self.count = 0
        for i in range(1,size+1):
            self.push(i)

    def is_empty(self):
        return self.top == None

    def push(self, data):
        new_node = Node(data)
        if not self.is_empty() :
            new_node.down = self.top            
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return None
        pop_node = self.top
        self.top = pop_node.down
        self.count -= 1
        return pop_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack vacío - Error peek")
        return self.top.data

    def size(self):
        return self.count