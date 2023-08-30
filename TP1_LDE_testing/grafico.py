import matplotlib.pyplot as plt
import time

def algoritmo(n):
    
    for i in range(n):
        actualizador = 0 
        for i in range(n):
            actualizador += 1

# analisis 
tan = [10, 100, 1000]
tiempo = []
for cantidad in tan():
    tini = time.time()
    algoritmo(cantidad)
    tfin = time.time()

    duracion = tfin - tini
    tiempo.append(duracion)

print(tiempo)