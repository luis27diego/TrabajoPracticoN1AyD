class ColaPrioridadMax:
    def __init__(self):
        # Constructor: inicializa una lista que servirá para almacenar las tuplas (clave, valor) y el tamaño del montículo.
        self.listaMonticulo = [(0, 0)]  # Inicialmente se crea una tupla ficticia.
        self.tamanio = 0

    def construirMonticulo(self, lista):
        # Método para construir un montículo a partir de una lista de elementos (claves, valores).
        self.tamanio = len(lista)
        self.listaMonticulo = [(0, 0)] + lista[:]  # Se inicializa la listaMonticulo con una tupla ficticia y los elementos de la lista.
        i = self.tamanio // 2
        while (i > 0):
            self.bajar(i)  # Se ajusta el montículo para que sea válido.
            i = i - 1

    def eliminarMin(self):
        # Elimina el elemento con la máxima prioridad (valor) y lo devuelve.
        val_raiz = self.listaMonticulo[1]  # Obtiene la raíz (elemento con máxima prioridad).
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanio]  # Reemplaza la raíz con el último elemento del montículo.
        self.tamanio = self.tamanio - 1  # Reduce el tamaño del montículo.
        self.listaMonticulo.pop()  # Elimina el último elemento (ya duplicado).
        self.bajar(1)  # Ajusta el montículo para mantener su propiedad.
        return val_raiz[1]  # Retorna el valor del elemento con máxima prioridad.

    def decrementarClave(self, nodo, nueva_prioridad):
        # Decrementa la prioridad (clave) de un nodo específico en el montículo.
        idx = 0
        for i in range(1, self.tamanio + 1):
            if self.listaMonticulo[i][1] == nodo:
                idx = i
                break  # Encuentra el índice del nodo en la listaMonticulo.

        if idx > 0:
            if nueva_prioridad > self.listaMonticulo[idx][0]:  # Compara la nueva prioridad con la anterior.
                self.listaMonticulo[idx] = (nueva_prioridad, nodo)  # Actualiza la prioridad del nodo.
                self.subir(idx)  # Ajusta el montículo subiendo el nodo modificado.

    def estaVacia(self):
        # Verifica si el montículo está vacío (sin elementos).
        return self.tamanio == 0

    def subir(self, i):
        # Ajusta el montículo subiendo un nodo específico para mantener la propiedad de max heap.
        while i // 2 > 0:
            if self.listaMonticulo[i][0] > self.listaMonticulo[i // 2][0]:  # Compara la prioridad con su padre.
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]  # Intercambia si es necesario.
            i = i // 2  # Se mueve hacia el padre.

    def bajar(self, i):
        # Ajusta el montículo bajando un nodo específico para mantener la propiedad de max heap.
        while (i * 2) <= self.tamanio:
            mc = self.encontrarMinHijo(i)  # Encuentra el hijo con máxima prioridad.
            if self.listaMonticulo[i][0] < self.listaMonticulo[mc][0]:  # Compara con el hijo de máxima prioridad.
                self.listaMonticulo[i], self.listaMonticulo[mc] = self.listaMonticulo[mc], self.listaMonticulo[i]  # Intercambia si es necesario.
            i = mc  # Se mueve hacia el hijo.

    def encontrarMinHijo(self, i):
        # Encuentra el hijo con máxima prioridad del nodo en la posición 'i'.
        if i * 2 + 1 > self.tamanio:
            return i * 2  # Si solo hay un hijo, lo devuelve.
        else:
            if self.listaMonticulo[i * 2][0] > self.listaMonticulo[i * 2 + 1][0]:  # Compara los hijos.
                return i * 2  # Devuelve el índice del hijo de máxima prioridad.
            else:
                return i * 2 + 1  # Devuelve el índice del otro hijo de máxima prioridad.
