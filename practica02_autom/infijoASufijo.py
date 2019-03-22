#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import ArbolBinario
sys.path.append('./../')
from aramirezLibs.estructuras import Pila, Estado

alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#"
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
			print("Para char:",char)
			if char in '+*':
				print("Cerraduras")
				minDelUltimo = analizados[-1] #En realidad el mínimo del primero, será el del inicio
				maxDelUltimo = analizados[-1] #En realidad el máximo del ultimo, será el del final
				if minDelUltimo is list:
					minDelUltimo=minDelUltimo[0]
				if maxDelUltimo is list:
					maxDelUltimo=maxDelUltimo[-1]


				gamma = "R"+str(nR)+" -> R"; nR+=1; gamma+= str(nR)+' [label="&epsilon;"];\n' ; nR+=1	#R5->R6 &epsilon;
				betta = "R"+str(nR)+" -> R"; nR+=1; betta+= str(nR)+' [label="&epsilon;"];\n' ; nR+=1	#R7->R8 &epsilon;
				aux = nR - 2
				alffa = "R"+str(aux)+" -> R"+str(aux-1)+' [label="&epsilon;"];\n' #R7 -> R6 &epsilon; Regreso positivo
				

				gamma = gamma.replace("R"+str(aux-1), analizados[-1].split(" ->")[0]) #Reemplaza último estado por el primer nodo del anterior cálculo (R2->R3) => (R2->R0)
				
				#betta = betta.replace( betta[:2], "R"+str( max(re.findall(r'\d+', analizados[-1])) ) ) #Reemplaza penúltimo estado por último estado (máximo) del anterior cálculo (R4->R3) => (R1->R5)
				betta = betta.replace( betta[:2], "R"+str( max(re.findall(r'\d+', maxDelUltimo)) ) ) #Reemplaza penúltimo estado por último estado (máximo) del anterior cálculo (R4->R3) => (R1->R5)
				
				alffa = alffa.replace("R"+str(aux), "R"+str( max(re.findall(r'\d+', maxDelUltimo)) )) #Reemplaza el penúltimo y lo apunta a el máximo del anterior calculado (R4->R3) => (R1->R3)
				alffa = alffa.replace("R"+str(aux-1), "R"+str( min(re.findall(r'\d+', minDelUltimo)) )) #Reemplaza el que era penúltimo por el mínimo del cálculo anterior (R1->R3) => (R1->R0)
				
				kleene = ""
				if char == '*':
					kleene = "R"+gamma[1:2]+" -> R"+betta[7:8]+' [label="&epsilon;"];' #R5 -> R8 &epsilon; Kleene

				analizados.append([gamma, betta, alffa, kleene])
				print(gamma+betta+alffa+kleene)
			elif char == '.':
				print("Concats")
				primeroFin = analizados[-2] #En realidad el máximo del primero, será el del inicio
				segundoIni = analizados[-1] #En realidad el mínimo del ultimo, será el del final
				if primeroFin is list:
					primeroFin=primero[-1]
				if segundoIni is list:
					segundoIni=segundo[0]

				print( "R"+str(min(re.findall(r'\d+', primeroFin))) +" -> R"+ str(min(re.findall(r'\d+', segundoIni))) +' [label='+re.findall(r'\".*\"+', primeroFin)[0]+']')
		
nR = 0

def construyeArbol(sufijoInv):
	arbol = Arbol()
	raiz = Nodo(sufijoInv[0], 'raiz')
	arbol.agregar(raiz)
	for a in range(1, len(sufijoInv)):
		nodo = Nodo( sufijoInv[a] )
		if arbol.nodos[-1].derecha is None:
			arbol.agregar( nodo , 'derecha')
		else:
			arbol.agregar( nodo , 'derecha')
	
		

if __name__ == '__main__':
	regex = input("Dame la regex en infijo:\n")
	sufijo = infixToSufix(regex)
	print(sufijo)

	sufijoReverso = sufijo[::-1]
	print(sufijoReverso)
	input()
	construyeArbol(sufijoReverso)

	analiza_regex_sufijo(sufijo)