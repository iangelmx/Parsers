#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import re
#sys.path.append('./../aramirezLibs')
from estructuras import Pila, Estado

alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#"
operadores = "+|*."
agrupadores = "()[]}{"

def construyeThompson(postfix):
	regex=''.join(postfix)

	keys=list(set(re.sub('[^A-Za-z0-9]+', '', regex)+'e'))

	s=[];pilaL=[];eInicial=0;eFinal=1

	contAux=-1;c1=0;c2=0
	listaQuitar = []

	for i in regex:
		#print("s->", s)
		if i in keys:
			contAux=contAux+1
			c1=contAux
			contAux=contAux+1
			c2=contAux
			s.append({})
			s.append({})
			pilaL.append([c1,c2])
			s[c1][i]=c2
		elif i=='*':
			r1,r2=pilaL.pop()
			contAux=contAux+1
			c1=contAux
			contAux=contAux+1
			c2=contAux
			s.append({})
			s.append({})
			pilaL.append([c1,c2])
			s[r2]['&epsilon;']=(r1,c2)
			s[c1]['&epsilon;']=(r1,c2)
			if eInicial==r1:
				eInicial=c1 
			if eFinal==r2:
				eFinal=c2 
		elif i=='+':
			r1,r2=pilaL.pop()
			contAux+=1
			c1=contAux
			contAux+=1
			c2=contAux
			s.append({})
			s.append({})
			pilaL.append([c1,c2])
			s[r2]['&epsilon;']= (r1,c2)
			s[c1]['&epsilon;']= r1 #(r1,c2)
			if eInicial==r1:
				eInicial=c1 
			if eFinal==r2:
				eFinal=c2 
		elif i=='.':
			r11,r12=pilaL.pop()
			r21,r22=pilaL.pop()
			pilaL.append([r21,r12])
			###print("->",r21, r22, r11, r22)
			###print("pre",s[r22])
			#s[r22]=r11
			#s[r22][ i ]=r11
			###Original: #s[r22][ 'e' ]=r11
			#Recorrer desde r21 y cuando vaya a llegar a r22 cambiar a r11
			#Gustavo: s[r21][ 'e' ]=r11
			s[r22] = s[r11] #quitar<-
			
			#del s[r11]
			s[r11][''] = 0
			listaQuitar.append(r11)
			
			###print("post", s[r22])
			if eInicial==r11:
				eInicial=r21 
			if eFinal==r22:
				eFinal=r12 
		else:
			contAux=contAux+1
			c1=contAux
			contAux=contAux+1
			c2=contAux
			s.append({})
			s.append({})
			r11,r12=pilaL.pop()
			r21,r22=pilaL.pop()
			pilaL.append([c1,c2])
			s[c1]['&epsilon;']=(r21,r11)
			s[r12]['&epsilon;']=c2
			s[r22]['&epsilon;']=c2
			if eInicial==r11 or eInicial==r21:
				eInicial=c1 
			if eFinal==r22 or eFinal==r12:
				eFinal=c2
	#print(keys)
	print("s->",s)
	return [s, listaQuitar, eInicial]



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

if __name__ == '__main__':
	regex = input("Dame la regex en infijo:\n")
	regex = preprocesaRegex(regex)
	print(">>>"+regex)
	notacion = Notaciones( regex )
	sufijo = notacion.infixToSufix()
	#print(sufijo)

	[tabla, quitar, eInicial ] = construyeThompson(sufijo)
	print("quitar", quitar)
	archivo = open("salida.gv", "w")
	
	i = 0
	archivo.write("""digraph AFN{
rankdir = LR;
node [shape = "circle"];
""")
	index = 0
	#for a in tabla:
	maximo = 0
	minimo = 999

	for a in tabla:
		if a != {}:
			if isinstance(list(a.values())[0], tuple):
				for b in list(a.values())[0]:
					if int(b) > maximo:
						maximo = int(b)
					if int(b) < minimo:
						minimo = int(b)
			else:
				if int(list(a.values())[0]) > maximo:
					maximo = int(list(a.values())[0])
				if int(list(a.values())[0]) < minimo:
					minimo = int(list(a.values())[0])
	ind = 0
	inicial = '0'
	for a in tabla:
		if a != {}:
			if isinstance(list(a.values())[0], tuple):
				if int(list(a.values())[0][0]) == minimo:
					print("quiza:", ind)
					inicial = ind
			else:
				if int(list(a.values())[0]) == minimo:
					print("quiza i:", ind)
					inicial = ind
			ind += 1

	print("Maximo:",maximo)
	print("minimo:", minimo)
	for a in range( len(tabla) ):
		if a in quitar:
			i+=1
			continue
		if tabla[a] != {}:
			print(i, " con ", list(tabla[a].keys())[0], " va a:", list(tabla[a].values()))
			#print(type(list(a.values())[0]))
			if isinstance(list(tabla[a].values())[0], tuple):
				#print(type(list(a.values())[0] ))
				for b in list(tabla[a].values())[0]:
					if int(b) == maximo:
						archivo.write( 'r{} -> r{} [label="{}", peripheries="4"];\n'.format(i, b, list(tabla[a].keys())[0]) )
					else:
						archivo.write( 'r{} -> r{} [label="{}"];\n'.format(i, b, list(tabla[a].keys())[0]) )
			else:
				if int( list(tabla[a].values())[0] ):
					archivo.write( 'r{} -> r{} [label="{}", peripheries="4"];\n'.format(i, list(tabla[a].values())[0], list(tabla[a].keys())[0]))
				else:
					archivo.write( 'r{} -> r{} [label="{}"];\n'.format(i, list(tabla[a].values())[0], list(tabla[a].keys())[0]))
			i+=1
	archivo.write("r{} [shape=doublecircle];".format(maximo))
	archivo.write('I [shape="plaintext"]')
	archivo.write('I ->r{}'.format(eInicial))
	archivo.write("}")
	archivo.close()
	
