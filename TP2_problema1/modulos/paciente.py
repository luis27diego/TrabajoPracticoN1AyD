# -*- coding: utf-8 -*-

from random import randint, choices

from random import randint, choices

# Listas de nombres y apellidos para generar pacientes aleatorios.
nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

# Niveles de riesgo y descripciones asociadas a los niveles.
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']

# Probabilidades de aparición de cada tipo de paciente (deben sumar 1).
probabilidades = [0.1, 0.3, 0.6]

class Paciente:
    def __init__(self):
        # Genera un paciente aleatorio.
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    # Método para obtener el nombre del paciente.
    def get_nombre(self):
        return self.__nombre
    
    # Método para obtener el apellido del paciente.
    def get_apellido(self):
        return self.__apellido
    
    # Método para obtener el riesgo del paciente.
    def get_riesgo(self):
        return self.__riesgo
    
    # Método para obtener la descripcion del paciente.
    def get_descripcion_riesgo(self):
        return self.__descripcion

    def __str__(self):
        # Representación en cadena del paciente.
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad

    # Método especial para comparación de igualdad (==).
    def __eq__(self, otro):
        return (self.__nombre == otro.__nombre and
                self.__apellido == otro.__apellido and
                self.__riesgo == otro.__riesgo)

    # Método especial para comparación de menor que (<).
    def __lt__(self, otro):
        return self.__riesgo < otro.__riesgo

    # Método especial para comparación de mayor que (>).
    def __gt__(self, otro):
        return self.__riesgo > otro.__riesgo
   
        
        
        