from Queue import Queue
from Stack import Stack
from DisjointSet_LinkedList import DisjointSet_L
from DisjointSet_Forest import DisjointSet
import random
import copy

N=100000 #Número de operaciones
# random.seed() 

def queueF(parameter):
    operation_data = []
    size_data = []
    ds = Queue(parameter)
    for i in range(1, N+1):
        operation = random.randint(0, 1)
        if operation == 0:
                ds.dequeue()
        else:
            ds.enqueue('new')
        operation_data.append(i)
        size_data.append(ds.size())

    return operation_data, size_data        

def stackF(parameter):
    operation_data = []
    size_data = []
    ds = Stack(parameter)
    for i in range(1, N+1):
        operation = random.randint(0, 1)
        if operation == 0:
            ds.pop()
        else:
            ds.push('new')
        operation_data.append(i)
        size_data.append(ds.size())
    return operation_data, size_data        

def disjointSet_LinkedListF(parameter):
    operation_data = []
    connectance_data = []
    sets = []

    for i in range(parameter):
        ds = DisjointSet_L(i)
        sets.append(ds)

    j= 1
    for i in range(1, N+1):
        x = random.randint(0, parameter-j)
        y = random.randint(0, parameter-j)
        
        if x!=y:
            x_copy = copy.deepcopy(sets[x])
            y_copy = copy.deepcopy(sets[y])
            x_copy.union(y_copy)
            sets[x] = x_copy
            sets.pop(y)
            j +=1

        operation_data.append(i)
        connectance = 1 - (len(sets)/parameter)**2
        connectance_data.append(connectance)
        
    return operation_data, connectance_data
    

def disjointSet_LinkedForestF(parameter):
    ds = DisjointSet(parameter)