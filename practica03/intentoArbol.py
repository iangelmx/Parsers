from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	i = 0
	while(i < len(fplist)):
		print("Analyzing:",fplist[i])
		if fplist[i] == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif fplist[i] in ['|', '.']:
			currentTree.setRootVal(fplist[i])
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif fplist[i] in ["*>" , "+>"]:
			#if fplist[i+1] == '>':
			currentTree.setRootVal(fplist[i])
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
			#i+=2
			#continue
		elif fplist[i] in ['<*', '<+']:
			#if fplist[i+1] == '*':
			currentTree = pStack.pop()
			#i+=2
			#continue
		elif fplist[i] not in ['.', '|', '*>', '+', ')', '<*']:
			currentTree.setRootVal(fplist[i])
			parent = pStack.pop()
			currentTree = parent
		elif fplist[i] == ')':
			currentTree = pStack.pop()
		else:
			raise ValueError
		i += 1
	return eTree

#pt = buildParseTree("( ( 10 + 5 ) * 3 )")


regex = input("Dame la regex: ")
new = []
regex = "(("+regex+").#)"
ocurrencias = [pos for pos, char in enumerate(regex) if char == '*']
nOcur = len(ocurrencias)*2
print(ocurrencias)

import re

#ocurParent = re.findall( r'\([a-zA-Z|\||\.|\*|\+]*\)\*', regex)
ocurParent = re.findall( r'\(.*\)\*', regex)
ocurSimb = re.findall(r'[a-zA-Z]\*', regex)

for a in ocurParent:
	while a.count('(') > 1 and a.count('(') != a.count(')'):
		a = a.replace('(', "")
	regex = regex.replace( "("+a, "*>("+a[:-1]+"<*" )
	regex = regex.replace( "("+a, "*>("+a[:-1]+"<*" )

for a in ocurSimb:
	regex = regex.replace( a, "*>"+a[:-1]+"<*" )

print(regex)
input(":v")

b=0
while b < len(regex):
	if regex[b] in ["*"] and regex[b+1]==">":
		new.append(regex[b]+">")
		b+=1
	elif regex[b] in ["<"] and regex[b+1]=="*":
		new.append(regex[b]+"*")
		b+=1
	else:
		new.append(regex[b])
	b+=1


"""
apar = 0
while apar < nOcur:
	if new[ocurrencias[apar]-1] == ')':
		new[ocurrencias[apar]] = '<*'
		while ocurrencias[apar] > 0:
			if new[ocurrencias[apar]] != '(':
				ocurrencias[apar]-=1
			else:
				#new.insert(ocurrencias[apar]-2, "*")
				new.insert(ocurrencias[apar], ">*")
				break
	else:
		new.insert(ocurrencias[apar], '<')
		new.insert(ocurrencias[apar]-3, "*")
		new.insert(ocurrencias[apar]-2, ">")
	ocurrencias.extend([pos for pos, char in enumerate(new) if char == '*'])
	print(len(new), ocurrencias, new)
	apar+=2

print("Uno: ")
print(' '.join(new))

input("-----------------")


string = ''.join(new)
print(string)


"""

pt = buildParseTree(' '.join(new))
pt.postorder()  #defined and explained in the next section