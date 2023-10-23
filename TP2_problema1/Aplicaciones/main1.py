import time
import datetime
from TP2_problema1.modulos.paciente import Paciente 
import random
from TP2_problema1.modulos.MonticuloPaciente import MonticuloBinarioPaciente


n = 20  # cantidad de ciclos de simulación

cola_de_espera = MonticuloBinarioPaciente()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = Paciente()
    cola_de_espera.ingresar_paciente(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.atender()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)

# Una vez que no ingresen más pacientes, atender a todos los pacientes restantes en la fila de espera
print('No se ingresarán más pacientes. Atendiendo a los pacientes restantes...')
while len(cola_de_espera) > 0:
    paciente_atendido = cola_de_espera.atender()
    print('*'*40)
    print('Se atiende el paciente:', paciente_atendido)
    print('*'*40)
    time.sleep(1)

print('Todos los pacientes han sido atendidos.')