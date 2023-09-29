from TP2_problema1.modulos.MonticuloBinario import MonticuloBinario

class MonticuloBinarioPaciente:
    def __init__(self):
        self.monticulo = MonticuloBinario()  # Crear una instancia de MonticuloBinario

    def ingresar_paciente(self, paciente):
        self.monticulo.insertar(paciente)

    def ateneder(self):
        return self.monticulo.eliminarMin()

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.monticulo.tamanoActual:
            result = self.monticulo.listaMonticulo[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
       
    def __len__(self):
        return self.monticulo.tamanoActual