class MonticuloBinarioTupla:
    def __init__(self):
        self.listaMonticulo = [(0, 0)]
        self.tamanoActual = 0

    def decrementarClave(self, vertice, nueva_distancia):
        idx = None
        for i, (distancia, v) in enumerate(self.listaMonticulo):
            if v == vertice:
                idx = i
                break

        if idx is not None and nueva_distancia < self.listaMonticulo[idx][0]:
            self.listaMonticulo[idx] = (nueva_distancia, vertice)
            self.flotar(idx)

    def flotar(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2

    def construirMonticulo(self, listaElementos):
        self.listaMonticulo = [(0, 0)] + listaElementos[:]
        self.tamanoActual = len(listaElementos)
        i = self.tamanoActual // 2
        while (i > 0):
            self.flotar(i)
            i = i - 1

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.flotar(self.tamanoActual)

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.hundir(1)
        return valorSacado

    def hundir(self, i):
        while (i * 2) <= self.tamanoActual:
            mc = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[mc][0]:
                self.listaMonticulo[i], self.listaMonticulo[mc] = self.listaMonticulo[mc], self.listaMonticulo[i]
            i = mc

    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2][0] < self.listaMonticulo[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def estaVacia(self):
        return self.tamanoActual == 0

    def tamano(self):
        return self.tamanoActual

    def construirMonticuloVacio(self):
        self.listaMonticulo = [(0, 0)]
        self.tamanoActual = 0
# ***********************************************************************************************************************************************



class ColaPrioridad:
    def __init__(self):
        self.listaMonticulo = [(0, 0)]  # Tuplas (clave, valor)
        self.tamanio = 0

    def construirMonticulo(self, lista):
        self.tamanio = len(lista)
        self.listaMonticulo = [(0, 0)] + lista[:]
        i = self.tamanio // 2
        while (i > 0):
            self.bajar(i)
            i = i - 1

    def eliminarMin(self):
        val_raiz = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanio]
        self.tamanio = self.tamanio - 1
        self.listaMonticulo.pop()
        self.bajar(1)
        return val_raiz[1]

    def decrementarClave(self, nodo, nueva_prioridad):
        idx = 0
        for i in range(1, self.tamanio + 1):
            if self.listaMonticulo[i][1] == nodo:
                idx = i
                break

        if idx > 0:
            if nueva_prioridad < self.listaMonticulo[idx][0]:
                self.listaMonticulo[idx] = (nueva_prioridad, nodo)
                self.subir(idx)

    def estaVacia(self):
        return self.tamanio == 0

    def subir(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2

    def bajar(self, i):
        while (i * 2) <= self.tamanio:
            mc = self.encontrarMinHijo(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[mc][0]:
                self.listaMonticulo[i], self.listaMonticulo[mc] = self.listaMonticulo[mc], self.listaMonticulo[i]
            i = mc

    def encontrarMinHijo(self, i):
        if i * 2 + 1 > self.tamanio:
            return i * 2
        else:
            if self.listaMonticulo[i * 2][0] < self.listaMonticulo[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1