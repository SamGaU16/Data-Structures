import Model
import sys
import matplotlib.pyplot as plt
import time

sys.setrecursionlimit(10**9)

# ==============
# Funciones Menú
# ==============

def printMenu():
    print("Bienvenido")
    print("1- Forest LL Directional")
    print("2- Forest LL Iteration")
    print("3- Forest Directional")
    print("4- Forest Iteration")
    print("5- Warehouse")
    print("0- Salir")

# ===============
# Funciones Input
# ===============

def initialP():
    condition = input('Número de nodos iniciales: ')
    Verifier = False
    try:
        condition = int(condition)
        Verifier = True
    except ValueError:
        pass
    if Verifier and 0<=condition and condition<=1000:
        return condition
    else:   
        print('Ingrese solo valor numérico. Entre 0 a 1000.')

# =================
# Funciones Mostrar
# =================

def plotGD(x1,y1,x2,y2,folder,size,labely='<size>',c1='r-', c2='g--',l1='Hacia 1',l2='Hacia infinito'):
    fig, ax = plt.subplots()
    ax.plot(x1, y1, c1, label=l1)
    ax.plot(x2, y2, c2, label=l2)
    ax.legend(loc='upper right')
    font1 = {'family':'serif','color':'green','size':15}
    plt.xlabel('make/join', fontdict = font1)
    plt.ylabel(labely, fontdict = font1)
    saveFig(folder,size)
    plt.show()

def plotG(x,y,xlabel,ylabel,folder,size,color='r-'):
    plt.plot(x,y,color)
    font1 = {'family':'serif','color':'green','size':15}
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    saveFig(folder,size)
    plt.show()

def plotMultiG(x,y,y2,xlabel,folder,size,c1='r-',c2='b--',l1=None,l2=None):
    fig, ax = plt.subplots()
    ax.plot(x, y , c1, label=l1)
    ax.plot(x, y2, c2, label=l2)
    ax.legend(loc='upper right')
    font1 = {'family':'serif','color':'green','size':15}
    plt.xlabel(xlabel, fontdict = font1)
    saveFig(folder,size)
    plt.show()

# =================
# Funciones Guardar
# =================

def saveData(y,folder,size=None):
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    with open('./Data/'+folder+'/'+date+'_'+str(size)+'.txt', 'w') as f:
        for line in y:
            f.write(str(line))
            f.write('\n')

def saveFig(folder,size):
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    plt.savefig('./Data/'+folder+'/'+date+'_'+str(size)+'.png')

# ==========
# Loop Menú
# ==========

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        condition = initialP()
        if condition:
            x1,y1,x2,y2 = Model.ForestLLD(condition)
            plotGD(x1,y1,x2,y2, 'ForestLL', condition)
            #saveData(y,'ForestLL',condition)

    elif int(inputs[0]) == 2:
        condition = initialP()
        if condition:
            x,y = Model.ForestLLIteration(condition)
            plotG(x,y,'make/join','<size>','ForestLL',condition)
            #saveData(y,'ForestLL') 

    elif int(inputs[0]) == 3:
        condition = initialP()
        if condition:
            x1,y1,y2,x2,y3,y4 = Model.ForestD(condition)
            plotGD(x1,y1,x2,y3,'Forest',condition)
            plotGD(x1,y2,x2,y4,'Forest',condition,labely='<degree>')
            #saveData(y,'Forest',condition)

    elif int(inputs[0]) == 4:
        condition = initialP()
        if condition:
            x,y,y2 = Model.ForestIteration(condition)
            plotMultiG(x,y,y2,'make/join','Forest',condition,l1='<size>',l2='<degree>')
            #saveData(y,'Forest')

    elif int(inputs[0]) == 5:
        condition = initialP()
        if condition:
            x,y = Model.WarehouseIteration(condition)
            plotG(x,y,'pop/push','<height>','Warehouse',condition)
            #saveData(y,'Warehouse',condition)

    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        continue