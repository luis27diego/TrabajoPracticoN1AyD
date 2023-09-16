import os

class ExternalSort:
    def __init__(self, input_file, output_file, block_size=200):
        self.input_file = input_file
        self.output_file = output_file
        self.block_size = block_size
        self.temp_dir = "temp"
        os.makedirs(self.temp_dir, exist_ok=True)

    def sort(self):
        # Divide el archivo en bloques, ordena cada bloque y guarda los bloques temporales
        self.divide_and_sort()

        # Mezcla los bloques temporales en un solo archivo ordenado
        self.merge_blocks()

    def divide_and_sort(self):
        block_num = 0
        with open(self.input_file, 'r') as input_file:
            while True:
                lines = []
                for _ in range(self.block_size):
                    line = input_file.readline().strip()
                    if not line:
                        break
                    lines.append(line)

                if not lines:
                    break

                # Ordena las líneas del bloque y guárdalas en un archivo temporal
                block_file = os.path.join(self.temp_dir, f"block_{block_num}.txt")
                lines.sort(key=int)
                with open(block_file, 'w') as block:
                    block.writelines(line + '\n' for line in lines)

                block_num += 1

    def merge_blocks(self):
        block_files = [os.path.join(self.temp_dir, f"block_{i}.txt") for i in range(len(os.listdir(self.temp_dir)))]

        # Abre los bloques temporales para lectura
        block_readers = [open(file, 'r') for file in block_files]

        # Acumula todas las líneas de los bloques temporales en una lista
        all_lines = []
        for block_reader in block_readers:
            lines = block_reader.readlines()
            all_lines.extend(lines)

        # Ordena todas las líneas en orden ascendente
        all_lines.sort(key=int)

        # Escribe las líneas ordenadas en el archivo de salida final
        with open(self.output_file, 'w') as final_output:
            final_output.writelines(all_lines)

        # Cierra todos los archivos
        for block_reader in block_readers:
            block_reader.close()

        # Elimina los archivos temporales
        for file in block_files:
            os.remove(file)



if __name__ == "__main__":
    input_file = "F0.txt"
    output_file = "output.txt"
    sorter = ExternalSort(input_file, output_file)
    sorter.sort()
