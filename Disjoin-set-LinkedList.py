class Node:
    def __init__(self, data=None, next=None, disjoint=None):
        self.data = data
        self.next = next
        self.disjoint = disjoint

class DisjointSet:
    def __init__(self, data):
        new_node = Node(data=data)
        self.head = new_node
        self.tail = new_node
        new_node.disjoint = self
    
    def find(self, node: Node)->Node:
        return node.disjoint.head
    
    def union(self, Node1: Node, Node2: Node):
        Head1 = self.find(Node1)
        Head2 = self.find(Node2)
        union_node = Head1.disjoint.tail
        union_node.next = Head2
        last_node = self.replace_set(self, Head1.head, Head2.head)
        Head1.disjoint.tail = last_node

    def replace_set(self, new_head: Node, node: Node):
        node.disjoint = new_head.disjoint
        if node.next:
            self.replace_set(new_head, node.next)
        else:
            return node
        