import Model
import sys
import os 
import csv
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**9)
SizeSeeds = [10,20,50,100,200,500,1000,2000]
MinorSeeds = SizeSeeds[:5]
Relations = [round(i*0.1,1) for i in range(1,21)]
MProceso = '\n Procesando...\n'
MDone = 'Proceso terminado con éxito.\n'

# ==============
# Funciones Menú
# ==============

def printMenu():
    print("Bienvenido")
    print("1- Forest LL")
    print("2- Forest")
    print("3- Warehouse")
    print("9- Forest Debug")
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
    if Verifier and 0<=condition and condition<=3000:
        return condition
    else:   
        print('Ingrese solo valor numérico. Entre 0 a 3000.')

# ==================
# Funciones Gráficas
# ==================

font1 = {'family':'serif','color':'green','size':15}

def plotDebug(x1,y1,x2,y2,name, path=None,xlabel= None, ylabel=None, c1='r-',c2='b--',l1=None,l2=None):
    fig, ax = plt.subplots()
    ax.plot(x1, y1, c1, label=l1)
    ax.plot(x2, y2, c2, label=l2)
    ax.legend(loc='upper right')
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    saveFig(path,name)
    plt.show()
    plt.close()

def plotG(x,y,name, path=None, xlabel= None, ylabel=None, color='r-'):
    plt.plot(x,y,color)
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    saveFig(path,name)
    plt.close() 

def plotDoubleG(x1,y1,x2,y2,name, path=None,xlabel= None, ylabel=None, c1='r-',c2='b--',l1=None,l2=None):
    fig, ax = plt.subplots()
    ax.plot(x1, y1, c1, label=l1)
    ax.plot(x2, y2, c2, label=l2)
    ax.legend(loc='upper right')
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    saveFig(path,name)
    plt.close() 

def plotMultiY(data: list, name, path=None, xlabel = None, ylabel= None, x_data=SizeSeeds, labelst=Relations):
    fig, ax = plt.subplots()
    for i in range(len(data)):
        ax.plot(x_data, data[i], label=labelst[i])
    ax.legend(loc='upper left')
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    saveFig(path,name)
    plt.close() 

def plotMultiXY(data: list, path=None, xlabel = None, ylabel= None, labelst=SizeSeeds):
    for i in range(len(data)):
        fig, ax = plt.subplots()
        for j in range(len(data[i])):
            ax.plot(data[i][j], label=labelst[j])
        ax.legend(loc='upper left')
        plt.xlabel(xlabel, fontdict = font1)
        plt.ylabel(ylabel, fontdict = font1)
        name = 'Proporción '+str(Relations[i])
        plt.title(name, fontdict = font1)
        saveFig(path,name)
        plt.close()

def plotFG(x,y,name, path=None, xlabel= None, ylabel=None):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.plot(x[i],y[i],label=f'{SizeSeeds[i]}')
    ax.legend(loc='upper left')
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    saveFig(path,name)
    plt.close() 

# ==================
# Funciones Guardado
# ==================

def createFolder(dir:str):
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    upper_path = './Data/'+dir+'/'
    path = os.path.join(upper_path, date)
    os.mkdir(path)
    return path

def saveData(data,name,path):
    with open(path+f'/{name}.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(data)

def saveFig(path,name):
    plt.savefig(path+'/'+str(name)+'.png')

# ==========
# Loop Menú
# ==========

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    label = 'join/make'
    label_w = 'push/pop'

    if int(inputs[0]) == 1:
            print(MProceso)
            x,y = Model.ForestLLIteration(SizeSeeds)
            path_folder = createFolder('ForestLL')
            plotFG(x,y,'Transition',path=path_folder,xlabel=label,ylabel='<size>')
            for i in range(len(x)):
                saveData(zip(x[i],y[i]),SizeSeeds[i],path_folder)
            print(MDone)

    elif int(inputs[0]) == 2:
            print(MProceso)
            x,y,y2 = Model.ForestIteration(SizeSeeds)
            path_folder = createFolder('Forest')
            plotFG(x,y,'Transition',path=path_folder,xlabel=label,ylabel='<size>')
            plotFG(x,y2,'Transition Degree',path=path_folder,xlabel=label,ylabel='<degree>')
            for i in range(len(x)):
                saveData(zip(x[i],y[i],y2[i]),SizeSeeds[i],path_folder)
            print(MDone)

    elif int(inputs[0]) == 3:
            print(MProceso)
            x,y,size_data, relation_data, data = Model.WarehouseIteration(Relations, SizeSeeds)
            path_folder = createFolder('Warehouse') 
            plotG(x,y,'Transition',path=path_folder, xlabel=label_w, ylabel='<height>')
            plotMultiY(size_data,'Height Comparison', path=path_folder, 
                       xlabel= 'Stacks number',ylabel= '<height>', x_data=SizeSeeds)
            plotMultiY(relation_data,'Relation Comparison', path=path_folder,
                       xlabel= 'Stacks number',ylabel= label_w, x_data=SizeSeeds)
            plotMultiXY(data, path=path_folder, 
                        xlabel='N Operaciones', ylabel='<height>', labelst=Relations)
            saveData(zip(x,y),'Warehouse',path_folder)
            print(MDone)

    elif int(inputs[0]) == 9:
        condition = initialP()
        if condition:
            print(MProceso)
            path_folder = createFolder('Debug') 
            x1,y1,y2,x2,y3,y4 = Model.ForestDebug(condition)
            plotDebug(x1,y1,x2,y3,condition,path=path_folder,
                       xlabel='join/make',ylabel='<size>',c2='g--',l1='Hacia 1',l2='Hacia infinito')
            plotDebug(x1,y2,x2,y4,str(condition)+'_degree',path=path_folder,
                       xlabel='join/make',ylabel='<degree>',c2='g--',l1='Hacia 1',l2='Hacia infinito')
            print(MDone)

    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        continue

