from Stack import Stack
from DisjointSet_LinkedList import DisjointSet_L
from DisjointSet import DisjointSet
import random
import copy

import matplotlib.pyplot as plt

Nmod = 3000 #Número de operaciones
N = 4000

# ==============================
# Funciones Semillas de Forests
# ==============================

def RandomForestG(size: int, type=DisjointSet_L):
    forest = []
    copy_sets = []
    Guard = True
    count = 0
    while Guard:
        operation = random.randint(0, 1)
        if operation == 0:
            ds = type('Base')
            forest.append(ds)
            copy_sets.append(copy.copy(ds))
            count += 1

        elif operation==1 and 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
        
        if count == size:
            Guard = False
        
    return copy_sets

# ===================
# Funciones de Apoyo
# ===================

def randomXY(range: int):
    x = random.randint(0, range)
    y = random.randint(0, range)
    if x != y:
        return x,y
    else:
        return randomXY(range)
    
def union_op(sets: list, x: int, y: int):
    sets[x].union(sets[y])
    sets.pop(y)

def Mean(lst: list):
    return sum(lst) / len(lst)

# ==================
# Funciones ForestLL
# ==================

def ForestLLD(parameter: int, limit =1.1):
    operation_data = []
    connectance_data = []
    operation2_data = []
    connectance2_data = []

    make_count = 0
    join_count = 0

    forest = RandomForestG(parameter)

    for i in range(Nmod):
        ds = DisjointSet_L(i)
        forest.append(ds)
        make_count +=1

    copy_sets = copy.copy(forest)

    for i in range(Nmod):
        if 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            join_count +=1
        relation = make_count/join_count
        if round(relation,1) <= limit:
            size = 0
            for disjoint in copy_sets:
                size += disjoint.size
            operation_data.append(relation)
            connectance_data.append(size/len(copy_sets))

    for i in range(Nmod):
        ds = DisjointSet_L(i)
        copy_sets.append(ds)
        make_count +=1
        relation = make_count/join_count
        if round(relation,1) <= limit:
            size = 0
            for disjoint in copy_sets:
                size += disjoint.size
            operation2_data.append(relation)
            connectance2_data.append(size/len(copy_sets))

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
    norm_connectance2_data = [float(i)/max(connectance2_data) for i in connectance2_data]
        
    return operation_data, norm_connectance_data, operation2_data, norm_connectance2_data

def ForestLLOperation(parameter: int, limit: int, max_value: int):
    connectance_data = []

    make_count = 0
    union_count = 0

    forest = RandomForestG(parameter)
    copy_sets = copy.copy(forest)

    for i in range(1,N+1):
        operation = random.randint(1, max_value)
        if limit < operation:
            ds = DisjointSet_L(i)
            forest.append(ds)
            copy_sets.append(copy.copy(ds))
            make_count +=1

        if operation <= limit and 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            union_count +=1
        
        if i==N-1:
            relation = make_count/union_count
            print(relation)

        size = 0
        for disjoint in copy_sets:
            size += disjoint.size
        connectance_data.append(size/len(copy_sets))

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
        
    return norm_connectance_data

def ForestLLIteration(parameter: int, Nseeds=10):
    relation = []
    data = []
    for i in range(10,20):
        last_points = []
        fig, ax = plt.subplots()
        
        for j in range(Nseeds):
            point_data = ForestLLOperation(parameter, 10,i+10)
            ax.plot(point_data, label=j)
            last_points.append(point_data[-1])

        plt.legend(loc='upper right')
        plt.show()

        average_size = Mean(last_points)
        relation.append(round(i/10,1))
        data.append(average_size)

    return relation, data

# ================
# Funciones Forest
# ================

def ForestD(parameter, limit=1.1):
    operation_data = []
    connectance_data = []
    degree_data = []
    operation2_data = []
    connectance2_data = []
    degree2_data = []
    make_count = 0
    join_count = 0

    forest = RandomForestG(parameter, type=DisjointSet)

    for i in range(Nmod):
        ds = DisjointSet(i)
        forest.append(ds)
        make_count += 1

    copy_sets = copy.copy(forest)

    for i in range(Nmod):
        if 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            join_count +=1
        relation = make_count/join_count
        if round(relation,1) <= limit:
            size = 0
            degree  = 0
            for disjoint in copy_sets:
                size += len(disjoint.nodes)
                for node in disjoint.nodes:
                    degree += node.degree
            operation_data.append(relation)
            connectance_data.append(size/len(copy_sets))
            degree_data.append(degree/size)

    for i in range(Nmod):
        ds = DisjointSet(i)
        copy_sets.append(ds)
        make_count +=1
        relation = make_count/join_count
        if round(relation,1) <= limit:
            size = 0
            degree  = 0
            for disjoint in copy_sets:
                size += len(disjoint.nodes)
                for node in disjoint.nodes:
                    degree += node.degree
            operation2_data.append(relation)
            connectance2_data.append(size/len(copy_sets))
            degree2_data.append(degree/size)

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
    norm_connectance2_data = [float(i)/max(connectance2_data) for i in connectance2_data]
        
    return operation_data, norm_connectance_data, degree_data, operation2_data, norm_connectance2_data, degree2_data

def ForestOperation(parameter:int, limit: int, max_value: int):
    connectance_data = []
    degree_data = []

    make_count = 0
    union_count = 0

    forest = RandomForestG(parameter, type=DisjointSet)
    copy_sets = copy.copy(forest)

    for i in range(1,N+1):
        operation = random.randint(1, max_value)
        if limit < operation :
            ds = DisjointSet(i)
            forest.append(ds)
            copy_sets.append(copy.copy(ds))
            make_count +=1

        if operation <= limit and 1<len(copy_sets):
            x,y = randomXY(len(copy_sets)-1)
            union_op(copy_sets,x,y)
            union_count +=1
        
        if i == N-1:
            relation = make_count/union_count
            print(relation)
        
        size = 0
        degree = 0
        for disjoint in copy_sets:
            size += len(disjoint.nodes)
            for node in disjoint.nodes:
                degree += node.degree
        connectance_data.append(size/len(copy_sets))
        degree_data.append(degree/size)
        
    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]

    return norm_connectance_data, degree_data

def ForestIteration(parameter: int, Nseeds=10):
    relation = []
    c_data = []
    d_data = []
    for i in range(10,21):
        last_points_c = []
        last_points_d = []
        fig, ax = plt.subplots()

        for j in range(Nseeds):
            point_data, degree_data = ForestOperation(parameter, 10,i+10)
            ax.plot(point_data, label=j)
            last_points_c.append(point_data[-1])
            last_points_d.append(degree_data[-1])

        ax.legend(loc='upper right')
        plt.show()

        average_size_c = Mean(last_points_c)
        average_size_d = Mean(last_points_d)
        relation.append(round(i/10,1))
        c_data.append(average_size_c)
        d_data.append(average_size_d)

    return relation, c_data, d_data

# ===================
# Funciones Warehouse
# ===================

def Warehouse(parameter):
    operation_data = []
    size_data = []
    Warehouse = []
    pop = 0
    push = 0
    counter = 0
    i = 0
    while i<parameter:
        if counter < parameter:
            randomizer = random.randint(1, parameter-counter)
        else:
            randomizer = 0
        ds = Stack(randomizer)
        counter += randomizer
        Warehouse.append(ds)
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

        if push != 0: 
            relation = pop/push
            height = 0
            for stack in Warehouse:
                height += stack.count
            Warehouse_size = height/len(Warehouse)
            operation_data.append(relation)
            size_data.append(Warehouse_size)
        i+=1

    return operation_data, size_data