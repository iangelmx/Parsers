#!/usr/bin/env python
# -*- coding: utf-8 -*-
from estructuras import Estado

class Automata():

    __estado_inicial = None
    __estado_final = None

    __estados = []

    dp = {}

    tablaAutomata = {} 
    """ 
    1 : {'Eps':[5,6,7], 'a':[1], 'b': [2], 'c':[None]} 
    2 : {'Eps':[], 'a':1, 'b': 3, 'c':4} 
    2 : {'Eps':[6], 'a':1, 'b': 3, 'c':4} 
    """
    nEstado = 0

    def __init__(self, labelInicial, alfabeto):
        self.__estado_inicial = labelInicial
        self.nEstado = int(labelInicial)
        q1 = Estado(None, None, labelInicial)
        self.__estados.append( q1 )
    
    def create_simbol_transition(self, label, transitionChar):
        self.nEstado+=1

        if label not in self.dp:
            qA = Estado(label)
            qA.set_transitions(transitionChar, nEstado)



        if label not in self.dp:
            #Estado(edoSig, label, transitionToNext):
            qA = Estado( (label+1), label, transitionChar) #
            qB = Estado( None, label+1)
            #qA.set_transition_to_next( transitionChar )

            #self.dp[ str(label)+'->'+str(label+1) ] = [qA, qB]
            self.dp[ transitionChar ] = [qA, qB]
            self.__estados.append(qA, qB)
            return True
    
    def create_or_transition(self, label, takeTransition):
        [r, s] = takeTransition.split('|')      
        qI = Estado( [self.dp[r] , self.dp[s]], label, 'Eps')
        qI.
        qF = Estado(None, label+1)

    def concatenate_transitions(self, toConcatA, toConcatB):
        qConcat = Estado(  )
        qI = dp[ toConcatA ]
        qF = dp[ toConcatB ]


