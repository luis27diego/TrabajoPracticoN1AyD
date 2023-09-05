from TP1_LDE_testing.main import ListaDobleEnlazada
import random


valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['♠', '♥', '♦', '♣']

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f'{self.valor}{self.palo}'
    

class JuegoGuerra:
    def __init__(self, semilla=None):
        self.random = random.Random(semilla)
        self.mazo = ListaDobleEnlazada()
        for valor in valores:
            for palo in palos:
                self.mazo.agregar_al_final(Carta(valor, palo))



    def jugar(self):
        jugador1 = ListaDobleEnlazada()
        jugador2 = ListaDobleEnlazada()
        mesa = ListaDobleEnlazada()
        turnos = 0

        def guerra():
            nonlocal turnos
            turnos += 1
            print(f'Turno {turnos} - Guerra dentro de la Guerra!')

            # Agregar las dos cartas iniciales de la Guerra a la mesa
            mesa.agregar_al_final(carta_jugador1)
            mesa.agregar_al_final(carta_jugador2)

            # Agregar 3 cartas boca abajo de cada jugador a la mesa
            cartas_guerra = []  # Lista para almacenar todas las cartas de la Guerra
            for _ in range(3):
                if not jugador1.esta_vacio():
                    carta_jugador1 = jugador1.extraer(0)
                    mesa.agregar_al_final(carta_jugador1)
                    cartas_guerra.append(carta_jugador1)
                if not jugador2.esta_vacio():
                    carta_jugador2 = jugador2.extraer(0)
                    mesa.agregar_al_final(carta_jugador2)
                    cartas_guerra.append(carta_jugador2)

            # Voltear una carta boca arriba de cada jugador y agregarlas a la mesa
            if not jugador1.esta_vacio():
                carta_jugador1 = jugador1.extraer(0)
                mesa.agregar_al_final(carta_jugador1)
                cartas_guerra.append(carta_jugador1)
            if not jugador2.esta_vacio():
                carta_jugador2 = jugador2.extraer(0)
                mesa.agregar_al_final(carta_jugador2)
                cartas_guerra.append(carta_jugador2)

            print(f'Carta de Guerra dentro de la Guerra - Jugador 1: {carta_jugador1}')
            print(f'Carta de Guerra dentro de la Guerra - Jugador 2: {carta_jugador2}')

            # Comparar las dos últimas cartas en la mesa para determinar el ganador de la Guerra dentro de la Guerra
            if valores.index(carta_jugador1.valor) > valores.index(carta_jugador2.valor):
                print('¡Jugador 1 gana la Guerra dentro de la Guerra!')
                for carta in cartas_guerra:
                    jugador1.agregar_al_final(carta)  # Todas las cartas de la Guerra al jugador 1
            elif valores.index(carta_jugador2.valor) > valores.index(carta_jugador1.valor):
                print('¡Jugador 2 gana la Guerra dentro de la Guerra!')
                for carta in cartas_guerra:
                    jugador2.agregar_al_final(carta)  # Todas las cartas de la Guerra al jugador 2
            else:
                print('Empate en la Guerra dentro de la Guerra. Se inicia otra Guerra dentro de la Guerra.')
                guerra()  # Llamada recursiva para una nueva Guerra dentro de la Guerra


        while not jugador1.esta_vacia() and not jugador2.esta_vacia() and turnos < 10000:
            turnos += 1 
            print(f'Turno {turnos}:')

            carta_jugador_1 = jugador1.extraer(0)
            carta_jugador_2 = jugador2.extraer(0)

            mesa.agregar_al_final(carta_jugador_1)
            mesa.agregar_al_final(carta_jugador_2)

            print(f'Jugador 1: {carta_jugador_1}')
            print(f'Jugador 2: {carta_jugador_2}')

            if valores.index(carta_jugador_1.valor) > valores.index(carta_jugador_2.valor):
                print('¡Jugador 1 gana la ronda!')
                jugador1.agregar_al_final(carta_jugador_1)
                jugador1.agregar_al_final(carta_jugador_2)
            elif valores.index(carta_jugador_2.valor) > valores.index(carta_jugador_1.valor):
                print('¡Jugador 2 gana la ronda!')
                jugador2.agregar_al_final(carta_jugador_1)
                jugador2.agregar_al_final(carta_jugador_2)
            else:
                print('¡Guerra!')
                guerra()  # Llamada a la función de Guerra para manejar el empate



