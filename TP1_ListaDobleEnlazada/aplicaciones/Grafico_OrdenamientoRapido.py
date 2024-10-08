from TP1_ListaDobleEnlazada.modulos.ListaDobleEnlazada import ListaDobleEnlazada
import random
import time
import matplotlib.pyplot as plt

# Función para generar una lista de números aleatorios
def generar_lista_aleatoria(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Función que ejecuta QuickSort y mide el tiempo
def tiempo_ordenar(lista):
    inicio = time.time()
    lista.ordenar()  # Llama a tu método QuickSort aquí
    fin = time.time()
    return fin - inicio

tamaños = [1000,3000,7000,10000,20000,30000]  # Cambia estos valores según tus necesidades
tiempos = []

for n in tamaños:
    lista_aleatoria = generar_lista_aleatoria(n)
    # Crea una instancia de tu clase ListaDobleEnlazada y agrega los elementos aleatorios
    lista_doble = ListaDobleEnlazada()
    for elemento in lista_aleatoria:
        lista_doble.agregar_al_final(elemento)
    
    tiempo = tiempo_ordenar(lista_doble.copiar())  # Usar una copia para no alterar la lista original
    tiempos.append(tiempo)

# Grafica los resultados
plt.plot(tamaños, tiempos, marker='o')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Rendimiento de QuickSort para ListaDobleEnlazada')
plt.grid(True)
plt.show()