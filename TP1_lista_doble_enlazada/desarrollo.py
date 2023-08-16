class Nodo:
    def __init__(self,valor):
        self.valor = valor 
        self.izq = None
        self.der = None 



    def set_izq (self, value):

        self.izq = value 

    def set_der (self,value):

        self.der = value 



nodo = Nodo(5)

nodo.set_der(56)
nodo.set_izq(800)
print(nodo.der)
print(nodo.izq)


