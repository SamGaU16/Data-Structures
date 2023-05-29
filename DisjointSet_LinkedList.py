from SingleLinked import LinkedList

class SNode:
    def __init__(self, data, next=None, lst=None):
        self.data = data
        self.next = next
        self.lst = lst

class SList:
    def __init__(self, data):
        new_node = SNode(data)
        self.head = new_node
        self.tail = new_node
        self.size = 1
        new_node.lst = self
        
class DisjointSet_L:
    def __init__(self):
        self.forest = LinkedList()
        self.nodes = 0

    def makeSet(self,data=None):
        self.forest.appendLast(SList(data))
        self.nodes +=1

    def find(self, pos: int):
        return self.forest.getNode(pos).data
    
    def union(self, pos1: int, pos2: int):
        if pos1 < 1:
            return
        set1 = self.find(pos1) 
        set2 = self.find(pos2)
        union_node = set1.tail
        union_node.next = set2.head
        last_node = self.replace_set(set1, set2.head)
        set1.tail = last_node
        self.forest.unlink(pos2)

    def replace_set(self, set: SList, node: SNode):
        node.lst = set
        set.size += 1
        if node.next: 
            return self.replace_set(set, node.next)
        else:
            return node
    
    def size(self):
        return self.forest.size