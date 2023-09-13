def ordenamiento_por_mezcla(una_lista):
    if len(una_lista) <= 1:
        return una_lista

    mitad = len(una_lista) // 2
    mitad_izquierda = una_lista[:mitad]
    mitad_derecha = una_lista[mitad:]

    mitad_izquierda = ordenamiento_por_mezcla(mitad_izquierda)
    mitad_derecha = ordenamiento_por_mezcla(mitad_derecha)

    i = j = k = 0
    while i < len(mitad_izquierda) and j < len(mitad_derecha):
        if mitad_izquierda[i] < mitad_derecha[j]:
            una_lista[k] = mitad_izquierda[i]
            i += 1
        else:
            una_lista[k] = mitad_derecha[j]
            j += 1
        k += 1

    while i < len(mitad_izquierda):
        una_lista[k] = mitad_izquierda[i]
        i += 1
        k += 1

    while j < len(mitad_derecha):
        una_lista[k] = mitad_derecha[j]
        j += 1
        k += 1
        
    return una_lista

def ordenamiento_mezcla_externo(archivo_entrada, tamaño_bloque):
    # Dividir el archivo en bloques y ordenarlos internamente
    archivo_entrada = open(archivo_entrada, 'r')
    bloques = []
    while True:
        bloque = archivo_entrada.readlines(tamaño_bloque)
        if not bloque:
            break
        bloque = [int(linea.strip()) for linea in bloque]

        ordenamiento_por_mezcla(bloque)  # Ordenar el bloque internamente con mezcla
        temp = open(temp.txt,w) as temp:
        for i in bloque:
            temp.write(i)
            temp.close()
        bloque = temp
        bloques.append(bloque)
    archivo_entrada.close()

    # Realizar la mezcla directa
    archivo_salida = open("datos_ordenados.txt", 'w')
    indices = [0] * len(bloques)

    while True:
        valores = [(bloque[indices[i]], i) for i, bloque in enumerate(bloques) if indices[i] < len(bloque)]
        if not valores:
            break

        min_valor, indice = min(valores)
        archivo_salida.write(str(min_valor) + '\n')
        indices[indice] += 1

    archivo_salida.close()

# Ejemplo de uso:
archivo_entrada = "datos.txt"
tamaño_bloque = 250000
ordenamiento_mezcla_externo(archivo_entrada, tamaño_bloque)
