from TP2_problema33.modulos.ColaDePrioridadTuplas import ColaPrioridad

def dijkstra(unGrafo,inicio):
    cp = ColaPrioridad()
    x = unGrafo.obtenerVertice(inicio.id)
    x.asignarDistancia(0)
    # inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)