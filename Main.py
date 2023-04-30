import Model
import sys
import matplotlib.pyplot as plt
import time

def printMenu():
    print("Bienvenido")
    print("1- Queue")
    print("2- Stack")
    print("3- DisjointSet LinkedList")
    print("4- Union de Queue")
    print("5- Warehouse")
    print("6- DisjointSet Forest")
    print("0- Salir")

def initialP():
    condition = input('Número de elementos iniciales: ')
    Verifier = False
    try:
        condition = int(condition)
        Verifier = True
    except ValueError:
        pass
    if Verifier:
        return condition
    else:   
        print('Ingrese solo valor numérico.')

def showG(x,y,xlabel,ylabel):
    plt.plot(x,y,'r-')
    font1 = {'family':'serif','color':'green','size':15}
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    plt.show()

def saveData(y,folder,size):
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    with open('./Data/'+folder+'/'+date+'_'+str(size)+'.txt', 'w') as f:
        for line in y:
            f.write(str(line))
            f.write('\n')

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        condition = initialP()
        if condition:
            x,y = Model.queueF(condition)
            showG(x,y,'','')
            saveData(y,'Queue',condition)

    elif int(inputs[0]) == 2:
        condition = initialP()
        if condition:
            x,y = Model.stackF(condition)
            showG(x,y,'','')
            saveData(y,'Stack',condition)

    elif int(inputs[0]) == 3:
        condition = initialP()
        if condition:
            x,y = Model.disjointSet_LinkedListF(condition)
            showG(x,y,'','')
            saveData(y,'DisjointSet',condition)

    elif int(inputs[0]) == 4:
        None

    elif int(inputs[0]) == 5:
        None

    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        continue