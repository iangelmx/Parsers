#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('./../')
from aramirezLibs.estructuras import Pila

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
	alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	operadores = "+|*."
	agrupadores = "()[]}{"
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
	print(infixToSufix(regex))