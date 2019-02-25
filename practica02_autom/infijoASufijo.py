#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('./../')
from aramirezLibs.estructuras import Pila, Estado

alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
operadores = "+|*."
agrupadores = "()[]}{"

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

def analiza_regex_sufijo(regexSufix):
	import re
	global nR
	#analizados = [ [0,1], [2,3,4] ]
	analizados = []
	cuentaSimb = 0
	for char in regexSufix:
		if char in alfabeto:
			salida = "R"+str(nR)+" -> R"; nR+=1; salida+=str(nR)+' [label="'+char+'"];\n'; nR+=1
			analizados.append(salida)
			print( salida )
		elif char in operadores:
			if char not in "|.":
				if char in '+*':
					salida = "R"+str(nR)+" -> R"; nR+=1; salida+= str(nR)+' [label="&epsilon;"];\n' ; nR+=1	#R5->R6 &epsilon;
					salida+= "R"+str(nR)+" -> R"; nR+=1; salida+= str(nR)+' [label="&epsilon;"];\n' ; nR+=1	#R7->R8 &epsilon;
					aux = nR - 2
					salida+= "R"+str(aux)+" -> R"+str(aux-1)+' [label="&epsilon;"];\n' #R7 -> R6 &epsilon; Regreso positivo
					if char == '*':
						salida += "R"+str(nR-3)+"-> R"+str(nR-1)+' [label="&epsilon;"];' #R5 -> R8 &epsilon; Kleene

					print(salida)
					print("Se reemplazará:", "R"+str(aux-1) ,"por:", analizados[-1].split(" ->")[0])
					print("Se reemplazará:", "R"+str(nR-1) ,"por:", max(re.findall(r'\d+', analizados[-1])) )
					salida = salida.replace( "R"+str(aux-1), analizados[-1].split(" ->")[0] )
					salida = salida[::-1].replace( "R"+str(nR-1), "R"+str( max(re.findall(r'\d+', analizados[-1])) ), 1)[::-1]
					print(salida)
		
nR = 0

if __name__ == '__main__':
	regex = input("Dame la regex en infijo:\n")
	sufijo = infixToSufix(regex)

	print(sufijo)

	analiza_regex_sufijo(sufijo)