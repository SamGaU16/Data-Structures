import Model
import sys
import matplotlib.pyplot as plt
import time

sys.setrecursionlimit(10**9)

def printMenu():
    print("Bienvenido")
    print("1- Forest LL Phase Transition")
    print("2- Forest LL Random")
    print("3- Forest Phase Transition")
    print("4- Forest Random")
    print("5- Warehouse")
    print("0- Salir")

def initialP():
    condition = input('Número de elementos iniciales: ')
    Verifier = False
    try:
        condition = int(condition)
        Verifier = True
    except ValueError:
        pass
    if Verifier and condition<=3000:
        return condition
    else:   
        print('Ingrese solo valor numérico. No mayor a 3000.')

def showG(x,y,xlabel,ylabel,color='r-'):
    plt.plot(x,y,color)
    font1 = {'family':'serif','color':'green','size':15}
    plt.xlabel(xlabel, fontdict = font1)
    plt.ylabel(ylabel, fontdict = font1)
    plt.show()

def showMultiG(x,y,y2,xlabel,c1='r-',c2='b--',l1=None,l2=None):
    fig, ax = plt.subplots()
    ax.plot(x, y , c1, label=l1)
    ax.plot(x, y2, c2, label=l2)
    ax.legend(loc='upper right')
    font1 = {'family':'serif','color':'green','size':15}
    plt.xlabel(xlabel, fontdict = font1)
    plt.show()

def saveData(y,folder,size=None):
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    with open('./Data/'+folder+'/'+date+'_'+str(size)+'.txt', 'w') as f:
        for line in y:
            f.write(str(line))
            f.write('\n')

def saveFig(folder,size=None):
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    if size:
        plt.savefig('./Data/'+folder+'/'+date+'_'+size+'.png')
    else:
        plt.savefig('./Data/'+folder+'/'+date+'.png')


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        condition = initialP()
        if condition:
            x,y = Model.ForestLLPT(condition)
            showG(x,y,'make/join','<size>')
            saveFig('ForestLL',size=condition)
            #saveData(y,'ForestLL',condition)

    elif int(inputs[0]) == 2:
        x,y = Model.ForestLLR()
        showG(x,y,'make/join','<size>')
        saveFig('ForestLL')
        #saveData(y,'ForestLL')  

    elif int(inputs[0]) == 3:
        condition = initialP()
        if condition:
            x,y,y2 = Model.ForestPT(condition)
            showMultiG(x,y,y2,'make/join',l1='<size>',l2='<degree>')
            saveFig('Forest',size=condition)
            #saveData(y,'Forest',condition)

    elif int(inputs[0]) == 4:
        x,y,y2 = Model.ForestR()
        showMultiG(x,y,y2,'make/join',l1='<size>',l2='<degree>')
        saveFig('Forest')
        #saveData(y,'Forest')

    elif int(inputs[0]) == 5:
        condition = initialP()
        if condition:
            x,y = Model.Warehouse(condition)
            showG(x,y,'pop/push','<height>')
            saveFig('Warehouse',size=condition)
            #saveData(y,'Warehouse',condition)

    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        continue