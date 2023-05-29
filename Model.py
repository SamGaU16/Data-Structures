from Stack import Stack
from DisjointSet_LinkedList import DisjointSet_L
from DisjointSet import DisjointSet
import random

Nmod = 3000 #Número de operaciones
NWarehouse = 5000

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

def ForestLLOperation(parameter: int, iteration=1.1):
    union = int(iteration*parameter)
    relation_data = []
    connectance_data = []

    Forest = SimpleForestG(parameter,type=DisjointSet_L)

    for i in range(union):
        x,y = randomXY(Forest.size())
        Forest.union(x,y)
        relation = (i+1)/parameter

        nodes = Forest.nodes
        relation_data.append(relation)
        connectance_data.append(nodes/Forest.size())
    
    norm_connectance_data = [(i-min(connectance_data))/(max(connectance_data)-min(connectance_data))
                              for i in connectance_data]
        
    return relation_data, norm_connectance_data

def ForestLLIteration(Nseeds: list, N=100):
    all_relation_data = []
    all_size_data = []
    for seed in Nseeds:
        seed_size_data = []
        avg_size_data = []
        
        for i in range(N):
            relation_data, size_data = ForestLLOperation(seed)
            seed_size_data.append(size_data)
        
        for i in range(len(relation_data)):
            sum_size_data = 0 
            for j in range(N):
                sum_size_data += seed_size_data[j][i]
            avg_size_data.append(sum_size_data/N)
        
        all_relation_data.append(relation_data)
        all_size_data.append(avg_size_data)
    
    return all_relation_data, all_size_data

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
        relation = union_count/make_count
        if round(relation,1) <= limit:
            sizeTrees, degreeLeafs = Forest.leafsInfo()
            operation_data.append(relation)
            connectance_data.append(sizeTrees/Forest.size())
            degree_data.append(degreeLeafs/sizeTrees)

    for i in range(Nmod):
        Forest.makeSet(i)
        make_count += 1
        relation = union_count/make_count
        if round(relation,1) <= limit:
            sizeTrees, degreeLeafs = Forest.leafsInfo()
            operation2_data.append(relation)
            connectance2_data.append(sizeTrees/Forest.size())
            degree2_data.append(degreeLeafs/sizeTrees)

    norm_connectance_data = [float(i)/max(connectance_data) for i in connectance_data]
    norm_connectance2_data = [float(i)/max(connectance2_data) for i in connectance2_data]
        
    return operation_data, norm_connectance_data, degree_data, operation2_data, norm_connectance2_data, degree2_data

def ForestOperation(parameter:int, iteration=1.1):
    union = int(iteration*parameter)
    relation_data = []
    connectance_data = []
    degree_data = []

    Forest = SimpleForestG(parameter)

    for i in range(union):
        x,y = randomXY(Forest.size())
        Forest.union(x,y)

        relation = (i+1)/parameter
        sizeTrees, degreeLeafs = Forest.leafsInfo()

        relation_data.append(relation)
        connectance_data.append(sizeTrees/Forest.size())
        degree_data.append(degreeLeafs/sizeTrees)

    norm_connectance_data = [(i-min(connectance_data))/(max(connectance_data)-min(connectance_data))
                              for i in connectance_data]
    norm_degree_data = [(i-min(degree_data))/(max(degree_data)-min(degree_data))
                              for i in degree_data]

    return relation_data, norm_connectance_data, norm_degree_data

def ForestIteration(Nseeds: list, N=100):
    all_relation_data = []
    all_size_data = []
    all_degree_data = []
    for seed in Nseeds:
        seed_size_data = []
        seed_degree_data = []
        avg_size_data = []
        avg_degree_data = []
        
        for i in range(N):
            relation_data, size_data, degree_data = ForestOperation(seed)
            seed_size_data.append(size_data)
            seed_degree_data.append(degree_data)
            
        for i in range(len(relation_data)):
            sum_size_data = 0
            sum_degree_data = 0
            for j in range(N):
                sum_size_data += seed_size_data[j][i]
                sum_degree_data += seed_degree_data[j][i]
            avg_size_data.append(sum_size_data/N)
            avg_degree_data.append(sum_degree_data/N)
        
        all_relation_data.append(relation_data)
        all_size_data.append(avg_size_data)
        all_degree_data.append(avg_degree_data)

    return all_relation_data, all_size_data, all_degree_data

# ===================
# Funciones Warehouse
# ===================

def WarehouseOperation(parameter: int, limit: int, max_value: int):
    height_data = []

    pop = 0
    push = 0

    Warehouse = RandomWarehouseG(parameter)

    for i in range(NWarehouse):
        pos_stack = random.randint(0, len(Warehouse)-1)
        operation = random.randint(1, max_value)
        if limit < operation:
            Warehouse[pos_stack].push(i)
            push += 1
        else:
            Warehouse[pos_stack].pop()
            pop += 1

        if i == NWarehouse-1:
            relation = push/pop
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
            relation, height_points = WarehouseOperation(seed, 10,round(value*10)+10)
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