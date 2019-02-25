import random
class Automata():
	__tipo = ""
	__caracteristicas = {
		'inicial' : None,
		'final' : None
	}
	__edos_automata = [] #Arreglo de Estados

	def __init__(self, tipo, estados):
		self.__tipo = tipo
		self.__edos_automata = estados

	def set_feature_state(self, feature, estado):
		self.__caracteristicas['feature'] = estado


class Estado():
	__transiciones = {} #{	'$':[1,2,3,4], 'a':[2]	}
	__iD = 0
	isFinal = False
	isInitial = False


	def __init__(self, transiciones):
		self.__transiciones = transiciones
		self.__iD = random.randint(0, 99999)

	def getId(self):
		return self.__iD

	def get_transitions(self, transiciones):
		return self.transiciones

	#def set_transition(self, transicion):
	#	if transicion not in self.__transiciones:
	#		self.__transiciones[ transicion ] = 

class Transicion():
	__simbolo = ""
	__e0 = None
	__ef = None

	def setStart(self, symbolTrans):
		self.__e0 = Estado(symbolTrans)
	
	def setEnd(self, endTrans):
		for estado in self.__e0.get_transitions():

		self.__ef = Estado(symbolTrans)

class RoS(Transicion):
	q0 = None
	def __init__(self, r, s): #Transiciones
		trans = Transicion()
		trans.setStart( {"Eps":[ r[0].getId() , s[0].getId() ]} )

		trans.setEnd( Estado([]) )

		trans
		q0 = Estado(
			{
				"Eps": 
					[
						r[0].getId(),
						s[0].getId()
					]
			}
		)
		q0.
