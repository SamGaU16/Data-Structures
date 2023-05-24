from Stack import Stack
from DisjointSet_LinkedList import DisjointSet_L
from DisjointSet import DisjointSet
import random

Nmod = 3000 #Número de operaciones
N = 5000

# ==============================
# Funciones Semillas de Forests
# ==============================

def RandomForestG(size: int, type=DisjointSet):
    Forest = type()
    Guard = True
    count = 0
    i = 0
    while Guard:
        operation = random.randint(0, 1)
        if operation == 0:
            Forest.makeSet(i)
            count += 1

        elif operation==1:
            x,y = randomXY(Forest.size())
            Forest.union(x,y)
        
        if count == size:
            Guard = False

        i+=1
        
    return Forest

def SimpleForestG(size: int, type=DisjointSet):
    Forest = type()
    for i in range(size):
        Forest.makeSet(i)        

    return Forest

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
    if range <= 1:
        return 0,0
    x = random.randint(1, range)
    y = random.randint(1, range)
    if x != y:
        return x,y
    else:
        return randomXY(range)
    
def WeightedValue(data: list, weights: list):
    upper = 0
    for i in range(len(data)):
        upper += data[i]*weights[i]
    return upper / sum(weights)

# ==================
# Funciones ForestLL
# ==================

def ForestLLOperation(parameter: int, limit: int, max_value: int):
    connectance_data = []

    make_count = 0
    union_count = 0

    Forest = SimpleForestG(parameter,type=DisjointSet_L)

    for i in range(N):
        operation = random.randint(1, max_value)
        if limit < operation:
            Forest.makeSet(i)
            make_count +=1

        if operation <= limit:
            x,y = randomXY(Forest.size())
            Forest.union(x,y)
            union_count +=1
        
        if i == N-1:
            relation = make_count/union_count

        nodes = Forest.nodes()
        connectance_data.append(nodes/Forest.size())
        
    return relation, connectance_data

def ForestLLIteration(Values:list ,Nseeds: list):
    avg_relation_data = []
    avg_size_data = []
    size_all_data = []
    relation_all_data = []
    all_data = []
    for value in Values:
        relation_data = []
        last_points = []
        weight_data = []
        pos_data = []
        
        for seed in Nseeds:
            relation, point_data = ForestLLOperation(seed, 10,round(value*10)+10)
            if value != relation:
                weight = 1/abs(value-relation)
            else:
                weight = 10**4
            relation_data.append(relation)
            last_points.append(point_data[-1])
            weight_data.append(weight)
            pos_data.append(point_data)

        average_relation = WeightedValue(relation_data, weight_data)
        average_size = WeightedValue(last_points, weight_data)

        avg_relation_data.append(average_relation)
        avg_size_data.append(average_size)
        size_all_data.append(last_points)
        relation_all_data.append(relation_data)
        all_data.append(pos_data)

    norm_avg_size_data = [float(i)/max(avg_size_data) for i in avg_size_data]

    return avg_relation_data, norm_avg_size_data, size_all_data, relation_all_data, all_data

# ================
# Funciones Forest
# ================

def ForestDebug(parameter, limit=1.1):
    operation_data = []
    connectance_data = []
    degree_data = []

    operation2_data = []
    connectance2_data = []
    degree2_data = []

    make_count = 0
    union_count = 0

    Forest = RandomForestG(parameter)

    for i in range(Nmod):
        Forest.makeSet(i)
        make_count += 1

    for i in range(Nmod):
        x,y = randomXY(Forest.size())
        Forest.union(x,y)
        union_count +=1
        relation = make_count/union_count
        if round(relation,1) <= limit:
            sizeTrees, degreeLeafs = Forest.leafsInfo()
            operation_data.append(relation)
            connectance_data.append(sizeTrees/Forest.size())
            degree_data.append(degreeLeafs/sizeTrees)

    for i in range(Nmod):
        Forest.makeSet(i)
        make_count += 1
        relation = make_count/union_count
        if round(relation,1) <= limit:
            sizeTrees, degreeLeafs = Forest.leafsInfo()
            operation2_data.append(relation)
            connectance2_data.append(sizeTrees/Forest.size())
            degree2_data.append(degreeLeafs/sizeTrees)

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
    norm_connectance2_data = [float(i)/max(connectance2_data) for i in connectance2_data]
        
    return operation_data, norm_connectance_data, degree_data, operation2_data, norm_connectance2_data, degree2_data

