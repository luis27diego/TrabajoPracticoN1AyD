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
   
    def insertar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola  = nuevo_nodo
        self.size += 1
           




   
    def agregar(self,dato,posicion = None):
        nuevo_nodo = Nodo(dato)


        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo


        elif posicion is None or posicion >= self.size:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo


        elif posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo


        else:
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
        self.size += 1




    def copiar(self):
        nuevalista = ListaDoblementeEnlazada()
        actual = self.cabeza


        while actual !=None:
            nuevalista.agregar(actual.dato)
            actual = actual.siguiente
       
        return nuevalista


    def eliminar(self, posicion=None):
        # Verificar si la lista está vacía
        if not self.cabeza:
            return None


        # Si no se proporciona una posición, eliminar el último elemento
        if posicion is None:
           
            # Si hay solo un nodo en la lista
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            self.size -= 1
            dato = self.cola.dato
            return print(dato)


        # Verificar si la posición es inválida
        if posicion < 0 or posicion >= self.size:
            return None


        # Eliminar el primer nodo
        if posicion == 0:
            dato = self.cabeza.dato
            # Si hay solo un nodo en la lista
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
        else:
            # Buscar el nodo en la posición dada
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            # Actualizar enlaces para eliminar el nodo
            actual.anterior.siguiente = actual.siguiente
            # Actualizar el último si se está eliminando el último nodo
            if actual == self.cola:
                self.cola = actual.anterior
            else:
                actual.siguiente.anterior = actual.anterior
       
        # Reducir el tamaño de la lista
        self.size -= 1
        return dato


    def invertir(self):
        if self.esta_vacia() or self.cabeza == self.cola:
            return
   
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
   
        self.cabeza, self.cola = self.cola, self.cabeza










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



print(listonga.cabeza.dato)
print(listonga.cabeza.siguiente.dato)
print(listonga.cola.dato)
print

print(listonga.primero)
print(listonga.ultimo)

