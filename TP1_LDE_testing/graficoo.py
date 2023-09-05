import matplotlib.pyplot as plt
import numpy as np
import time

def algoritmo(n):
    
    for i in range(n):
        actualizador = 0 
        for i in range(n):
            actualizador += 1

# analisis 
# tan = [10,50, 100, 500, 1000,5000]
tam = np.logspace(10,1000,10 )
tiempo = []
for cantidad in tam:
    tini = time.time()
    algoritmo(int(cantidad))
    tfin = time.time()

    duracion = tfin - tini
    tiempo.append(duracion)

print(tiempo)

plt.plot(tam, tiempo, ".")