class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.size = size

    def find(self, i): #GeeksforGeeks
        if self.parent[i] == i:
            return i
        else:
            return self.find(self.parent[i])

    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if parent_i == parent_j:
            return
        if self.rank[parent_i] < self.rank[parent_j]:
            self.parent[parent_i] = parent_j
        elif self.rank[parent_i] > self.rank[parent_j]:
            self.parent[parent_j] = parent_i
        else:
            self.parent[parent_i] = parent_j
            self.rank[parent_j] += 1

    def connected_to_G(self, i):
        parent_i = self.find(i)
        total = 0
        for j in range(self.size):
            if self.find(j) == parent_i:
                total += 1
        return total

# Ej:
ds = DisjointSet(10)

ds.union(0, 1)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(8, 9)
ds.union(1, 3)
ds.union(5, 7)
ds.union(9, 8)

# Encontrar el padre de 1, el cual es 3
parent_1 = ds.find(1)
print("El padre de 1 es:", parent_1)

# Encontrar el padre de 9, el cual es 9
parent_9 = ds.find(9)
print("El padre de 9 es:", parent_9)

# Conectividad de 0, el cual es 4
print("Componentes conectados a 0:", ds.connected_to_G(0))
