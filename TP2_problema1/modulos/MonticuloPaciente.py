from TP2_problema1.modulos.MonticuloBinario import MonticuloBinario

class MonticuloBinarioPaciente:
    def __init__(self):
        # Inicializa el montículo binario de pacientes como una instancia de MonticuloBinario.
        self.monticulo = MonticuloBinario()

    def ingresar_paciente(self, paciente):
        # Método para ingresar un paciente al montículo.
        self.monticulo.insertar(paciente)

    def atender(self):
        # Método para atender al paciente de mayor prioridad, que es el paciente con la máxima urgencia.
        return self.monticulo.eliminarMin()

    def __iter__(self):
        # Inicializa el iterador para recorrer el montículo.
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.monticulo.tamanoActual:
            # Si hay más elementos en el montículo, devuelve el siguiente paciente.
            result = self.monticulo.listaMonticulo[self.n]
            self.n += 1
            return result
        else:
            # Cuando se recorren todos los pacientes, se lanza StopIteration para indicar el final del recorrido.
            raise StopIteration

    def __len__(self):
        # Devuelve la cantidad de pacientes en el montículo, que es igual al tamaño actual del montículo.
        return self.monticulo.tamanoActual
