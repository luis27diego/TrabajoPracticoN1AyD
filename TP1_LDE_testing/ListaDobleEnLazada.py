class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def __iter__(self):
        self._actual = self.cabeza
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        dato = self._actual.dato
        self._actual = self._actual.siguiente
        return dato

    def tamanio(self):

        return self.tamanio

    def esta_vacia(self):
        return self.tamanio == 0
   
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1
   
    def agregar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola  = nuevo_nodo
        self.tamanio += 1
           
    def __len__(self):
        return self.tamanio


   
    def insertar(self,dato,posicion = None):
        nuevo_nodo = Nodo(dato)

        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo


        elif posicion is None or posicion >= self.tamanio:
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
        self.tamanio += 1




    def copiar(self):
        nuevalista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual !=None:
            nuevalista.insertar(actual.dato)
            actual = actual.siguiente
       
        return nuevalista


    def extraer(self, posicion=None):
        # Verificar si la lista está vacía
        if self.tamanio == 0:
            raise ValueError("Extraer de una lista vacia deberia extraer error")
        
        # Si no se proporciona una posición, eliminar el último elemento
        if posicion is None or posicion == -1:
            dato = self.cola.dato
            # Si hay solo un nodo en la lista
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            self.tamanio -= 1
            
            return dato


        # Verificar si la posición es inválida
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("La posición especificada está fuera de los límites de la lista")

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
        self.tamanio -= 1
        return dato


    def invertir(self):
        if self.esta_vacia() or self.cabeza == self.cola:
            return
   
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
   
        self.cabeza, self.cola = self.cola, self.cabeza


    def concatenar(self, otra_lista):
        
        
        lista = otra_lista.copiar()
        self.cola.siguiente = lista.cabeza
        lista.cabeza.anterior = self.cola
        self.cola = lista.cola

        self.tamanio += lista.tamanio

        
    
    def __add__(self,lista):
        lista_e = ListaDobleEnlazada()
        nodo_a = self.cabeza

        while nodo_a != None:
            lista_e.agregar_al_final(nodo_a.dato)
            nodo_a = nodo_a.siguiente

        lista_e.concatenar(lista) 
        return lista_e
    
    def ordenar(self):
        # Primera llamada a otro metodo, pasandole la posicion 0 que será la cabeza del nodo
        # y el final que sería la cola
        self.ordenar_auxiliar(0,self.tamanio-1)

    def ordenar_auxiliar(self,primero,ultimo):
        if primero < ultimo:
            # Lo segundo es llamar a la función quick_sort que va a ordenar y retornar
            # un punto para dividir la lista
            puntoDivision = self.quick_sort(primero,ultimo)
            # Luego de dividir la lista, se llama a si misma para repetir el proceso de puntoDivision pero en
            # la primera mitad
            self.ordenar_auxiliar(primero,puntoDivision-1)
            # Por ultimo, se llama de nuevo pero se invierten los valores para que ordene la segunda mitad
            self.ordenar_auxiliar(puntoDivision+1,ultimo)

    def quick_sort(self,primero,ultimo):

        if primero == 0 and ultimo == self.tamanio-1:
            nodo_pivote = self.cabeza
            nodo_Izq = self.cabeza.siguiente
            nodo_Der = self.cola
        else:
            if primero < (self.tamanio/2):
                nodo_pivote = self.cabeza
                for _ in range(primero):
                    nodo_pivote = nodo_pivote.siguiente
                nodo_Izq = nodo_pivote.siguiente

            else:
                nodo_pivote = self.cola
                for _ in range((self.tamanio - (primero + 1))):
                    nodo_pivote = nodo_pivote.anterior
                nodo_Izq = nodo_pivote.siguiente

            if ultimo > (self.tamanio/2):
                nodo_Der = self.cola
                for _ in range((self.tamanio - (ultimo + 1))):
                    nodo_Der = nodo_Der.anterior

            else:
                nodo_Der = self.cabeza
                for _ in range(ultimo):
                    nodo_Der = nodo_Der.siguiente

        marcaIzq = primero + 1
        marcaDer = ultimo

        hecho = False
        while not hecho:

            while marcaIzq <= marcaDer and nodo_Izq.dato <= nodo_pivote.dato:
                nodo_Izq = nodo_Izq.siguiente
                marcaIzq += 1
            while nodo_Der.dato >= nodo_pivote.dato and marcaDer >= marcaIzq:
                nodo_Der = nodo_Der.anterior
                marcaDer -=1

            if marcaDer < marcaIzq:
                hecho = True

            else:
                dato_Temp = nodo_Izq.dato
                nodo_Izq.dato = nodo_Der.dato
                nodo_Der.dato = dato_Temp

        dato_Temp = nodo_pivote.dato
        nodo_pivote.dato = nodo_Der.dato
        nodo_Der.dato = dato_Temp

        return marcaDer


