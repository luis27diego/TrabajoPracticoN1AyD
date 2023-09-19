import os
import tempfile

# Esta función mezcla bloques de líneas ordenadas de varios archivos de entrada
# en un archivo de salida.
def mezclar_bloques(rutas_archivos_entrada, ruta_archivo_salida, tamaño_bloque):
    # Abre los archivos de entrada en modo lectura.
    archivo_de_entrada = [open(ruta, 'r') for ruta in rutas_archivos_entrada]
    # Abre el archivo de salida en modo escritura.
    archivo_de_salida = open(ruta_archivo_salida, 'w')

    # Lista para mantener los valores actuales leídos de cada archivo.
    valores_actuales = [None] * len(archivo_de_entrada)

    # Lee la primera línea de cada archivo y almacena los valores en valores_actuales.
    for i, archivo in enumerate(archivo_de_entrada):
        linea = archivo.readline()
        if linea:
            valores_actuales[i] = int(linea.strip())

    # Mientras haya valores en valores_actuales.
    while any(valores_actuales):
        # Encuentra el valor mínimo en valores_actuales.
        min_value = min(val for val in valores_actuales if val is not None)
        min_index = valores_actuales.index(min_value)

        # Escribe el valor mínimo en el archivo de salida.
        archivo_de_salida.write(f'{min_value}\n')

        # Lee la siguiente línea del archivo correspondiente y actualiza valores_actuales.
        linea = archivo_de_entrada[min_index].readline()
        if linea:
            valores_actuales[min_index] = int(linea.strip())
        else:
            valores_actuales[min_index] = None

    # Cierra todos los archivos.
    for archivo in archivo_de_entrada:
        archivo.close()
    archivo_de_salida.close()

# Esta función implementa el algoritmo de ordenación quicksort en una lista.
def ordenar_bloque(lista, primero, ultimo):
    if primero < ultimo:
        punto_division = particion(lista, primero, ultimo)
        ordenar_bloque(lista, primero, punto_division - 1)
        ordenar_bloque(lista, punto_division + 1, ultimo)

# Esta función realiza la partición de la lista en ordenación quicksort.
def particion(lista, primero, ultimo):
    valor_pivote = lista[primero]
    marca_izq = primero + 1
    marca_der = ultimo
    hecho = False

    while not hecho:
        while marca_izq <= marca_der and lista[marca_izq] <= valor_pivote:
            marca_izq = marca_izq + 1
        while lista[marca_der] >= valor_pivote and marca_der >= marca_izq:
            marca_der = marca_der - 1

        if marca_der < marca_izq:
            hecho = True
        else:
            temp = lista[marca_izq]
            lista[marca_izq] = lista[marca_der]
            lista[marca_der] = temp

    temp = lista[primero]
    lista[primero] = lista[marca_der]
    lista[marca_der] = temp

    return marca_der

def ordenar_archivo_grande(ruta_archivo, tamaño_bloque):
    # Obtiene el directorio temporal.
    directorio_temporal = tempfile.gettempdir()
    # Lista para mantener los nombres de los archivos temporales generados.
    archivos_temporales = []

    # Abre el archivo de entrada en modo lectura.
    with open(ruta_archivo, 'r') as archivo_entrada:
        while True:
            # Lee un bloque de líneas del archivo de entrada.
            lineas = [archivo_entrada.readline().strip() for _ in range(tamaño_bloque)]
            # Si no hay más líneas, termina el bucle.
            if not any(lineas):
                break

            # Filtra las líneas vacías o no numéricas y las ordena dentro del bloque.
            lineas = [int(linea) for linea in lineas if linea.isdigit()]

            if lineas:
                # Ordena el bloque de líneas utilizando la función 'ordenar_bloque'.
                ordenar_bloque(lineas, 0, len(lineas) - 1)

                # Crea un archivo temporal para el bloque y lo guarda en la lista.
                archivo_temporal = os.path.join(directorio_temporal, f'tmp_{len(archivos_temporales)}.txt')
                archivos_temporales.append(archivo_temporal)

                # Escribe las líneas ordenadas en el archivo temporal.
                with open(archivo_temporal, 'w') as tmp:
                    tmp.writelines([f'{linea}\n' for linea in lineas])

    # Define el nombre del archivo de salida que contendrá todos los bloques ordenados.
    archivo_salida = os.path.join(directorio_temporal, 'archivo_salida.txt')

    # Mezcla los bloques ordenados en un solo archivo ordenado final.
    while len(archivos_temporales) > 1:
        mezclar_bloques(archivos_temporales, archivo_salida, tamaño_bloque)
        archivos_temporales = [archivo_salida]
        archivo_salida = os.path.join(directorio_temporal, f'tmp_ordenado_{len(archivos_temporales)}.txt')

        # Verificar si el archivo de salida ya existe y eliminarlo si es necesario.
        if os.path.exists('archivo_salida.txt'):
            os.remove('archivo_salida.txt')

    # Renombra el archivo final y lo devuelve como resultado de la función.
    os.rename(archivos_temporales[0],"archivo_salida.txt")
    return 'archivo_salida.txt'


