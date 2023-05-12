class Node:
    def __init__(self, data, next=None, disjoint=None):
        self.data = data
        self.next = next
        self.disjoint = disjoint

class DisjointSet_L:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.size = 1
        new_node.disjoint = self
    
    def union(self, set2):
        union_node = self.tail
        union_node.next = set2.head                                                                                                                                                                                     
        last_node = self.replace_set(set2.head)
        self.tail = last_node

    def replace_set(self, node: Node):
        node.disjoint = self
        self.size += 1
        if node.next: 
            return self.replace_set(node.next)
        else:
            return node