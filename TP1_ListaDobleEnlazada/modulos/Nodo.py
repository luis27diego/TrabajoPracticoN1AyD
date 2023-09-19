# Definición de la clase Nodo que representa un nodo en la lista doblemente enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None