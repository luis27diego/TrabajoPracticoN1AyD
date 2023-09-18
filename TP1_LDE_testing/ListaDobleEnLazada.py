# Definición de la clase Nodo que representa un nodo en la lista doblemente enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# Definición de la clase ListaDobleEnlazada que representa una lista doblemente enlazada.
class ListaDobleEnlazada:
    def __init__(self):
        # Inicialización de la cabeza, cola y tamaño de la lista.
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

# Método para hacer que la lista sea iterable.
    def __iter__(self):
        self._actual = self.cabeza
        return self
    
# Método para avanzar a través de la lista en la iteración.
    def __next__(self):
        if self._actual is None:
            raise StopIteration
        dato = self._actual.dato
        self._actual = self._actual.siguiente
        return dato
    
# Método para obtener el tamaño de la lista.
    def tamanio(self):

        return self.tamanio
    
# Método para verificar si la lista está vacía.
    def esta_vacia(self):
        return self.tamanio == 0
    
# Método para agregar un nuevo nodo al principio de la lista.   
    def agregar_al_inicio(self, dato):

        # Crear un nuevo nodo con el dato proporcionado.
        nuevo_nodo = Nodo(dato)

        # Verificar si la lista está vacía.
        if self.esta_vacia():

            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola de la lista.
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo

        else:
            # Si la lista no está vacía, se enlaza el nuevo nodo al nodo actual de la cabeza.
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo

            # El nuevo nodo se convierte en la nueva cabeza de la lista.
            self.cabeza = nuevo_nodo
        self.tamanio += 1

# Método para agregar un nuevo nodo al final de la lista.  
    def agregar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)

        # Verificar si la lista está vacía.
        if self.esta_vacia():

            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola de la lista.
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo

        # Si la lista no está vacía, se enlaza el nuevo nodo al nodo actual de la cola.
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo

            # El nuevo nodo se convierte en la nueva cola de la lista.
            self.cola  = nuevo_nodo
        self.tamanio += 1

# Método para obtener la longitud de la lista utilizando len().           
    def __len__(self):
        return self.tamanio

# Método para insertar un nuevo nodo en una posición específica o al final de la lista.
    def insertar(self,dato,posicion = None):
        nuevo_nodo = Nodo(dato)

        # Verifica si la lista está vacía.
        if not self.cabeza:

            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola de la lista.
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo

        # Si la posición no se proporciona o es mayor que el tamaño actual de la lista, el nuevo nodo se agrega al final de la lista.
        elif posicion is None or posicion >= self.tamanio:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

        # Si la posición es 0, el nuevo nodo se convierte en la nueva cabeza de la lista, se agrega al inicio
        elif posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

        # Agregar el nuevo nodo a la posición indicada 
        else:
            # Buscamos el nodo en la posición dada.
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente

            # Se acomodan los enlaces para insertar el nuevo nodo en la posición indicada.
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
        self.tamanio += 1

# Método para copiar la lista en una nueva lista doblemente enlazada.
    def copiar(self):
        nuevalista = ListaDobleEnlazada()
        actual = self.cabeza

        # Recorrer la lista original y agregar cada elemento a la nueva lista.
        while actual !=None:
            nuevalista.insertar(actual.dato)

            # Inicializar un puntero al nodo actual, comenzando desde la cabeza de la lista original.
            actual = actual.siguiente

        # Devolver la nueva lista doblemente enlazada que contiene una copia de los datos.
        return nuevalista

# Método para extraer un nodo de una posición específica o el último nodo si no se proporciona una posición.
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

            # El ultimo nodo de la lista
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

# Método para invertir la lista doblemente enlazada.
    def invertir(self):
        if self.esta_vacia() or self.cabeza == self.cola:
            return
   
        actual = self.cabeza
        while actual:
            # Se invierten los enlaces de los nodos para invertir la lista.
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior

        # Se actualiza la cabeza y la cola después de la inversión.
        self.cabeza, self.cola = self.cola, self.cabeza

# Método para concatenar la lista actual con otra lista proporcionada.
    def concatenar(self, otra_lista):
        
        
        lista = otra_lista.copiar()          # Copiar la lista proporcionada para evitar modificarla directamente.

        # Enlazar la cola de la lista actual con la cabeza de la lista copiada.
        self.cola.siguiente = lista.cabeza
        lista.cabeza.anterior = self.cola

        # Actualizar la cola de la lista actual para que sea la cola de la lista copiada.
        self.cola = lista.cola

        self.tamanio += lista.tamanio
   
