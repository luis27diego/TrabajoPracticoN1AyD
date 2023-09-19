from TP1_ListaDobleEnlazada.modulos.ListaDobleEnlazada import ListaDobleEnlazada
import random
from TP1_juego_guerra.modulos.Cartas import Carta  # Importa la clase Carta desde el archivo carta.py

valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['♠', '♥', '♦', '♣']

class Mazo:
    def __init__(self,semilla=None):
        self.mazo = []
        self.jugador_1 = ListaDobleEnlazada()   # Mazo del jugador 1.
        self.jugador_2 = ListaDobleEnlazada()   # Mazo del jugador 2.

        # Creación del mazo de cartas, combinando valores y palos.
        for valor in valores:
            for palo in palos:
                self.mazo.append(Carta(valor,palo))

        if semilla is not None:
            random.seed(semilla)    # Inicialización de la semilla para la aleatoriedad.

        self.barajador()        # Barajar el mazo.

    # Método para barajar el mazo de cartas.
    def barajador(self):

        # Verificar si el mazo no está vacío antes de barajar.
        if self.mazo:

            # Se barajea el mazo.
            self.mazo = random.sample(self.mazo, len(self.mazo))


        # Método para pasar de una lista de python a una ListaDobleEnlazada
        def pasador(self):
            
            lista = ListaDobleEnlazada()   # Se crea una ListaDobleEnlazada
            for carta in self.mazo:
                lista.agregar_al_final(carta)   # Se agregan las cartas a ListaDobleEnlazada
            self.mazo = lista    # Ahora self.mazo va a ser una ListaDobleEnlazada

        pasador(self)

        # Método para repartir las cartas a los dos jugadores.    
        def repartir(self):
            for _ in range(26):    # For para extraer las cartas del mazo, repartirlas y agregarlas a los jugadores.
                carta1 = self.mazo.extraer(0)
                carta2 = self.mazo.extraer(0)
                self.jugador_1.agregar_al_inicio(carta1)
                self.jugador_2.agregar_al_inicio(carta2)

        repartir(self)
        
    # Método para poner en la parte superior del mazo.   
    def poner_arriba(self,Carta):
        self.mazo.agregar_al_inicio(Carta)

    # Método para poner abajo del mazo.  
    def poner_abajo(self, carta):
        self.mazo.agregar_al_final(carta)

    # Método para sacar cartas en la parte superior del mazo.   
    def sacar_arriba(self):
        if self.mazo:
            return self.mazo.extraer(0)
        else:
            return None