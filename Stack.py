class Stack:
    def __init__(self):
        self.model = []

    def is_empty(self):
        return self.model == []

    def push(self, data):
        self.model.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack vacío - Error pop")
        return self.model.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack vacío - Error peek")
        return self.model[-1]

    def size(self):
        return len(self.model)