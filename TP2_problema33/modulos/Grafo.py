from TP2_problema33.modulos.Vertice import Vertice
from TP2_problema33.modulos.Dijkstra import dijkstra_cuello_botella, camino_dijkstra

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self, de, a, ponderacion=0, segunda_ponderacion=0):
        # Verifica si el vértice 'de' no está en la lista de vértices y, si no está, lo agrega.
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        
        # Verifica si el vértice 'a' no está en la lista de vértices y, si no está, lo agrega.
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        
        # Agrega el vértice 'a' como vecino del vértice 'de' con la ponderación y segunda ponderación especificadas.
        self.listaVertices[de].agregarVecino(self.listaVertices[a], ponderacion, segunda_ponderacion)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def crear_grafo_de_rutas_posibles_peso_max(self, inicio, final):
        # Ejecuta el algoritmo dijkstra_cuello_botella para encontrar el cuello de botella del camino óptimo.
        dijkstra_cuello_botella(self, inicio, final)
        
        # Obtiene el valor del cuello de botella calculado en el paso anterior.
        cuello = camino_dijkstra(self, inicio, final)[1]
        
        # Crea un nuevo grafo vacío.
        grafo = Grafo()
        
        # Obtiene los identificadores de inicio y final para asi ser pasados al metodo eliminar_rutas_posibles.
        inicio = inicio.id
        final = final.id
        
        # Obtiene una tabla de rutas filtradas que cumplen con el cuello de botella calculado.
        tabla = self.eliminar_rutas_sobrepeso(inicio, final, cuello)

        for ruta in tabla:
            for i in range(len(ruta[3]) - 1):
                # Itera a través de los vértices de la ruta.

                x = self.obtenerVertice(ruta[3][i])  # Obtiene el vértice 'x'.
                y = self.obtenerVertice(ruta[3][i+1])  # Obtiene el vértice 'y'.

                # Agrega una arista entre los vértices 'x' e 'y' con el peso de la segunda ponderación.
                grafo.agregarArista(ruta[3][i], ruta[3][i+1], x.obtenerSegundaPonderacion(y))

        return grafo  # Retorna el nuevo grafo basado en las rutas filtradas para luego utilizar dijkstra y encontrar el mínimo costo.
    
    
    def crear_grafo_de_rutas_posibles(self, inicio, final, peso):
        grafo = Grafo()  # Crea un nuevo grafo vacío.
        tabla = self.eliminar_rutas_sobrepeso(inicio, final, peso)
        # Supongamos que 'tabla' es una lista de rutas filtradas con cuellos de botella dentro del peso especificado.

        # Agrega las aristas al grafo basadas en las rutas
        for ruta in tabla:
            for i in range(len(ruta[3]) - 1):  # "ruta[3]" porque la tupla tiene en su elemento 3 la lsita de vertices de la ruta
                # Itera a través de los vértices de la ruta.

                x = self.obtenerVertice(ruta[3][i])  # Obtiene el vértice 'x'.
                y = self.obtenerVertice(ruta[3][i+1])  # Obtiene el vértice 'y'.

                # Agrega una arista entre los vértices 'x' e 'y' con el peso de la segunda ponderación.
                grafo.agregarArista(ruta[3][i], ruta[3][i+1], x.obtenerSegundaPonderacion(y))

        return grafo  # Retorna el nuevo grafo basado en las rutas filtradas para luego utilizar dijkstra y econtrar el minimo costo


    def eliminar_rutas_sobrepeso(self, inicio, final, peso_maximo):
        # Obtiene la lista de todos los cuellos de botella de rutas posibles entre el vértice de inicio y el vértice final.
        lista_rutas = self.todos_los_cuellos_de_botella_de_rutas_posibles(inicio, final)

        # Filtra las rutas que tienen un cuello de botella mayor o igual al peso máximo especificado.
        rutas_filtradas = [ruta for ruta in lista_rutas if ruta[0] >= peso_maximo]

        return rutas_filtradas  # Retorna la lista de rutas filtradas con cuellos de botella dentro del peso especificado.

    def todos_los_cuellos_de_botella_de_rutas_posibles(self, inicio, final):
        # Encuentra todos los caminos posibles entre el vértice de inicio y el vértice final.
        cam = self.encontrador_caminos_posibles(inicio, final)
        
        contador = 0  # Inicializa un contador para llevar un seguimiento de los caminos.
        cuellos = []  # Inicializa una lista para almacenar los cuellos de botella encontrados.

        for camino in cam:
            contador += 1  # Incrementa el contador para identificar el camino actual.
            cuello = (9000000000, None)  # Inicializa el cuello de botella con un valor alto y sin información.
            
            for i in range(len(camino)-1): # for para iterar las sublistas que contienen a la ruta y obtener su cuello de botella

                siguiente = i + 1
                vecino = camino[siguiente]  # Obtiene el vértice vecino en el camino.
                cuello_de_botella = camino[i].obtenerPonderacion(vecino)
                # Calcula el cuello de botella entre el vértice actual y su vecino.

                if cuello_de_botella < cuello[0]:
                    # Si el cuello de botella actual es menor que el registrado anteriormente.
                    cuello = (cuello_de_botella, "camino " + str(contador),
                            "La ruta:", [i.obtenerId() for i in camino],
                            "el cuello de botella se presenta de " + camino[i].obtenerId() + " a " + vecino.obtenerId())
                    # Actualiza el cuello de botella con la nueva información.

            cuellos.append(cuello)  # Agrega el cuello de botella del camino actual a la lista.

        return cuellos  # Retorna la lista de cuellos de botella encontrados.

    
    def encontrador_caminos_posibles(self,inicio,final):
        tabla_ver = []
        cam = self.encontrar_caminos_posibles_str(inicio,final)
        for camino in cam:
            x = []
            for _ in camino:
                x.append(self.listaVertices[_])
            tabla_ver.append(x)
        return tabla_ver   
    
# Este metodo emplea el algortimo de Búsqueda en profundidad o tambien conocida como busqueda exhaustiva, pero con ciertas modificanciones
    def encontrar_caminos_posibles_str(self, inicio, final):
        res = []  # Inicializa una lista para almacenar los caminos encontrados.
        camino = [inicio]  # Inicializa una lista para representar el camino actual, empezando desde el vértice de inicio.
        vecinos = self.listaVertices[inicio].obtenerConexiones()  # Obtiene los vecinos del vértice de inicio.

        def encontrar_caminos(inicio, final, camino, res):
            # Función recursiva para encontrar caminos desde el vértice 'inicio' al vértice 'final'.
            if inicio == final:
                res.append(list(camino))  # Si se llega al vértice final, se añade el camino a la lista de resultados.
            else:
                vecinos = self.listaVertices[inicio].obtenerConexiones()  # Obtiene los vecinos del vértice actual.
                for vecino in vecinos:
                    act = vecino.obtenerId()  # Obtiene el ID del vecino.
                    if act not in camino:  # Verifica que el vecino no esté en el camino actual para evitar ciclos.
                        copia = list(camino)  # Crea una copia del camino actual.
                        copia.append(act)  # Agrega el vecino al camino copiado.
                        encontrar_caminos(act, final, copia, res)  # Llama a la función recursivamente.

        for vecino in vecinos:
            act = vecino.obtenerId()  # Obtiene el ID del vecino.
            copia = list(camino)  # Crea una copia del camino actual.
            copia.append(act)  # Agrega el vecino al camino copiado.
            encontrar_caminos(act, final, copia, res)  # Llama a la función recursiva para encontrar caminos desde el vecino al final.
        return res  # Retorna la lista de caminos encontrados.
    


