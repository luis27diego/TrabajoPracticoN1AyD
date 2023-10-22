from TP2_problema33.modulos.Grafo import Grafo
from TP2_problema33.modulos.Dijkstra import dijkstra,dijkstra_cuello_botella, camino_dijkstra__o


mi_grafo = Grafo()

with open("rutas.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.rstrip()
        datos = linea.split(",")
        if len(datos) == 4:
            ciudad_origen, ciudad_destino, peso, precio = datos
            peso = int(peso)
            precio = int(precio)  # Convierte la segunda ponderación a entero
            mi_grafo.agregarArista(ciudad_origen, ciudad_destino, peso, precio)


# Llamamos a dijkstra_max_weight con Buenos Aires como punto de inicio
inicio = mi_grafo.obtenerVertice("Rosario")
final = mi_grafo.obtenerVertice("LaRioja")

print("1")
dijkstra_cuello_botella(mi_grafo,inicio,final)
print("Cuello de botella dijiktra super eficiente")
print(camino_dijkstra__o(mi_grafo,inicio,final))


print("1 alternativo")

caminos = mi_grafo.todos_los_cuellos_de_botella_de_rutas_posibles(inicio.id, final.id)
c = mi_grafo.cuello_de_botella(inicio.id,final.id)
print()

print("Todos las rutas posibles y su cuello de botella desde", inicio.id, "hasta", final.id, "\n \n", caminos)



print()

print("El camino con el maximo cuello de botella desde", inicio.id, "hasta", final.id, "\n \n",c)

print() 


print("Ejercicio 2")
grafiño = mi_grafo.crear_grafo_de_rutas_posibles(inicio.id,final.id,40)


dijkstra(grafiño,inicio)
print("El camino menos costoso que pueda transportar un peso dado desde", inicio.id, "hasta", final.id, "\n \n")
print(camino_dijkstra__o(grafiño,inicio,final))