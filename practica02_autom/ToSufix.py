class Pila():
    __pila = ""
    def __init__(self):
        self.__pila = []
    
    def isEmpty(self):
        if len(self.__pila) == 0:
            return True
        else:
            return False

    def push(self, obj):
        self.__pila.append(obj)

    def pop(self):
        self.__pila.pop()
    
    def getTop(self):
        return self.__pila[-1]
    
    def getSize(self):
        return len(self.__pila)

def getType(char):
    if char in alfabeto:
        return "simbol"
    elif char in ops:
        return "operator"

alfabeto = "abcdefghijklmnopqrstuvxyz0123456789"
operadores = ['+', '*', '|', '(', ')']
ops = "+|*()"


if __name__ == "__main__":
    pass'

regex = input("Inserta la expresión regular:\n")

pila = []

for char in regex:
    