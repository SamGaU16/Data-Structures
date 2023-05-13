class Node:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.rank = 0
        self.disjoint = None
        self.degree = 0

class DisjointSet:
    def __init__(self, data):
        self.nodes = []
        new_node = Node(data)
        new_node.parent = new_node
        self.nodes.append(new_node)
        new_node.disjoint = self
    
    def find(self, pos):
        node = self.nodes[pos]
        if node != node.parent:
            node.parent = self.find(pos+1)
        return node.parent
    
    def union(self, set2):
        representative_N1 = self.find(0) 
        representative_N2 = set2.find(0)
        for node in set2.nodes:
            self.nodes.append(node)
        self.link(representative_N1,representative_N2)

    def link(self, Node1: Node, Node2: Node):
        Node1.degree +=1
        Node2.degree +=1
        if Node1.rank > Node2.rank:
            Node2.parent = Node1
        else:
            Node1.parent = Node2
            if Node1.rank == Node2.rank:
                Node2.rank += 1

