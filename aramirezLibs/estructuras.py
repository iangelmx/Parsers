#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Pila():
	__pila = ""
	def __init__(self):
		self.__pila = []
		#self.__pila.append("BOTTOM")
	
	def isEmpty(self):
		if len(self.__pila) < 1:
			return True
		else:
			return False

	def push(self, obj):
		self.__pila.append(obj)

	def pop(self):
		return self.__pila.pop()
	
	def getTop(self):
		if not self.isEmpty():
			return self.__pila[-1]
		else:
			return None
	
	def getSize(self):
		return len(self.__pila)

	def print(self):
		print("Pila->",self.__pila)

class Estado():

	__label = None

	#__edoAnt = None
	#__edoSig = None

	##__edoAnt = []
	__edoSig = []

	#__transitionIn = []
	__transitionOut = []
	__isFinal = False
	__isInitial = False

	def __init__(self, edoSig, label):
		self.__label = label
		##self.__edoAnt.append(edoAnt)
		self.__edoSig.append(edoSig)

		
	# def set_previous_state(self, edoAnt):
	# 	if edoAnt is not list:
	# 		self.__edoAnt.append(edoAnt)
	# 	else:
	# 		self.__edoAnt.extend(edoAnt)
	
	def set_next_state(self, edoSig):
		if edoSig is not list:
			self.__edoSig.append(edoSig)
		else:
			self.__edoSig.extend(edoSig)
	
	# def set_transition_to_this(self, simbol):
	# 	self.__transitionIn.append(simbol)

	def set_transition_to_next(self, simbol):
		self.__transitionOut.append(simbol)
	
	def set_transitions(self, posibleTransitions, Inicial): #listaTransicionesPosibles.
		s = Inicial
		for transition in posibleTransitions:
			s+=1
			self.__transitionOut.append(transition)


	def set_type(self, tipo):
		if tipo == 'final':
			self.__isFinal = True
		elif tipo == 'initial':
			self.__isInitial = True
	
	def get_name(self):
		return self.__label

	def print_state_details(self):
		print(
			"Name:", self.__label, \
			"Edo Sig:", self.__edoSig,"\nTransitions:\n\t", \
			"\n\tOut:", self.__transitionOut,"\nIs Final?:",self.__isFinal, \
			"Is Initial?:", self.__isInitial
			)
