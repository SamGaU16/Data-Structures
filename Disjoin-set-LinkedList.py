class Node:
    def __init__(self, data=None, next=None, head=None):
        self.data = data
        self.next = next
        self.head = head

class DisjointSet:
    def __init__(self, data):
        new_node = Node(data=data)
        self.head = new_node
        self.tail = new_node

class AllSets:
    def __init__(self):
        self.sets = [DisjointSet]

    def make_set(self, data):
        new_set = DisjointSet(data)
        self.sets.append(new_set)
    
    def find(self, data):
        for i in range(len(self.sets)):
            set = self.sets[i]
            object = self.set_find(set.head, data)
            if object:
                return object  
        return None

    def set_find(self, node: Node, data):
        if node.data == data:
            return node
        else:
            self.set_find(node.next, data)

    def union(self, set1: DisjointSet, set2: DisjointSet):
        union_node = set1.tail
        union_node.next = set2.head
        last_node = self.replace_head(self, set1.head, set2.head)
        set1.tail = last_node

    def replace_head(self, new_head: Node, node: Node):
        node.head = new_head
        if node.next:
            self.replace_head(new_head, node.next)
        else:
            return node