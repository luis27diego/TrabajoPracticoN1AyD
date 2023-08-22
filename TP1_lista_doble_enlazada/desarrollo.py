class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def esta_vacia(self):
        return self.size == 0

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        self.size += 1




listonga = ListaDoblementeEnlazada()
listonga.insertar_al_principio(5)

print(listonga.primero)
print(listonga.ultimo)

