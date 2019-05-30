class Node:
    def __init__(self, type, label, id=None, hijo_izquierdo=None, hijo_derecho=None):
        self.id = id  
        self.type = type
        self.hijo_izquierdo = hijo_izquierdo
        self.hijo_derecho = hijo_derecho
        self.label = label
        self.nullable = False  
        self.firstpos = set()  
        self.lastpos = set()  

    def __str__(self):
        cuentaHijos = int(self.hijo_derecho != None) + int(self.hijo_izquierdo != None)
        return '''Tipo\t\t:\t{0}
Nombre\t\t:\t{1}
Hijos\t:\t{2}
Anulable\t:\t{3}
PrimerPos\t:\t{4}
UltimoPos\t\t:\t{5}'''.format(self.type, self.label, cuentaHijos, self.nullable, self.firstpos, self.lastpos)

    def __repr__(self):
        cuentaHijos = int(self.hijo_derecho != None) + int(self.hijo_izquierdo != None)
        s = "<" + "'{0}'".format(self.type) + ' Node with label ' + "'{0}'".format(self.label) + ' and ' + str(
            cuentaHijos) + [' child', ' children'][cuentaHijos != 1] + '>'
        return s

    def imprime_subarbol(self, nivel=0, linelist=[], hijoDerecho=False, instar=False):
        cerradura = self.type == 'cerradura'
        N = '\n'
        T = '\t'
        L = '|'
        if nivel == 0:
            ret = self.label + '\n'
        else:
            s = ''
            if not instar:
                for k in range(2):
                    for i in range(nivel):
                        if i in linelist:
                            s += T*(i!=0) + L
                        else:
                            s += T
                    if k == 0:
                        s += N

            ret = s + '___' + self.label + N * (not cerradura)
        if hijoDerecho:
            linelist.pop(-1)
        if self.hijo_izquierdo:
            ret += self.hijo_izquierdo.imprime_subarbol(nivel + 1, linelist + [nivel] * (not cerradura),
                                                 instar=cerradura)
        if self.hijo_derecho:
            ret += self.hijo_derecho.imprime_subarbol(nivel + 1, linelist + [nivel], hijoDerecho=True)
        return ret


class ArbolSintactico:
    
    def __init__(self, post):
        
        self.raiz = Node('cat', '.')  
        self.leaves = dict()  
        self.id_contador = 1  
        #Se crea el arbol
        self.create_tree(post)
        #Se buscan siguientes, anulables, Primerpos and Ultimopos para cada nodo:
        self.followpos = [set() for i in range(self.id_contador)]
        self.postOrden_anulablePrimerPosUltimoPosSiguiente(self.raiz)

    def create_tree(self, post):
        
        stack = []
        for token in post:
            print("token:",token)
            if token == '.':
                left = stack.pop()
                right = stack.pop()
                temp = Node('cat', token, hijo_izquierdo=right, hijo_derecho=left)
                stack.append(temp)
            
            elif token == '|':
                left = stack.pop()
                right = stack.pop()
                temp = Node('or', token, hijo_izquierdo=left, hijo_derecho=right)
                stack.append(temp)
            elif token == '*':
                left = stack.pop()  
                temp = Node('cerradura', token, hijo_izquierdo=left)
                stack.append(temp)
            else:  
                temp = Node('identifier', token, id=self.give_next_id())
                self.leaves[temp.id] = temp.label
                stack.append(temp)

        temp = Node('identifier', '#', id=self.give_next_id())
        self.leaves[temp.id] = temp.label
        self.raiz.hijo_izquierdo = stack.pop()
        self.raiz.hijo_derecho = temp
        return

    def give_next_id(self):
       
        id = self.id_contador
        self.id_contador += 1
        return id

    def postOrden_anulablePrimerPosUltimoPosSiguiente(self, node):
        
        if not node:  
            return
        self.postOrden_anulablePrimerPosUltimoPosSiguiente(node.hijo_izquierdo)
        self.postOrden_anulablePrimerPosUltimoPosSiguiente(node.hijo_derecho)
        if node.type == 'identifier':
            if node.label == '@':  # empty char
                node.nullable = True
            else:
                node.firstpos.add(node.id)
                node.lastpos.add(node.id)
        elif node.type == 'or':
            node.nullable = node.hijo_izquierdo.nullable or node.hijo_derecho.nullable
            node.firstpos = node.hijo_izquierdo.firstpos.union(node.hijo_derecho.firstpos)
            node.lastpos = node.hijo_izquierdo.lastpos.union(node.hijo_derecho.lastpos)
        elif node.type == 'cerradura':
            node.nullable = True
            node.firstpos = node.hijo_izquierdo.firstpos
            node.lastpos = node.hijo_izquierdo.lastpos
            self.compute_follows(node)  
        elif node.type == 'cat':
            node.nullable = node.hijo_izquierdo.nullable and node.hijo_derecho.nullable
            if node.hijo_izquierdo.nullable:
                node.firstpos = node.hijo_izquierdo.firstpos.union(node.hijo_derecho.firstpos)
            else:
                node.firstpos = node.hijo_izquierdo.firstpos
            if node.hijo_derecho.nullable:
                node.lastpos = node.hijo_izquierdo.lastpos.union(node.hijo_derecho.lastpos)
            else:
                node.lastpos = node.hijo_derecho.lastpos
            self.compute_follows(node)  
        return

    def compute_follows(self, n):
        
        if n.type == 'cat':
            for i in n.hijo_izquierdo.lastpos:
                self.followpos[i] = self.followpos[i].union(n.hijo_derecho.firstpos)
        elif n.type == 'cerradura':
            for i in n.hijo_izquierdo.lastpos:
                self.followpos[i] = self.followpos[i].union(n.hijo_izquierdo.firstpos)

    def __str__(self):
        return self.raiz.imprime_subarbol()
    def __repr__(self):
        return self.raiz.imprime_subarbol()
