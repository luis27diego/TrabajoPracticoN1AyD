def ordenamientoRapido(unaLista):
   ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)

def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
   if primero<ultimo:

       puntoDivision = particion(unaLista,primero,ultimo)

       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)


def particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False
   while not hecho:

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp

   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp


   return marcaDer

# Función principal de ordenamiento externo
def split_file(input_filename, block_size):
    with open(input_filename, 'r') as infile:
        archi1_flag = True  # Bandera para alternar entre archi1 y archi2
        archi1_filename = 'archi1.txt'
        archi2_filename = 'archi2.txt'
        archi1_count = 0
        archi2_count = 0

        with open(archi1_filename, 'w') as f1file, open(archi2_filename, 'w') as f2file:
            while True:
                block = []
                for _ in range(block_size):
                    line = infile.readline().rstrip('\n')
                    if not line:
                        break
                    block.append(line)

                if not block:
                    break

                ordenamientoRapido(block)

                if archi1_flag:
                    f1file.writelines([line + '\n' for line in block])
                    archi1_count += len(block)
                else:
                    f2file.writelines([line + '\n' for line in block])
                    archi2_count += len(block)

                archi1_flag = not archi1_flag





input_file = "F0.txt"
output_file = "archivo_ordenado.txt"
block_size = 100

split_file(input_file, block_size)


def merge_blocks(block1, block2, output, block_size):
    with open(block1, 'r') as file1, open(block2, 'r') as file2, open(output, 'w') as out_file:
        lines_written = 0

        line1 = file1.readline().strip()
        line2 = file2.readline().strip()

        while line1 or line2:
            num1 = int(line1) if line1 else float('inf')
            num2 = int(line2) if line2 else float('inf')

            while num1 < float('inf') or num2 < float('inf'):
                if num1 < num2:
                    out_file.write(line1 + '\n')
                    line1 = file1.readline().strip()
                    num1 = int(line1) if line1 else float('inf')
                else:
                    out_file.write(line2 + '\n')
                    line2 = file2.readline().strip()
                    num2 = int(line2) if line2 else float('inf')

                lines_written += 1

                if lines_written == block_size:
                    break

    return lines_written

# Ejemplo de uso
block1_filename = 'archi1.txt'
block2_filename = 'archi2.txt'
output_filename = 'archi3.txt'
block_size = 100

lines_written = merge_blocks(block1_filename, block2_filename, output_filename, block_size)

print(f'{lines_written} líneas escritas en {output_filename}')

