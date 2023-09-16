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


import os
import tempfile

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




def len_F0(input_filename):
    with open(input_filename,"r") as F0:
        contador = 0
        for _ in F0:
            contador += 1 

    return contador

# Ejemplo de uso
input_file = "F0.txt"
output_file = "archivo_ordenado.txt"
block_size = 100

split_file(input_file, block_size)

x = len_F0("archi1.txt")
print(x)









#Se leen archi1 y archi2 para combinarlos y escribir en archi3 y archi4
def mezclador(archi1, archi2, archi3, archi4, max_lines=200):
    flag = True


    while True:
        if flag:
            done = escritor(archi1, archi2, archi3, max_lines)
        else:
            done = escritor(archi1, archi2, archi4, max_lines)

        flag = not flag

        if done:
            break  # Terminar si uno de los archivos llegó al final

def escritor(archi1, archi2, archi_salida, max_lines=200):
    with open(archi1, 'r') as file1, open(archi2, 'r') as file2, open(archi_salida, 'a') as output_file:
        lines_written = 0
        both_files_empty = False  # Bandera para indicar que ambos archivos están vacíos

        while not both_files_empty and lines_written < max_lines:
            line1 = file1.readline().strip()
            line2 = file2.readline().strip()

            if not line1 and not line2:
                both_files_empty = True  # Ambos archivos llegaron al final
                break  # Salir del bucle si ambos archivos están vacíos

            num1 = int(line1) if line1 else float('inf')
            num2 = int(line2) if line2 else float('inf')

            while lines_written < max_lines:
                if num1 < num2:
                    output_file.write(str(num1) + '\n')
                    line1 = file1.readline().strip()
                    num1 = int(line1) if line1 else float('inf')
                else:
                    output_file.write(str(num2) + '\n')
                    line2 = file2.readline().strip()
                    num2 = int(line2) if line2 else float('inf')

                lines_written += 1

        return both_files_empty
# Resto del código sin cambios


# Resto del código sin cambios


# Llama a la función mezclador y escritor con los nombres de los archivos
archivo1 = 'archi1.txt'
archivo2 = 'archi2.txt'
archivo3 = 'archi3.txt'
archivo4 = 'archi4.txt'

mezclador(archivo1, archivo2, archivo3, archivo4, max_lines=200)
#     with open(archi1, 'r') as archi1 , open(archi2, 'r') as archi2:

#         with open("archi3.txt", 'w') as archi3, open("archi4.txt","w") as archi4:
                    

#             # for para leer archi1 y archi2 y combinarlo en archi3
#             flag = True
#             cant_blqoues = (len_F0(input_file) // block_size)
#             # if cant_blqoues %2 == 0:
#             #     cant_blqoues = cant_blqoues
#             # else: 
#             #     cant_blqoues +=1

            
#             for _ in range (cant_blqoues//2):
#                 rango = block_size *2
            
            
#                 line1 = archi1.readline().rstrip('\n')
#                 line2 = archi2.readline().rstrip('\n')

#                 num1 = int(line1)
#                 num2 = int(line2)
#                 contador = 0
#                 contador1 = 0

#                 if flag:
#                     for _ in range(rango):
#                         num1 = int(line1)
#                         num2 = int(line2)    

#                         if not line1 or not line2:
#                             break

#                         if num1 < num2:
#                             archi3.write(str(num1) + '\n')
#                             line1 = archi1.readline().strip('\n')  # Leer la siguiente línea del primer bloque
#                             contador +=1
#                             if contador == block_size:
#                                 break

#                         else:
#                             archi3.write(str(num2) + '\n')
#                             line2 = archi2.readline().strip('\n')  # Leer la siguiente línea del segundo bloque
#                             contador1 += 1
#                             if contador1 == block_size:
#                                 break
                            
#                     if contador != rango//2:
#                         for i in range(block_size - contador):
#                             archi3.write(line1 + '\n')
#                             line1 = archi1.readline().strip('\n')
                            

#                     if contador1 != rango//2:
#                         for i in range (block_size - contador1):
#                             archi3.write(line2 + '\n')
#                             line2 = archi2.readline().strip('\n')
                        