def ForestOperation(parameter:int, limit: int, max_value: int):
    connectance_data = []
    degree_data = []

    make_count = 0
    union_count = 0

    Forest = SimpleForestG(parameter)

    for i in range(N):
        operation = random.randint(1, max_value)
        if limit < operation :
            Forest.makeSet(i)
            make_count +=1

        if operation <= limit:
            x,y = randomXY(Forest.size())
            Forest.union(x,y)
            union_count +=1
        
        if i == N-1:
            relation = make_count/union_count
        
        sizeTrees, degreeLeafs = Forest.leafsInfo()
        connectance_data.append(sizeTrees/Forest.size())
        degree_data.append(degreeLeafs/sizeTrees)

    return relation, connectance_data, degree_data

def ForestIteration(Values:list, Nseeds: list):
    avg_relation_data = []
    avg_size_data = []
    avg_degree_data = []
    size_all_data = []
    relation_all_data = []
    all_data = []
    for value in Values:
        relation_data = []
        last_points_c = []
        last_points_d = []
        weight_data = []
        pos_data = []

        for seed in Nseeds:
            relation, point_data, degree_data = ForestOperation(seed, 10,round(value*10)+10)
            if value != relation:
                weight = 1/abs(value-relation)
            else:
                weight = 10**4
            relation_data.append(relation)
            last_points_c.append(point_data[-1])
            last_points_d.append(degree_data[-1])
            weight_data.append(weight)
            pos_data.append(point_data)

        average_relation = WeightedValue(relation_data, weight_data)
        average_size = WeightedValue(last_points_c, weight_data)
        average_degree = WeightedValue(last_points_d, weight_data)

        avg_relation_data.append(average_relation)
        avg_size_data.append(average_size)
        avg_degree_data.append(average_degree)
        size_all_data.append(last_points_c)
        relation_all_data.append(relation_data)
        all_data.append(pos_data)

    norm_avg_size_data = [float(i)/max(avg_size_data) for i in avg_size_data]
    norm_avg_degree_data = [float(i)/max(avg_degree_data) for i in avg_degree_data]

    return avg_relation_data, norm_avg_size_data, norm_avg_degree_data, size_all_data, relation_all_data, all_data

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

def WarehouseIteration(Values:list, Nseeds: list):
    avg_relation_data = []
    avg_height_data = []
    size_all_data = []
    relation_all_data = []
    all_data = []
    for value in Values:
        relation_data = []
        height_data = []
        weight_data = []
        pos_data = []
        
        for seed in Nseeds:
            relation, height_points = ForestLLOperation(seed, 10,round(value*10)+10)
            if value != relation:
                weight = 1/abs(value-relation)
            else:
                weight = 10**4
                
            relation_data.append(relation)
            height_data.append(height_points[-1])
            weight_data.append(weight)
            pos_data.append(height_points)

        average_relation = WeightedValue(relation_data, weight_data)
        average_height = WeightedValue(height_data, weight_data)
    
        avg_relation_data.append(average_relation)
        avg_height_data.append(average_height)
        size_all_data.append(height_data)
        relation_all_data.append(relation_data)
        all_data.append(pos_data)

    norm_avg_height_data = [float(i)/max(avg_height_data) for i in avg_height_data]

    return avg_relation_data, norm_avg_height_data, size_all_data, relation_all_data, all_data