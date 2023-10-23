class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = None # Inicializar distancia como None
        self.predecesor = None  # Inicializar predecesor como None

    def agregarVecino(self, vecino, ponderacion=0, segunda_ponderacion=0):
        # Agrega el vértice 'vecino' como un vecino del vértice actual, junto con las ponderaciones especificadas.
        self.conectadoA[vecino] = (ponderacion, segunda_ponderacion) # Una tupla para poder almacenar ambas ponderaciones (peso y precio)

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerDistancia(self):
        return self.distancia

    def asignarDistancia(self, distancia):
        self.distancia = distancia

    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor

    def obtenerPonderacion(self, vecino):
        # Retorna la ponderación entre el vértice actual y el vértice 'vecino'.
        return self.conectadoA[vecino][0]

    def obtenerSegundaPonderacion(self, vecino):
        # Retorna la segunda ponderación entre el vértice actual y el vértice 'vecino'.
        return self.conectadoA[vecino][1]
