from TP2_problema33.modulos.Vertice import Vertice

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
            if de not in self.listaVertices:
                nv = self.agregarVertice(de)
            if a not in self.listaVertices:
                nv = self.agregarVertice(a)
            self.listaVertices[de].agregarVecino(self.listaVertices[a], ponderacion,segunda_ponderacion)
            # self.listaVertices[de].segunda_ponderacion = segunda_ponderacion  # Asigna la segunda ponderación

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def camino_dijkstra(self,a,b):
        camino = []
        x = self.obtenerVertice(b.id)
        
        actual = x
        while actual !=None:
            camino.insert(0,actual.id)
            actual = actual.predecesor
            # actual = self.obtenerVertice(actual.id).predecesor
        x = self.obtenerVertice(b.id)
        return [camino, x.distancia]
    

    
    def crear_grafo_de_rutas_posibles(self, inicio, final,peso):
        grafo = Grafo()
        tabla = self.eliminar_rutas_sobrepeso(inicio,final,peso)
        # Supongamos que lista_rutas es una lista de listas de vértices que forman las rutas
        
        # Agrega las aristas al grafo basadas en las rutas
        for ruta in tabla:
            for i in range(len(ruta[3]) - 1):

                x = self.obtenerVertice(ruta[3][i])
                y = self.obtenerVertice(ruta[3][i+1])
                grafo.agregarArista(ruta[3][i], ruta[3][i+1],x.obtenerSegundaPonderacion(y))

        return grafo

    def eliminar_rutas_sobrepeso(self, inicio, final,peso_maximo):
        lista_rutas = self.todos_los_cuellos_de_botella_de_rutas_posibles(inicio,final)
        rutas_filtradas = [ruta for ruta in lista_rutas if ruta[0] >= peso_maximo]
        return rutas_filtradas

    
    def cuello_de_botella(self, inicio, final):
        c = self.todos_los_cuellos_de_botella_de_rutas_posibles(inicio, final)
        
        if not c:
            # Si c está vacía, puedes manejarlo como quieras, por ejemplo, retornar un valor predeterminado.
            return "No hay rutaas posibles"  # O cualquier otro valor que desees

        maximo_tupla = max(c, key=lambda tupla: tupla[0])
        return maximo_tupla


    def todos_los_cuellos_de_botella_de_rutas_posibles(self,inicio, final):
        cam = self.encontrador_caminos_posibles(inicio, final)
        
        contador = 0
        cuellos = []

        for camino in cam:
            contador += 1 
            cuello = (9000000000,None)
            for i in range(len(camino)):
                siguiente = i + 1

                if siguiente  < len(camino):
                    vecino = camino[siguiente]
                else:
                    break
                
                cuello_de_botella = camino[i].obtenerPonderacion(vecino)
                if cuello_de_botella < cuello[0]:
                    cuello = (cuello_de_botella , "camino "+ str(contador),"La ruta con mayor capacidad de carga:", [i.obtenerId()  for i in camino], "el cuello de botella se presenta de " + camino[i].obtenerId() + " a " + vecino.obtenerId())
            cuellos.append(cuello)
    
        
        return cuellos
    

    def encontrador_caminos_posibles(self,inicio,final):
        tabla_ver = []
        cam = self.encontrar_caminos_posibles_str(inicio,final)
        for camino in cam:
            x = []
            for _ in camino:
                x.append(self.listaVertices[_])
            tabla_ver.append(x)
        return tabla_ver   
    
    def encontrar_caminos_posibles_str(self, inicio, final):
        res = []
        camino = [inicio]
        vecinos = self.listaVertices[inicio].obtenerConexiones()

        def encontrar_caminos(inicio, final, camino, res):
            if inicio == final:
                res.append(list(camino))
            else:
                vecinos = self.listaVertices[inicio].obtenerConexiones()
                for vecino in vecinos:
                    act = vecino.obtenerId()
                    if act not in camino:
                        copia = list(camino)
                        copia.append(act)
                        encontrar_caminos(act, final, copia, res)

        for vecino in vecinos:
            act = vecino.obtenerId()
            copia = list(camino)
            copia.append(act)
            encontrar_caminos(act, final, copia, res)
        return res