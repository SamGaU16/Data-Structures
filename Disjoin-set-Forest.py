class Node:
    def __init__(self, data=None):
        self.data = data
        self.parent = data
        self.rank = 0
        self.disjoint = None

class DisjointSet:
    def __init__(self, data):
        self.nodes = [Node]
        new_node = Node(data=data)
        new_node.parent = data
        self.nodes.append(new_node)
        new_node.disjoint = self
    
    def find(self, node: Node):
        if node != node.parent:
            node.parent = self.find(node.parent)
        return node.parent
    
    def union(self, Node1: Node, Node2: Node):
        representative_N1 = self.find(Node1) 
        representative_N2 = self.find(Node2)
        self.link(representative_N1,representative_N2)

    def link(self, Node1: Node, Node2: Node):
        if Node1.rank > Node2.rank:
            Node2.parent = Node1
        else:
            Node1.parent = Node2
            if Node1.rank == Node2.rank:
                Node2.rank += 1

