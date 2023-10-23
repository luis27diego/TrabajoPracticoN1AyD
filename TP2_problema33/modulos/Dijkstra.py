from TP2_problema33.modulos.ColaDePrioridadMin import ColaPrioridadMin
from TP2_problema33.modulos.ColaDePrioridadMax import ColaPrioridadMax
import sys

def dijkstra(unGrafo, inicio):
    # Crear una cola de prioridad mínima para almacenar los vértices.
    cp = ColaPrioridadMin()

    # Inicializar todas las distancias a +infinito.
    for v in unGrafo:
        v.asignarDistancia(sys.maxsize)

    # Establecer la distancia del vértice de inicio como 0.
    x = unGrafo.obtenerVertice(inicio.id)
    x.asignarDistancia(0)

    # Construir un montículo con todas las distancias y vértices.
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])

    # Mientras la cola de prioridad no esté vacía.
    while not cp.estaVacia():
        # Obtener el vértice con la distancia mínima.
        verticeActual = cp.eliminarMin()

        # Explorar las conexiones del vértice actual.
        for verticeSiguiente in verticeActual.obtenerConexiones():
            # Calcular la nueva distancia desde el vértice actual al siguiente.
            nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)

            # Si la nueva distancia es menor que la distancia almacenada en el vértice siguiente.
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                # Actualizar la distancia del vértice siguiente.
                verticeSiguiente.asignarDistancia(nuevaDistancia)

                # Establecer el vértice actual como predecesor del vértice siguiente.
                verticeSiguiente.asignarPredecesor(verticeActual)

                # Actualizar la cola de prioridad con la nueva distancia.
                cp.decrementarClave(verticeSiguiente, nuevaDistancia)

# *********************************************************************************************************************************************
def dijkstra_cuello_botella(unGrafo, inicio, final):
    #Contador para cambiar la distancia a 0 (linea 86)
    contador = 0

    # Crear una cola de prioridad máxima para almacenar los vértices.
    cp = ColaPrioridadMax()

    # Inicializar todas las distancias a 0.
    for v in unGrafo:
        v.asignarDistancia(0)

    # Establecer la distancia del vértice de inicio como +infinito.
    x = unGrafo.obtenerVertice(inicio.id)
    x.asignarDistancia(sys.maxsize)

    # Construir un montículo con todas las distancias y vértices.
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])

    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()

        for verticeSiguiente in verticeActual.obtenerConexiones():
            # Obtener la distancia actual desde el vértice de inicio al vértice actual.
            distanciaActual = verticeActual.obtenerDistancia()

            # Obtener la ponderación entre el vértice actual y el vértice siguiente.
            ponderacion = verticeActual.obtenerPonderacion(verticeSiguiente)

            # Obtener la distancia actual almacenada en el vértice siguiente.
            obtener_distancia_ver_sig = verticeSiguiente.obtenerDistancia()

            # Encontrar el mínimo entre la distancia actual y la ponderación del vértice siguiente.
            minimo = min(distanciaActual, ponderacion)

            # Calcular la nueva distancia como el máximo entre la distancia del vértice siguiente
            # y el mínimo (cuello de botella máximo).
            nuevaDistancia = max(obtener_distancia_ver_sig, minimo)

            # Si la nueva distancia es mayor que la distancia almacenada en el vértice siguiente.
            if nuevaDistancia > verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)

                # Actualizar la cola de prioridad con la nueva distancia.
                cp.decrementarClave(verticeSiguiente, nuevaDistancia)

        contador += 1

        # Establecer la distancia del vértice de inicio a 0 después de la primera iteración.
        if verticeActual == inicio and contador == 1:
            verticeActual.asignarDistancia(0)

# *******************************************************************************************************************************************
#METODO PARA RECORRER DESDE VERTICE FINAL HASTA SUS PREDECESORES (CONTRUIR EL CAMINO)

def camino_dijkstra(unGrafo, inicio, final):
    camino = []  # Lista para almacenar el camino desde 'a' hasta 'b'.
    Vfinal = unGrafo.obtenerVertice(final.id)  # Obtener el vértice 'b'.
    actual = Vfinal  # Inicializar el vértice actual como 'b'.

    while actual is not None:
        # Insertar el vértice actual al principio de la lista 'camino'.
        camino.insert(0, actual.id)
        
        # Si el vértice 'a' es igual al vértice actual, hemos llegado al origen.
        if inicio == actual:
            # Retornar el camino y la distancia acumulada hasta 'a'.
            return [camino, Vfinal.distancia]

        # Mover al vértice predecesor en el camino más corto.
        actual = actual.predecesor

    return [camino, Vfinal.distancia]
