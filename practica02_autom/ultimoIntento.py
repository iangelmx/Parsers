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

	for i in regex:
		#print("s->", s)
		if i in keys:
			contAux=contAux+1;c1=contAux;contAux=contAux+1;c2=contAux;
			s.append({});s.append({})
			pilaL.append([c1,c2])
			s[c1][i]=c2
		elif i=='*':
			r1,r2=pilaL.pop()
			contAux=contAux+1;c1=contAux;contAux=contAux+1;c2=contAux;
			s.append({});s.append({})
			pilaL.append([c1,c2])
			s[r2]['e']=(r1,c2);s[c1]['e']=(r1,c2)
			if eInicial==r1:eInicial=c1 
			if eFinal==r2:eFinal=c2 
		elif i=='.':
			r11,r12=pilaL.pop()
			r21,r22=pilaL.pop()
			pilaL.append([r21,r12])
			###print("->",r21, r22, r11, r22)
			###print("pre",s[r22])
			#s[r22]=r11
			#s[r22][ i ]=r11
			s[r22][ 'e' ]=r11
			###print("post", s[r22])
			if eInicial==r11:eInicial=r21 
			if eFinal==r22:eFinal=r12 
		else:
			contAux=contAux+1;c1=contAux;contAux=contAux+1;c2=contAux;
			s.append({});s.append({})
			r11,r12=pilaL.pop()
			r21,r22=pilaL.pop()
			pilaL.append([c1,c2])
			s[c1]['e']=(r21,r11); s[r12]['e']=c2; s[r22]['e']=c2
			if eInicial==r11 or eInicial==r21:eInicial=c1 
			if eFinal==r22 or eFinal==r12:eFinal=c2
	#print(keys)
	return s

def getPrecedence(char):
	jerarquia = {
#		'(' : 4,
#		')' : 4,
		'+' : 3,	#monoario
		'*' : 3,	#monoario
		'.' : 2,	#binario
		'|' : 1,	#binario
	}
	return jerarquia[char]


def infixToSufix(regexInfijo):
	#alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	#operadores = "+|*."
	#agrupadores = "()[]}{"
	pila = Pila()
	salida = ""
	for char in regexInfijo:
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
			elif pila.getTop() not in agrupadores and getPrecedence(char) > getPrecedence(pila.getTop()):
				pila.push(char)
			elif pila.getTop() not in agrupadores and getPrecedence(char) == getPrecedence(pila.getTop()):
				if not pila.isEmpty():
					if pila.getTop() in '+*': #Asociacion R -> L
						pila.push(char)
					elif pila.getTop() in ".|": #Asociacion L -> R
						salida += pila.pop()
						pila.push(char)
			elif pila.getTop() not in agrupadores and getPrecedence(char) < getPrecedence(pila.getTop()):
				salida+=pila.pop()
				while not pila.isEmpty() and \
							pila.getTop() not in agrupadores and \
							getPrecedence(char) < getPrecedence(pila.getTop()):
					salida+=pila.pop()
				if not pila.isEmpty() and \
						pila.getTop() not in agrupadores and \
						getPrecedence( pila.getTop() ) == getPrecedence(char): #Desempate
					if pila.getTop() in '+*': #Asociacion R -> L
						pila.push(char)
					elif pila.getTop() in ".|": #Asociacion L -> R
						salida += pila.pop()
						pila.push(char)
						continue
				pila.push(char) #Si no se cumple el if anterior, quiere decir que la precedencia del tope de la pila será mayor al del char en cuestion
		else:
			return "Caracter no soportado: '"+char+"'"
		#print("pila despues de iter: ")
		#pila.print()
		#print("Salida despues de Iter:", salida)
		#print("................................................")

	while not pila.isEmpty():
		salida+=pila.pop()

	return salida

if __name__ == '__main__':
	regex = input("Dame la regex en infijo:\n")
	sufijo = infixToSufix(regex)
	print(sufijo)

	tabla = construyeThompson(sufijo)
	archivo = open("salida.gv", "w")
	
	i = 0
	archivo.write("""digraph AFN{
rankdir = LR;
node [shape = "circle"];""")
	for a in tabla:
		if a != {}:
			print(i, " con ", list(a.keys())[0], " va a:", list(a.values()))
			#print(type(list(a.values())[0]))
			if isinstance(list(a.values())[0], tuple):
				print(type(list(a.values())[0] ))
				for b in list(a.values())[0]:
					archivo.write( 'r{} -> r{} [label="{}"];\n'.format(i, b, list(a.keys())[0]) )
			else:
				archivo.write( 'r{} -> r{} [label="{}"];\n'.format(i, list(a.values())[0], list(a.keys())[0]))
			i+=1
	archivo.write("}")
	archivo.close()
	
