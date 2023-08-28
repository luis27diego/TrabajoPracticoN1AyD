class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def esta_vacia(self):
        return self.size == 0

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.size += 1




listonga = ListaDoblementeEnlazada()
listonga.insertar_al_principio(5)
listonga.insertar_al_principio(10)
listonga.insertar_al_principio(70)
listonga.agregar(900,1)
listonga.eliminar(1)


print(listonga.cabeza.dato)
print(listonga.cabeza.siguiente.dato)
print(listonga.cola.dato)
print

print(listonga.primero)
print(listonga.ultimo)

