#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import re
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree as Arbol
#sys.path.append('./../aramirezLibs')
from estructuras import Pila, Estado

alfabeto = "abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#"
operadores = "+|*."
agrupadores = "()[]}{"

def automate(postfix):
	regex=''.join(postfix)

	keys=list(set(re.sub('[^A-Za-z0-9]+', '', regex)+'e'))

	s=[];stack=[];start=0;end=1

	counter=-1;c1=0;c2=0

	for i in regex:
		print("s->", s)
		if i in keys:
			counter=counter+1;c1=counter;counter=counter+1;c2=counter;
			s.append({});s.append({})
			stack.append([c1,c2])
			s[c1][i]=c2
		elif i=='*':
			r1,r2=stack.pop()
			counter=counter+1;c1=counter;counter=counter+1;c2=counter;
			s.append({});s.append({})
			stack.append([c1,c2])
			s[r2]['e']=(r1,c2);s[c1]['e']=(r1,c2)
			if start==r1:start=c1 
			if end==r2:end=c2 
		elif i=='.':
			r11,r12=stack.pop()
			r21,r22=stack.pop()
			stack.append([r21,r12])
			###print("->",r21, r22, r11, r22)
			###print("pre",s[r22])
			#s[r22]=r11
			#s[r22][ i ]=r11
			s[r22][ 'e' ]=r11
			###print("post", s[r22])
			if start==r11:start=r21 
			if end==r22:end=r12 
		else:
			counter=counter+1;c1=counter;counter=counter+1;c2=counter;
			s.append({});s.append({})
			r11,r12=stack.pop()
			r21,r22=stack.pop()
			stack.append([c1,c2])
			s[c1]['e']=(r21,r11); s[r12]['e']=c2; s[r22]['e']=c2
			if start==r11 or start==r21:start=c1 
			if end==r22 or end==r12:end=c2

	print(keys)

	i = 0
	for a in s:
		if a != {}:
			print(i, " con ", list(a.keys())[0], " va a:", list(a.values()))
			i+=1

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

	automate(sufijo)

	input(":-:-:-::-:-:-::-:-:-::-:-:-::-:-:-::-:-:-:")

	sufijoReverso = sufijo[::-1]
	print(sufijoReverso)
	input()
	construyeArbol(sufijoReverso)

	analiza_regex_sufijo(sufijo)