import re
from ArbolSintact import *
from Automata import *
from estructuras import Pila, Estado

alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#"
operadores = "+|*."
agrupadores = "()[]}{"

class Notaciones():

	regexInfijo = ""
	def __init__(self, regexInfijo):
		self.regexInfijo = regexInfijo

	def getPrecedence(self,char):
		jerarquia = {
	#		'(' : 4,
	#		')' : 4,
			'+' : 3,	#monoario
			'*' : 3,	#monoario
			'.' : 2,	#binario
			'|' : 1,	#binario
		}
		return jerarquia[char]

	def infixToSufix(self):
		#alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		#operadores = "+|*."
		#agrupadores = "()[]}{"
		pila = Pila()
		salida = ""
		for char in self.regexInfijo:
			#print("pila antes Iter con:", char)
			#pila.print()
			#print("Salida antes de Iter:", salida)
			if char in alfabeto:
				salida+=char
			elif char in operadores or char in agrupadores:
				if pila.isEmpty() or pila.getTop() == '(':
					pila.push(char)
				elif char == '(':
					pila.push(char)
				elif char == ')':
					while not pila.isEmpty() and pila.getTop() != '(':
						salida += pila.pop()
					if pila.getTop() == '(':
						pila.pop()
				elif pila.getTop() not in agrupadores and self.getPrecedence(char) > self.getPrecedence(pila.getTop()):
					pila.push(char)
				elif pila.getTop() not in agrupadores and self.getPrecedence(char) == self.getPrecedence(pila.getTop()):
					if not pila.isEmpty():
						if pila.getTop() in '+*': #Asociacion R -> L
							pila.push(char)
						elif pila.getTop() in ".|": #Asociacion L -> R
							salida += pila.pop()
							pila.push(char)
				elif pila.getTop() not in agrupadores and self.getPrecedence(char) < self.getPrecedence(pila.getTop()):
					salida+=pila.pop()
					while not pila.isEmpty() and \
								pila.getTop() not in agrupadores and \
								self.getPrecedence(char) < self.getPrecedence(pila.getTop()):
						salida+=pila.pop()
					if not pila.isEmpty() and \
							pila.getTop() not in agrupadores and \
							self.getPrecedence( pila.getTop() ) == self.getPrecedence(char): #Desempate
						if pila.getTop() in '+*': #Asociacion R -> L
							pila.push(char)
						elif pila.getTop() in ".|": #Asociacion L -> R
							salida += pila.pop()
							pila.push(char)
							continue
					pila.push(char) #Si no se cumple el if anterior, quiere decir que la precedencia del tope de la pila será mayor al del char en cuestion
			else:
				return "Caracter no soportado: '"+char+"'"
			

		while not pila.isEmpty():
			salida+=pila.pop()

		return salida

def preprocesaRegex(regex):
	lista = re.findall(r'\w+', regex)
	for i in lista:
		regex = regex.replace(i, '.'.join(i))

	return regex


def regex2AFD():

	entrada = "(a.b.c|c*)"
	regex = input("Dame la regex\n")
	entrada = preprocesaRegex(regex)
	alfa = [x for x in entrada if x.isalpha()]

	a = Notaciones( entrada )

	post = a.infixToSufix()
	t = ArbolSintactico(post)
	d = AFD(alfa, t)
	#print(t) #arbol
	#print(d)	#tabla autom
	salida = open("salidaAfd.gv", "w")
	salida.write("""digraph AFN{
	rankdir = LR;
	node [shape = "circle"];""")


	renglones = str(d).split("\n")
	index = 0
	cadenaOut = ""
	for renglon in renglones:
		original = renglon
		if renglon == "":
			break
		if index == 0:
			if 'I [shape="plaintext"]I ->r1;\n' not in cadenaOut:
				cadenaOut+='I [shape="plaintext"]I ->r1;\n'
			renglon = renglon.replace("->", "")
		renglon=renglon.replace("\t", " ")
		edoActual = renglon.lstrip()[0]
		#print(renglon)

		transiciones = re.findall(r'\w : \d',renglon)
		caracter = ""
		if "Final" in original:
			caracter = 'r{} [shape=doublecircle]'.format(edoActual)
			cadenaOut+=caracter+"\n"
		for tran in transiciones:
			#print(tran)
			if index == 0:
				linea = 'r{} -> r{} [label="{}"]; '.format(edoActual, tran[4],
				tran[0])
				if linea not in cadenaOut:
					cadenaOut+= linea+"\n"
		index+=0
	print("Resultado en salidaAfd.gv")
	salida.write(cadenaOut+"}")
	salida.close()

		


if __name__ == "__main__":
	regex2AFD()