from Queue import Queue
from Stack import Stack
from DisjointSet_LinkedList import DisjointSet_L
from DisjointSet import DisjointSet
import random
import copy

N=4000 #Número de operaciones

def queueF(parameter): #No usada
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

def ForestLLPT(parameter):
    operation_data = []
    connectance_data = []
    forest = []

    for i in range(parameter):
        ds = DisjointSet_L(i)
        forest.append(ds)

    copy_sets = copy.copy(forest)

    for i in range(1, 2*parameter):
        if 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
        if 1 <= round(parameter/i,1) and round(parameter/i,1) <= 1.1:
            size = 0
            for disjoint in copy_sets:
                size += disjoint.size
            operation_data.append(parameter/i)
            connectance_data.append(size/len(copy_sets))

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
        
    return operation_data, norm_connectance_data

def randomXY(range):
    x = random.randint(0, range)
    y = random.randint(0, range)
    if x != y:
        return x,y
    else:
        return randomXY(range)
    
def union_op(sets,x,y):
    sets[x].union(sets[y])
    sets.pop(y)

def ForestLLR():
    make_count = 0
    union_count = 0
    operation_data = []
    connectance_data = []
    forest = []
    copy_sets = []

    for i in range(10):
        operation = random.randint(0, 1)
        if operation == 0:
            ds = DisjointSet_L(i)
            forest.append(ds)
            copy_sets.append(copy.copy(ds))
            make_count +=1

        if operation ==1 and 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            union_count +=1

    for i in range(10,N+10):
        operation = random.randint(0, 1)
        if operation == 0:
            ds = DisjointSet_L(i)
            forest.append(ds)
            copy_sets.append(copy.copy(ds))
            make_count +=1

        if operation ==1 and 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            union_count +=1
            relation = make_count/union_count
            if round(relation,1) <= 1.1:
                size = 0
                for disjoint in copy_sets:
                    size += disjoint.size
                operation_data.append(relation)
                connectance_data.append(size/len(copy_sets))

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
        
    return operation_data, norm_connectance_data

def ForestPT(parameter):
    operation_data = []
    connectance_data = []
    degree_data = []
    forest = []

    for i in range(parameter):
        ds = DisjointSet(i)
        forest.append(ds)

    copy_sets = copy.copy(forest)

    for i in range(1, 2*parameter):
        if 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
        if 1 <= round(parameter/i,1) and round(parameter/i,1) <= 10:
            size = 0
            degree  = 0
            for disjoint in copy_sets:
                size += len(disjoint.nodes)
                for node in disjoint.nodes:
                    degree += node.sons
            operation_data.append(parameter/i)
            connectance_data.append(size/len(copy_sets))
            degree_data.append(degree/size)

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
        
    return operation_data, norm_connectance_data, degree_data

def ForestR():
    make_count = 0
    union_count = 0
    operation_data = []
    connectance_data = []
    degree_data = []
    forest = []
    copy_sets = []

    for i in range(10):
        operation = random.randint(0, 1)
        if operation == 0:
            ds = DisjointSet(i)
            forest.append(ds)
            copy_sets.append(copy.copy(ds))
            make_count +=1

        if operation ==1 and 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            union_count +=1

    for i in range(10,N+10):
        operation = random.randint(0, 1)
        if operation == 0:
            ds = DisjointSet(i)
            forest.append(ds)
            copy_sets.append(copy.copy(ds))
            make_count +=1

        if operation ==1 and 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            union_count +=1
            relation = make_count/union_count
            if round(relation,1) <= 5:
                size = 0
                degree = 0
                for disjoint in copy_sets:
                    size += len(disjoint.nodes)
                    for node in disjoint.nodes:
                        degree += node.sons
                operation_data.append(relation)
                connectance_data.append(size/len(copy_sets))
                degree_data.append(degree/size)
        
    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]

    return operation_data, norm_connectance_data, degree_data

def Warehouse(parameter):
    operation_data = []
    size_data = []
    Warehouse = []
    pop = 0
    push = 0
    counter = 0
    i = 0
    while i<parameter:
        randomizer = random.randint(1, parameter-counter)
        ds = Stack(randomizer)
        counter += randomizer
        Warehouse.append(ds)
        i+=1
    
    i=0
    while i<10:
        pos_stack = random.randint(0, len(Warehouse)-1)
        operation = random.randint(0, 1)
        if operation == 0:
            Warehouse[pos_stack].pop()
            pop += 1
        else:
            Warehouse[pos_stack].push('new')
            push += 1
        i+=1
    
    i = 0
    while i<N:
        pos_stack = random.randint(0, len(Warehouse)-1)
        operation = random.randint(0, 1)
        if operation == 0:
            Warehouse[pos_stack].pop()
            pop += 1
        else:
            Warehouse[pos_stack].push('new')
            push += 1

        relation = pop/push
        if True: #round(relation,1) <= 1.1
            height = 0
            for stack in Warehouse:
                height += stack.count
            Warehouse_size = height/len(Warehouse)
            operation_data.append(relation)
            size_data.append(Warehouse_size)
        i+=1

    return operation_data, size_data