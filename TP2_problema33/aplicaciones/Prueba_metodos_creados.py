from TP2_problema33.modulos.Grafo import Grafo
from TP2_problema33.modulos.Dijkstra import dijkstra, dijkstra_cuello_botella, camino_dijkstra

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

# Llamamos a dijkstra_cuello_botella con Rosario como punto de inicio y La Rioja como destino
inicio = mi_grafo.obtenerVertice("Rosario")
final = mi_grafo.obtenerVertice("VillaMercedes")
print("\nEjercicio 1: Calcular el cuello de botella de una ciudad a otra")
print()

print("Cálculo del cuello de botella con Dijkstra modificado")
dijkstra_cuello_botella(mi_grafo, inicio, final)

print("\nCuello de botella máximo encontrado:")
cuello_maximo = camino_dijkstra(mi_grafo, inicio, final)
print("Camino:", cuello_maximo[0])
print("Cuello de botella máximo:", cuello_maximo[1])


print("\nCálculo de todos los cuellos de botella de rutas posibles:")
caminos_cuellos = mi_grafo.todos_los_cuellos_de_botella_de_rutas_posibles(inicio.id, final.id)
print("Todos las rutas posibles y su cuello de botella desde", inicio.id, "hasta", final.id)
print()

for camino in caminos_cuellos:
    print("Camino:", camino[1])
    print("Ruta con mayor capacidad de carga:", camino[3])
    print("Cuello de botella en el tramo:", camino[4])
    print("valor del cuello de botella:",camino[0])
    print()

print("\n" + "---- " * 35)  # Imprimir una línea de caritas en movimiento

print("\nEjercicio 2: Calcular el camino menos costoso que pueda transportar un peso dado:")
print()
# Supongamos que deseas encontrar el camino menos costoso que pueda transportar un peso de 40
peso_deseado = 40
grafiño = mi_grafo.crear_grafo_de_rutas_posibles(inicio.id, final.id, peso_deseado)

dijkstra(grafiño, inicio)

print("Camino menos costoso que pueda transportar un peso de", peso_deseado, "desde", inicio.id, "hasta", final.id)
camino_menos_costoso = camino_dijkstra(grafiño, inicio, final)
print("Camino:", camino_menos_costoso[0])
print("Costo total del camino:", camino_menos_costoso[1])

print()

# Supongamos que ahora tienes un nuevo método crear_grafo_de_rutas_posibles_peso_max

grafo_ruta_barata_max_peso = mi_grafo.crear_grafo_de_rutas_posibles_peso_max(inicio, final)
dijkstra(grafo_ruta_barata_max_peso, inicio)

# Llamar a la función 'camino_dijkstra' para encontrar el camino resultante
camino_resultante = camino_dijkstra(grafo_ruta_barata_max_peso, inicio, final)

print("Camino más barato con peso máximo de", cuello_maximo[1])
print("Camino:", camino_resultante[0])
print("Costo total del camino:", camino_resultante[1])
print()
