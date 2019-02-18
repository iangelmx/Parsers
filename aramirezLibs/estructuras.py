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