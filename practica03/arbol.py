from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree as ArbolBinario




regex = input("Dame la regex:\n")

#regex = "("+regex+").#"

simbolos = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#"

b = 0
pila1 = Stack()
pila2 = Stack()

flag = True

def buscaPivote(regex):
    if len(regex) == 1:
        return Nodo
    print(regex)
    pilas = []
    
    pivotes = {
        '*' : 2,
        '+' : 2,
        '.' : 3,
        '|' : 4
    }

    b = 0
    #pilas.append(Stack())
    pilas.append([])
    indexPila = 0
    for a in range( len(regex)-1, 0, -1 ):
        #print("a",a, "char", regex[a])
        #print("St pre char: '"+regex[a]+"' ->",pilas)
        if regex[a] in simbolos:
            pilas[indexPila].append( { regex[a] : 0 } )
        elif regex[a] == ')':
            indexPila+=1
            #pilas.append(Stack())
            pilas.append([])
        elif regex[a] == '(':
            string = ""
            while pilas[indexPila] != []:
                b = pilas[indexPila].pop()
                #print(a)
                string += list(b.keys())[0]
            indexPila-=1
            pilas[indexPila].append( { string : -1 } )
        elif regex[a] in pivotes:
            pilas[indexPila].append( { regex[a] : pivotes[ regex[a] ] } )
        
        #print("pilas después de: '"+regex[a]+"'->>>>",pilas)
    
    print(pilas)
    ###print("Len de pilas:",len(pilas))
    #pilas.remove([])
    maximo = 0
    pivote = ""
    for grupo in pilas:
        for b in grupo:
            if list(b.values())[0] > maximo:
                maximo = list(b.values())[0]
        #print("Maximo de {} : {}".format(a, maximo))
        for b in grupo:
            if list(b.values())[0] == maximo:
                #print("Pivote: ", list(b.keys())[0])
                pivote = list(b.keys())[0]
                break
        print("grupo->",grupo)
        if pivote != "":
            parteDerecha = grupo
            der = ""
            i = 0
            for a in parteDerecha[::-1]:
                if list(a.keys())[0] != pivote:
                    der += list(parteDerecha[i].keys())[0]
                i+=1
            pilas.remove(grupo)
            parteIzquierda = pilas
            izq = ""
            if len(parteIzquierda>1):
                for a in parteIzquierda:
                    for b in a:
                        izq += list(b.keys())[0]
            else:
                for a in parteIzquierda:
                    print("a in izq",a)
                
            ########print(parteIzquierda, "=>", parteDerecha)
            #break
            return [pivote, izq, der]
        ###print("siguiente...")




[pivot, pIzq, pDer] = buscaPivote(regex)
print(pivot)
print(pIzq)
print(pDer)
raizArbol = ArbolBinario('.')
raizArbol.insertRight('#')

"""
while pIzq != []:
    buscaPivote(pIzq)
    pass
"""

