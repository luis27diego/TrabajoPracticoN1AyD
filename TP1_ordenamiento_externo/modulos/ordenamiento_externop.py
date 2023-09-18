import os
import tempfile

def mezclar_bloques(rutas_archivos_entrada, ruta_archivo_salida, tamano_bloque):
    input_files = [open(ruta, 'r') for ruta in rutas_archivos_entrada]
    output_file = open(ruta_archivo_salida, 'w')

    current_values = [None] * len(input_files)

    for i, archivo in enumerate(input_files):
        linea = archivo.readline()
        if linea:
            current_values[i] = int(linea.strip())

    while any(current_values):
        min_value = min(val for val in current_values if val is not None)
        min_index = current_values.index(min_value)

        output_file.write(f'{min_value}\n')

        linea = input_files[min_index].readline()
        if linea:
            current_values[min_index] = int(linea.strip())
        else:
            current_values[min_index] = None

    for archivo in input_files:
        archivo.close()
    output_file.close()

def ordenar_bloque(lista, primero, ultimo):
    if primero < ultimo:
        punto_division = particion(lista, primero, ultimo)
        ordenar_bloque(lista, primero, punto_division - 1)
        ordenar_bloque(lista, punto_division + 1, ultimo)

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

def ordenar_archivo_grande(ruta_archivo, tamano_bloque):
    directorio_temporal = tempfile.gettempdir()
    archivos_temporales = []

    with open(ruta_archivo, 'r') as archivo_entrada:
        while True:
            lineas = [archivo_entrada.readline().strip() for _ in range(tamano_bloque)]
            if not any(lineas):
                break

            # Filtra las líneas vacías o no numéricas
            lineas = [int(linea) for linea in lineas if linea.isdigit()]

            if lineas:
                ordenar_bloque(lineas, 0, len(lineas) - 1)

                archivo_temporal = os.path.join(directorio_temporal, f'tmp_{len(archivos_temporales)}.txt')
                archivos_temporales.append(archivo_temporal)

                with open(archivo_temporal, 'w') as tmp:
                    tmp.writelines([f'{linea}\n' for linea in lineas])

    archivo_salida = os.path.join(directorio_temporal, 'archivo_ordenado.txt')

    while len(archivos_temporales) > 1:
        mezclar_bloques(archivos_temporales, archivo_salida, tamano_bloque)
        archivos_temporales = [archivo_salida]
        archivo_salida = os.path.join(directorio_temporal, f'tmp_ordenado_{len(archivos_temporales)}.txt')

    os.rename(archivos_temporales[0], 'archivo_ordenado.txt')
    return 'archivo_ordenado.txt'


# Ejemplo de uso
ruta_archivo = 'F0.txt'
tamano_bloque = 5000  # Tamaño del bloque (número de líneas)
archivo_ordenado = ordenar_archivo_grande(ruta_archivo, tamano_bloque)
