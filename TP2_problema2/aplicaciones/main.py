from TP2_problema2.modulos.AVl_Implementacion import AVL_Implementacion
from random import randint
from datetime import datetime, timedelta

# Función para generar una fecha aleatoria dentro de un rango específico
def fecha_aleatoria(fecha_inicio, fecha_fin):
    delta = fecha_fin - fecha_inicio
    random_days = timedelta(days=randint(0, delta.days))
    return fecha_inicio + random_days

# Crear una instancia de la clase AVL_Implementacion
avl_simulacion = AVL_Implementacion()

# Generar 500 datos ficticios y agregarlos al AVL
fecha_inicio = datetime(2022, 1, 1)
fecha_fin = datetime(2022, 12, 31)
for _ in range(15):
    fecha = fecha_aleatoria(fecha_inicio, fecha_fin).strftime("%d/%m/%Y")
    temperatura = randint(-10, 40)  # Temperaturas aleatorias entre -10°C y 40°C
    avl_simulacion.guardar_temperatura(fecha, temperatura)

# Utilizar los métodos de la clase para realizar consultas
print("Cantidad de muestras en el AVL:", avl_simulacion.cantidad_muetras())


avl_simulacion.avl_implementacion.mostrar()

fecha1 = "01/03/2022"
fecha2 = "30/06/2022"
print("Máxima temperatura en el rango:", avl_simulacion.max_temp_rango(fecha1, fecha2))
print("Mínima temperatura en el rango:", avl_simulacion.min_temp_rango(fecha1, fecha2))
print("Temperaturas en el rango:", avl_simulacion.devolver_temperaturas(fecha1, fecha2))

fecha3 = "15/04/2022"
print("Temperatura en la fecha", fecha3, ":", avl_simulacion.devolver_temperatura(fecha3))

fecha4 = "10/01/2022"
print("Borrar temperatura en la fecha", fecha4, ":", avl_simulacion.borrar_temperatura(fecha4))