from SingleLinked import LinkedList

class Leaf:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.children = []
        self.rank = 0
        self.degree = 0

class Tree:
    def __init__(self, data=None):
        new_node = Leaf(data)
        new_node.parent = new_node
        
        self.root = new_node
        self.nodes = 1
    
    def degrees(self):
        return self.degreeRecursive(self.root, 0)

    def degreeRecursive(self, Node: Leaf, count: int):
        count += Node.degree
        if len(Node.children) == 0:
            return count
        for leaf in Node.children:
            count = self.degreeRecursive(leaf, count)
        return count


class DisjointSet:
    def __init__(self):
        self.forest = LinkedList()

    def makeSet(self,data=None):
        self.forest.appendLast(Tree(data))

    def find(self, pos: int):
        return self.forest.getNode(pos).data
    
    def union(self, pos1: int, pos2: int):
        if pos1 < 1:
            return
        set1 = self.find(pos1) 
        set2 = self.find(pos2)
        new_representative = self.link(set1.root, set2.root)
        set1.root = new_representative
        set1.nodes += set2.nodes
        self.forest.unlink(pos2)
        
    def link(self, Node1: Leaf, Node2: Leaf):
        Node1.degree +=1
        Node2.degree +=1
        if Node1.rank > Node2.rank:
            Node2.parent = Node1
            Node1.children.append(Node2)
            return Node1
        else:
            Node1.parent = Node2
            Node2.children.append(Node1)
            if Node1.rank == Node2.rank:
                Node2.rank += 1
            return Node2
    
    def size(self):
        return self.forest.size
    
    def leafsInfo(self):
        sizeTree = 0
        degreesLeafs = 0
        Node = self.forest.getNode(1)
        while Node is not None:
            Tree = Node.data
            sizeTree += Tree.nodes
            degreesLeafs += Tree.degrees()
            Node = Node.next
        return sizeTree, degreesLeafs