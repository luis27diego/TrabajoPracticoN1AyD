# Define el tamaño máximo de una línea
MAX_LINE = 21

# Define el tamaño de los bloques iniciales
BLOCK_SIZE = 10000

# Define el nombre del archivo original
FILE_NAME = "F0.txt"

# Define los nombres de los archivos auxiliares
FILE_1 = "F1.txt"
FILE_2 = "F2.txt"
FILE_3 = "F3.txt"

# Función para intercambiar dos elementos de una lista
def swap(a, b):
  temp = a
  a = b
  b = temp

# Función para elegir un pivote aleatorio y colocarlo al final de la lista
def choose_pivot(arr, low, high):
  random_index = random.randint(low, high)
  swap(arr[random_index], arr[high])

# Función para particionar la lista según el pivote
def partition(arr, low, high):
  choose_pivot(arr, low, high)
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      swap(arr[i], arr[j])
  swap(arr[i + 1], arr[high])
  return i + 1

# Función para ordenar la lista usando quicksort
def quicksort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)

# Función para leer una línea de un archivo de texto y devolverla como una cadena
def read_line(file):
  line = file.readline()
  if line:
    return line.strip()
  else:
    return None

# Función para escribir una línea en un archivo de texto con un salto de línea al final
def write_line(file, line):
  file.write(line + "\n")

# Función para escribir un separador en un archivo de texto para indicar el fin de un bloque
def write_separator(file):
  write_line(file, "-")

# Función para comparar dos líneas y devolver la menor según el orden lexicográfico
def min_line(line1, line2):
  if line1 is None:
    return line2
  if line2 is None:
    return line1
  if line1 <= line2:
    return line1
  return line2

# Función para copiar una línea de un archivo de texto a otro y devolver la siguiente línea del archivo origen
def copy_line(source, dest):
  line = read_line(source)
  if line is not None:
    write_line(dest, line)
    return read_line(source)
  else:
    return None

# Función para copiar un bloque de un archivo de texto a otro y devolver la siguiente línea del archivo origen
def copy_block(source, dest):
  line = read_line(source)
  while line is not None and line != "-":
    write_line(dest, line)
    line = read_line(source)
  write_separator(dest) # Escribe el separador al final del bloque copiado
  return read_line(source) # Devuelve la siguiente línea después del separador

# Función para mezclar dos bloques de dos archivos de texto y escribirlos en un tercer archivo de texto
def merge_blocks(file1, file2, file3):
  line1 = read_line(file1) # Lee la primera línea del primer archivo de texto
  line2 = read_line(file2) # Lee la primera línea del segundo archivo de texto
  while line1 is not None and line2 is not None and line1 != "-" and line2 != "-":
    # Mientras no se llegue al final de ninguno de los dos bloques
    if line1 <= line2:
      # Si la línea del primer archivo es menor o igual que la del segundo
      write_line(file3, line1) # Escribe la línea del primer archivo en el tercer archivo de texto
      line1 = read_line(file1) # Lee la siguiente línea del primer archivo de texto
    else:
      # Si la línea del segundo archivo es menor que la del primero
      write_line(file3, line2) # Escribe la línea del segundo archivo en el tercer archivo de texto
      line2 = read_line(file2) # Lee la siguiente línea del segundo archivo de texto
  # Al salir del bucle, se ha terminado uno de los dos bloques
  if line1 is None or line1 == "-":
    # Si se terminó el bloque del primer archivo de texto
    while line2 is not None and line2 != "-":
      # Mientras no se termine el bloque del segundo archivo de texto
      write_line(file3, line2) # Escribe la línea del segundo archivo en el tercer archivo de texto
      line2 = read_line(file2) # Lee la siguiente línea del segundo archivo de texto
  else:
    # Si se terminó el bloque del segundo archivo de texto
    while line1 is not None and line1 != "-":
      # Mientras no se termine el bloque del primer archivo de texto
      write_line(file3, line1) # Escribe la línea del primer archivo en el tercer archivo de texto
      line1 = read_line(file1) # Lee la siguiente línea del primer archivo de texto
  write_separator(file3) # Escribe el separador al final del bloque mezclado

# Función para ordenar un archivo grande usando ordenamiento externo tipo polifase
def external_sort(file_name):
  file = open(file_name, "r+") # Abre el archivo original en modo lectura y escritura de texto
  if file is None:
    print("No se pudo abrir el archivo %s" % file_name)
    exit(1)

  file1 = open(FILE_1, "w+") # Crea y abre el primer archivo auxiliar en modo lectura y escritura de texto
  if file1 is None:
    print("No se pudo crear el archivo %s" % FILE_1)
    exit(1)

  file2 = open(FILE_2, "w+") # Crea y abre el segundo archivo auxiliar en modo lectura y escritura de texto
  if file2 is None:
    print("No se pudo crear el archivo %s" % FILE_2)
    exit(1)

  file3 = open(FILE_3, "w+") # Crea y abre el tercer archivo auxiliar en modo lectura y escritura de texto
  if file3 is None:
    print("No se pudo crear el archivo %s" % FILE_3)
    exit(1)

  buffer = [] # Crea una lista para almacenar los bloques leídos del archivo original

  n = 0 # Variable para contar el número de líneas leídas en cada bloque

  k = 0 # Variable para alternar entre los archivos auxiliares F1 y F2

  line = read_line(file) # Lee la primera línea del archivo original

  while line is not None:
    # Mientras no se llegue al final del archivo original

    n = 0 # Inicializa el contador de líneas a cero

    while line is not None and n < BLOCK_SIZE:
      # Mientras no se llegue al final del archivo original ni al tamaño máximo del bloque

      buffer.append(line) # Agrega la línea leída a la lista buffer

      n += 1 # Incrementa el contador de líneas

      line = read_line(file) # Lee la siguiente línea del archivo original

    quicksort(buffer, 0, n - 1) # Ordena la lista buffer usando quicksort

    if k == 0:
      # Si k es cero, escribe el bloque ordenado en F1
      for item in buffer:
        write_line(file1, item)
      write_separator(file1) # Escribe el separador al final del bloque
      k = 1 # Cambia k a uno para alternar entre F1 y F2
    else:
      # Si k es uno, escribe el bloque ordenado en F2
      for item in buffer:
        write_line(file2, item)
      write_separator(file2) # Escribe el separador al final del bloque
      k = 0 # Cambia k a cero para alternar entre F1 y F2

    buffer.clear() # Limpia la lista buffer para el siguiente bloque

  file.close() # Cierra el archivo original

  file.seek(0) # Coloca el puntero al inicio del archivo original

  file.truncate() # Borra el contenido del archivo original

  source1 = file1 # Inicializa el primer archivo fuente como F1

  source2 = file2 # Inicializa el segundo archivo fuente como F2

  dest = file3 # Inicializa el archivo destino como F3

  source1.seek(0) # Coloca el puntero al inicio del primer archivo fuente

  source2.seek(0)

