import sys
class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = sys.maxsize
        self.predecesor = None  # Inicializar predecesor como None

    def agregarVecino(self, vecino, ponderacion=0, segunda_ponderacion=0):
        self.conectadoA[vecino] = (ponderacion, segunda_ponderacion)

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerDistancia(self):
        return self.distancia

    def obtnervecinosenlista(self):
        return list(self.conectadoA.keys())

    def asignarDistancia(self, distancia):
        self.distancia = distancia

    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino][0]

    def obtenerSegundaPonderacion(self, vecino):
        return self.conectadoA[vecino][1]