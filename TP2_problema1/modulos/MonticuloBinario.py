class MonticuloMinimo:
    def __init__(self):
        self.monticulo = [0]  # Inicializar la lista con un valor ficticio (None)

    def insertar(self, elemento):
        self.monticulo.append(elemento)
        self._subir(len(self.monticulo) - 1)

    def extraer_minimo(self):
        if len(self.monticulo) <= 1:  # Verificar si el montículo está vacío
            return None

        minimo = self.monticulo[1]  # El mínimo es el segundo elemento (índice 1)
        ultimo = self.monticulo.pop()  # Obtener el último elemento
        if len(self.monticulo) > 1:  # Si todavía hay elementos en el montículo
            self.monticulo[1] = ultimo  # Mover el último elemento a la raíz
            self._bajar(1)  # Restaurar la propiedad del montículo

        return minimo

    def _subir(self, indice):
        while indice > 1:
            padre = indice // 2
            if self.monticulo[indice].get_riesgo() < self.monticulo[padre].get_riesgo():
                self.monticulo[indice], self.monticulo[padre] = self.monticulo[padre], self.monticulo[indice]
                indice = padre
            else:
                break

    def __len__(self):
        return len(self.monticulo) - 1  # Restar 1 para no contar el valor ficticio en el montículo

    def _bajar(self, indice):
        while 2 * indice < len(self.monticulo):
            hijo_izquierdo = 2 * indice
            hijo_derecho = 2 * indice + 1
            minimo = indice
            if (hijo_izquierdo < len(self.monticulo) and
                    self.monticulo[hijo_izquierdo].get_riesgo() < self.monticulo[minimo].get_riesgo()):
                minimo = hijo_izquierdo
            if (hijo_derecho < len(self.monticulo) and
                    self.monticulo[hijo_derecho].get_riesgo() < self.monticulo[minimo].get_riesgo()):
                minimo = hijo_derecho
            if minimo != indice:
                self.monticulo[indice], self.monticulo[minimo] = self.monticulo[minimo], self.monticulo[indice]
                indice = minimo
            else:
                break