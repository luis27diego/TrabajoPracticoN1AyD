
class MonticuloBinario:
    def __init__(self):
        # Inicializa el montículo binario con una lista que comienza con un valor 0.
        self.listaMonticulo = [0]
        # Inicializa el tamaño actual del montículo como 0.
        self.tamanoActual = 0

    # Método para infiltrar un elemento hacia arriba en el montículo.
    def infiltArriba(self, i):
        while i // 2 > 0:
            # Compara el elemento actual con su padre y los intercambia si es necesario.
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    # Método para insertar un elemento en el montículo.
    def insertar(self, k):
        # Agrega el elemento al final de la lista.
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        # Llama a la función infiltArriba para ajustar la posición del elemento en el montículo.
        self.infiltArriba(self.tamanoActual)

    # Método para infiltrar un elemento hacia abajo en el montículo.
    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            # Compara el elemento actual con su hijo más pequeño y los intercambia si es necesario.
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    # Método para encontrar el índice del hijo más pequeño de un elemento.
    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # Método para eliminar y devolver el elemento más pequeño (mínimo) del montículo.
    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        # Llama a la función infiltAbajo para ajustar la posición del elemento en el montículo.
        self.infiltAbajo(1)
        return valorSacado

    # Método para construir un montículo a partir de una lista dada.
    def construirMonticulo(self, unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            # Llama a la función infiltAbajo para ajustar la posición de los elementos en el montículo.
            self.infiltAbajo(i)
            i = i - 1

    # Método para verificar si el montículo está vacío.
    def estaVacia(self):
        return self.tamanoActual == 0

      