#                 else:
#                 # for para leer archi1 y archi2 y combinarlo en archi4
                    
#                     # line1 = archi1.readline().rstrip('\n')
#                     # line2 = archi2.readline().rstrip('\n')

#                     # num1 = int(line1)
#                     # num2 = int(line2)
#                     # contador = 0
#                     # contador1 = 0

#                     for _ in range(rango):
#                         num1 = int(line1)
#                         num2 = int(line2)

#                         if not line1 or not line2:
#                             break

#                         if num1 < num2:
#                             archi4.write(str(num1) + '\n')
#                             line1 = archi1.readline().strip('\n')  # Leer la siguiente línea del primer bloque
#                             contador +=1
#                             if contador == block_size:
#                                 break

#                         else:
#                             archi4.write(str(num2) + '\n')
#                             line2 = archi2.readline().strip('\n')  # Leer la siguiente línea del segundo bloque
#                             contador1 += 1
#                             if contador1 == block_size:
#                                 break

#                     if contador != block_size:
#                         for i in range(block_size - contador):
#                             archi4.write(line1 + '\n')
#                             line1 = archi1.readline().strip('\n')
#                     else:
#                         for i in range (block_size - contador1):
#                             archi4.write(line2 + '\n')
#                             line2 = archi2.readline().strip('\n')
#                 flag = not flag


# mezclador("archi1.txt","archi2.txt",block_size)



# Definir los nombres de los archivos de entrada y el archivo de salida
# archivo1 = 'archi1.txt'
# archivo2 = 'archi2.txt'
# archivo3 = 'archi3.txt'
# archivo4 = "archi4.txt"

# # Abrir el archivo de salida para escritura
# with open(archivo3, 'w') as output_file, open(archivo4, "w") as output_file2:

#     mezclador(archivo1,archivo2,archivo3,archivo4,max_lines=200)

# El contenido de las primeras 200 líneas de lox    s bloques ordenados ha sido fusionado y almacenado en 'resultado.txt'


#     # Se leen los archivos archi3 y archi4 para combinarlos y pasarlos a archi1 y archi2

#     with open(archi3, 'r') as archi3 , open(archi4, 'r') as archi4:

#         with open(archi1, 'w') as archi1, open(archi2,"w") as archi2:

#             line1 = archi3.readline().rstrip('\n')
#             line2 = archi4.readline().rstrip('\n')

#             num1 = int(line1)
#             num2 = int(line2)
#             contador = 0


#             # for para leer archi3 y archi4 y escribirlo en archi1

#             for _ in range(block_size*2):

#                 if not line1 or line2:
#                     break

#                 if num1 < num2:
#                     archi1.write(str(num1) + '\n')
#                     line1 = archi3.readline().strip()  # Leer la siguiente línea del primer bloque
#                     contador +=1

#                 else:
#                     archi1.write(str(num2) + '\n')
#                     line2 = archi4.readline().strip()  # Leer la siguiente línea del segundo bloque
                    
#             if contador != block_size:
#                 for i in range(final - contador):
#                     archi1.write(line1 + '\n')
#                     line1 = archi1.readline().strip()
#             else:
#                 for i in range (final - contador):
#                     archi1.write(line2 + '\n')
#                     line2 = archi2.readline().strip()

#             # for para leer archi3 y archi4 y escribirlo en archi2 

#             for _ in range(block_size*2):

#                 if not line1 or line2:
#                     break

#                 if num1 < num2:
#                     archi2.write(str(num1) + '\n')
#                     line1 = archi3.readline().strip()  # Leer la siguiente línea del primer bloque
#                     contador +=1

#                 else:
#                     archi2.write(str(num2) + '\n')
#                     line2 = archi4.readline().strip()  # Leer la siguiente línea del segundo bloque
                    
#             if contador != block_size:
#                 for i in range(final - contador):
#                     archi2.write(line1 + '\n')
#                     line1 = archi1.readline().strip()
#             else:
#                 for i in range (final - contador):
#                     archi2.write(line2 + '\n')
#                     line2 = archi2.readline().strip()
    



            
            



    


