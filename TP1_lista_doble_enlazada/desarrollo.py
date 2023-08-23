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
    
    def tamanio(self):
        return self.size

    def agregar(self,dato,posicion = None):
        nuevo_nodo = Nodo(dato)

        if not self.primero: 
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo 
        
        if posicion is None or posicion >= self.tamanio:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    
        if posicion == 0: 
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        
        actual = self.primero

        for i in range(posicion - 1):
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual

        actual.siguiente.anterior = nuevo_nodo



        

    def copiar(self):
        nuevalista = ListaDoblementeEnlazada()
        actual = self.primero

        while actual !=None:
            pass



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
print(listonga.esta_vacia())