# Sobrecarga del operador '+' para concatenar dos listas.   
    def __add__(self,lista):
        lista_resultante = ListaDobleEnlazada()
        nodo_a = self.cabeza

        # Copiar los elementos de la lista actual a la nueva lista resultante.
        while nodo_a != None:
            lista_resultante.agregar_al_final(nodo_a.dato)
            nodo_a = nodo_a.siguiente

        # Concatenar la lista proporcionada a la nueva lista resultante.
        lista_resultante.concatenar(lista) 
        return lista_resultante
    
# Método para ordenar la lista utilizando el algoritmo quicksort.
    def ordenar(self):
        
        # Primera llamada a otro metodo, pasandole la posicion 0 que será la cabeza del nodo y el final que sería la cola
        self.ordenar_auxiliar(0,self.tamanio-1)

# Método auxiliar para realizar la ordenación mediante quicksort.
    def ordenar_auxiliar(self,primero,ultimo):
        if primero < ultimo:
            # Lo segundo es llamar a la función ordenamiento_rapido que va a ordenar y retornar un punto para dividir la lista
            puntoDivision = self.ordenamiento_rapido(primero,ultimo)

            # Luego de dividir la lista, se llama a si misma para repetir el proceso de puntoDivision pero en la primera mitad
            self.ordenar_auxiliar(primero,puntoDivision-1)

            # Por ultimo, se llama de nuevo pero se invierten los valores para que ordene la segunda mitad
            self.ordenar_auxiliar(puntoDivision+1,ultimo)

# Método que realiza el particionamiento en quicksort y devuelve el punto de división.
    def ordenamiento_rapido(self,primero,ultimo):
    # Determinar los nodos pivote, izquierdo y derecho según las posiciones proporcionadas.

        # Si primero y último son los valores predeterminados, se utiliza toda la lista.
        if primero == 0 and ultimo == self.tamanio-1:
            nodo_pivote = self.cabeza
            nodo_Izq = self.cabeza.siguiente
            nodo_Der = self.cola

        else:

            # Si primero está en la primera mitad de la lista, se utiliza el nodo pivote de la izquierda.
            if primero < (self.tamanio/2):
                nodo_pivote = self.cabeza
                for _ in range(primero):
                    nodo_pivote = nodo_pivote.siguiente
                nodo_Izq = nodo_pivote.siguiente

            # Si primero está en la segunda mitad de la lista, se utiliza el nodo pivote de la derecha.
            else:
                nodo_pivote = self.cola
                for _ in range((self.tamanio - (primero + 1))):
                    nodo_pivote = nodo_pivote.anterior
                nodo_Izq = nodo_pivote.siguiente

            # Si último está en la primera mitad de la lista, se utiliza el nodo derecho de la izquierda.
            if ultimo > (self.tamanio/2):
                nodo_Der = self.cola
                for _ in range((self.tamanio - (ultimo + 1))):
                    nodo_Der = nodo_Der.anterior

            # Si último está en la segunda mitad de la lista, se utiliza el nodo derecho de la derecha.
            else:
                nodo_Der = self.cabeza
                for _ in range(ultimo):
                    nodo_Der = nodo_Der.siguiente

        marcaIzq = primero + 1
        marcaDer = ultimo

        hecho = False
        while not hecho:

            # Avanzamos el nodo_Izq mientras sea menor o igual al nodo_pivote.
            while marcaIzq <= marcaDer and nodo_Izq.dato <= nodo_pivote.dato:
                nodo_Izq = nodo_Izq.siguiente
                marcaIzq += 1

            # Retrocedemos el nodo_Der mientras sea mayor o igual al nodo_pivote.
            while nodo_Der.dato >= nodo_pivote.dato and marcaDer >= marcaIzq:
                nodo_Der = nodo_Der.anterior
                marcaDer -=1

            # Si las marcas se cruzan, hemos terminado.
            if marcaDer < marcaIzq:
                hecho = True

            else:
                # Intercambiamos los datos de los nodos Izq y Der.
                dato_Temp = nodo_Izq.dato
                nodo_Izq.dato = nodo_Der.dato
                nodo_Der.dato = dato_Temp

        # Intercambiamos el dato del nodo_pivote con el dato del nodo_Der.
        dato_Temp = nodo_pivote.dato
        nodo_pivote.dato = nodo_Der.dato
        nodo_Der.dato = dato_Temp

        # Devolvemos la posición del nodo_Der, que es el punto de división.
        return marcaDer


