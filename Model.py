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

def RandomWarehouseG(size: int):
    Warehouse = []
    count = 0
    Guard = True

    while Guard:
        if count < size:
            randomizer = random.randint(1, size-count)
        else:
            randomizer = 0

        ds = Stack(randomizer)
        count += randomizer
        Warehouse.append(ds)

        if len(Warehouse) == size:
            Guard = False

    return Warehouse

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

def WeightedValue(data: list, weights: list):
    upper = 0
    for i in range(len(data)):
        upper += data[i]*weights[i]
    return upper / sum(weights)

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

    for i in range(N):
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
        
        if i == N-1:
            relation = make_count/union_count

        size = 0
        for disjoint in copy_sets:
            size += disjoint.size
        connectance_data.append(size/len(copy_sets))

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
        
    return relation, norm_connectance_data

def ForestLLIteration(parameter: int, Nseeds=10):
    avg_relation_data = []
    avg_size_data = []
    for i in range(10,20):
        central_point = round(i/10,1)
        relation_data = []
        last_points = []
        weight_data = []
        fig, ax = plt.subplots()
        
        for j in range(Nseeds):
            relation, point_data = ForestLLOperation(parameter, 10,i+10)
            if central_point != relation:
                weight = 1/abs(central_point-relation)
            else:
                weight = 10**4
            relation_data.append(relation)
            last_points.append(point_data[-1])
            weight_data.append(weight)
            ax.plot(point_data, label=j)

        plt.legend(loc='upper right')
        plt.show()

        average_relation = WeightedValue(relation_data, weight_data)
        average_size = WeightedValue(last_points, weight_data)

        avg_relation_data.append(average_relation)
        avg_size_data.append(average_size)

    return avg_relation_data, avg_size_data   

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

    for i in range(N):
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
        
        size = 0
        degree = 0
        for disjoint in copy_sets:
            size += len(disjoint.nodes)
            for node in disjoint.nodes:
                degree += node.degree
        connectance_data.append(size/len(copy_sets))
        degree_data.append(degree/size)
        
    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]

    return relation, norm_connectance_data, degree_data

def ForestIteration(parameter: int, Nseeds=10):
    avg_relation_data = []
    avg_size_data = []
    avg_degree_data = []
    for i in range(10,21):
        central_point = round(i/10,1)
        relation_data = []
        last_points_c = []
        last_points_d = []
        weight_data = []
        fig, ax = plt.subplots()

        for j in range(Nseeds):
            relation, point_data, degree_data = ForestOperation(parameter, 10,i+10)
            if central_point != relation:
                weight = 1/abs(central_point-relation)
            else:
                weight = 10**4
            relation_data.append(relation)
            last_points_c.append(point_data[-1])
            last_points_d.append(degree_data[-1])
            weight_data.append(weight)
            ax.plot(point_data, label=j)

        ax.legend(loc='upper right')
        plt.show()

        average_relation = WeightedValue(relation_data, weight_data)
        average_size = WeightedValue(last_points_c, weight_data)
        average_degree = WeightedValue(last_points_d, weight_data)

        avg_relation_data.append(average_relation)
        avg_size_data.append(average_size)
        avg_degree_data.append(average_degree)

    return avg_relation_data, avg_size_data, avg_degree_data

# ===================
# Funciones Warehouse
# ===================

def WarehouseOperation(parameter: int, limit: int, max_value: int):
    height_data = []

    pop = 0
    push = 0

    Warehouse = RandomWarehouseG(parameter)

    for i in range(N):
        pos_stack = random.randint(0, len(Warehouse)-1)
        operation = random.randint(1, max_value)
        if limit < operation:
            Warehouse[pos_stack].pop()
            pop += 1
        else:
            Warehouse[pos_stack].push(i)
            push += 1

        if i == N-1:
            relation = pop/push
        height = 0
        for stack in Warehouse:
            height += stack.count
        Warehouse_size = height/len(Warehouse)
        height_data.append(Warehouse_size)

    return relation, height_data

def WarehouseIteration(parameter: int, Nseeds=10):
    avg_relation_data = []
    avg_height_data = []
    for i in range(1,21):
        central_point = round(i/10,1)
        relation_data = []
        height_data = []
        weight_data = []
        fig, ax = plt.subplots()
        
        for j in range(Nseeds):
            relation, height_points = ForestLLOperation(parameter, 10,i+10)
            if central_point != relation:
                weight = 1/abs(central_point-relation)
            else:
                weight = 10**4
                
            relation_data.append(relation)
            height_data.append(height_points[-1])
            weight_data.append(weight)

            ax.plot(height_points, label=j)

        plt.legend(loc='upper right')
        plt.show()

        average_relation = WeightedValue(relation_data, weight_data)
        average_height = WeightedValue(height_points, weight_data)

        avg_relation_data.append(average_relation)
        avg_height_data.append(average_height)

    return avg_relation_data, avg_height_data 