class Estado:

    def __init__(self, alfabeto, id_list, id, terminal_id):

        self.id_set = set(id_list)
        self.id = id
        self.transitions = dict()  
        self.final = terminal_id in self.id_set  
        for a in alfabeto:
            self.transitions[a] = {}  


class AFD:
    def __init__(self, alfabeto, arbol):
        self.states = []  
        self.alfabeto = alfabeto
        self.id_contador = 1
        self.terminal = arbol.id_contador - 1  
        self.cuentaEstados(arbol)  

    def cuentaEstados(self, t):
        D1 = Estado(self.alfabeto, t.raiz.firstpos, self.give_next_id(), self.terminal)
        self.states.append(D1)
        queue = [D1]
        while len(queue) > 0:  
            st = queue.pop(0)
            new_states = self.Dtran(st, t)
            for s in new_states:
                estado = Estado(self.alfabeto, s, self.give_next_id(), self.terminal)
                self.states.append(estado)
                queue.append(estado)
        return

    def Dtran(self, estado, arbol):
        new_states = []
        for i in estado.id_set:
            if i == self.terminal:
                continue
            label = arbol.leaves[i]
            if estado.transitions[label] == {}:
                estado.transitions[label] = arbol.followpos[i]
            else:
                estado.transitions[label] = estado.transitions[label].union(arbol.followpos[i])
        for a in self.alfabeto:
            if estado.transitions[a] != {}:
                new = True
                for s in self.states:
                    if s.id_set == estado.transitions[a] or estado.transitions[a] in new_states:
                        new = False
                if new:
                    new_states.append(estado.transitions[a])
        return new_states

    def post_procesamiento(self):
        sinEstado = False
        for estado in self.states:
            for a in self.alfabeto:
                if estado.transitions[a] == {}:
                    sinEstado = True
                    estado.transitions[a] = self.id_contador
                SET = estado.transitions[a]
                for state2 in self.states:
                    if state2.id_set == SET:
                        estado.transitions[a] = state2.id
        if sinEstado:
            self.states.append(Estado(self.alfabeto, [], self.id_contador, self.terminal))
            for a in self.alfabeto:
                self.states[-1].transitions[a] = self.states[-1].id

    def give_next_id(self):
        id = self.id_contador
        self.id_contador += 1
        return id

    def __str__(self):
        self.post_procesamiento()
        s = ''
        for estado in self.states:
            if estado.id == 1:
                s = s+'->\t'
            else:
                s = s+'\t'
            s= s+str(estado.id)+' \t'
            for a in self.alfabeto:
                s=s+str(a)+' : '+str(estado.transitions[a])+' \t'
            if estado.final:
                s=s+"Edo. Final"
            s+='\n'
        return s

    def __repr__(self):
        return self.__str__()
