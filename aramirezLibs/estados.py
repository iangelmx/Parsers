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

	def __init__(self, transiciones):
		self.__transiciones = transiciones

	def get_transitions(self, transiciones):
		return self.transiciones
