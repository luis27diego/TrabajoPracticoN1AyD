from TP1_LDE_testing.main import ListaDobleEnlazada
import random

valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['♠', '♥', '♦', '♣']

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        self.boca_abajo = True

    def __str__(self):
        if self.boca_abajo:
            return 'X'
        else:
            return f'{self.valor}{self.palo}'

class JuegoGuerra:
    def __init__(self, semilla=None):
        self.turnos = 0
        self.max_turnos = 10000
        self.mazo_jugador1 = self.crear_mazo()
        self.mazo_jugador2 = self.crear_mazo()
        self.mesa = ListaDobleEnlazada()
        random.seed(semilla)

    def crear_mazo(self):
        mazo = [Carta(valor, palo) for valor in valores for palo in palos]
        random.shuffle(mazo)
        lista = ListaDobleEnlazada()
        for carta in mazo:
            lista.agregar_al_final(carta)
        return lista

    def jugar_turno(self):
        if self.turnos >= self.max_turnos:
            print("La partida ha terminado en empate.")
            return

        carta_jugador1 = self.mazo_jugador1.extraer(0)
        carta_jugador2 = self.mazo_jugador2.extraer(0)

        if carta_jugador1 is None:
            print("¡Jugador 2 gana!")
            return
        if carta_jugador2 is None:
            print("¡Jugador 1 gana!")
            return

        print(f'Turno {self.turnos + 1}:')
        print(f'Jugador 1: {carta_jugador1}')
        print(f'Jugador 2: {carta_jugador2}')

        self.mesa.agregar_al_final(carta_jugador1)
        self.mesa.agregar_al_final(carta_jugador2)

        if valores.index(carta_jugador1.valor) > valores.index(carta_jugador2.valor):
            print('Jugador 1 gana el turno.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador1.agregar_al_final(self.mesa.extraer(0))
        elif valores.index(carta_jugador1.valor) < valores.index(carta_jugador2.valor):
            print('Jugador 2 gana el turno.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador2.agregar_al_final(self.mesa.extraer(0))
        else:
            print('¡Guerra!')
            self.guerra()

        self.turnos += 1

    def guerra(self):
        if self.turnos >= self.max_turnos:
            print("La partida ha terminado en empate.")
            return

        guerra_mesa = ListaDobleEnlazada()

        for _ in range(3):
            carta_jugador1 = self.mazo_jugador1.extraer(0)
            carta_jugador2 = self.mazo_jugador2.extraer(0)

            if carta_jugador1 is None or carta_jugador2 is None:
                print("No hay suficientes cartas para continuar. El juego termina.")
                return

            carta_jugador1.boca_abajo = False
            carta_jugador2.boca_abajo = False

            guerra_mesa.agregar_al_final(carta_jugador1)
            guerra_mesa.agregar_al_final(carta_jugador2)

        print('Cartas en la mesa durante la guerra:')
        for carta in guerra_mesa:
            print(f'{carta}', end=' ')
        print()

        carta_jugador1 = self.mazo_jugador1.extraer(0)
        carta_jugador2 = self.mazo_jugador2.extraer(0)

        if carta_jugador1 is None:
            print("¡Jugador 2 gana la guerra!")
            while not guerra_mesa.esta_vacia():
                self.mazo_jugador2.agregar_al_final(guerra_mesa.extraer())
            return
        if carta_jugador2 is None:
            print("¡Jugador 1 gana la guerra!")
            while not guerra_mesa.esta_vacia():
                self.mazo_jugador1.agregar_al_final(guerra_mesa.extraer())
            return

        print(f'Cuarta carta de Jugador 1: {carta_jugador1}')
        print(f'Cuarta carta de Jugador 2: {carta_jugador2}')

        if valores.index(carta_jugador1.valor) > valores.index(carta_jugador2.valor):
            print('Jugador 1 gana la guerra.')
            while not guerra_mesa.esta_vacia():
                self.mazo_jugador1.agregar_al_final(guerra_mesa.extraer())
        elif valores.index(carta_jugador1.valor) < valores.index(carta_jugador2.valor):
            print('Jugador 2 gana la guerra.')
            while not guerra_mesa.esta_vacia():
                self.mazo_jugador2.agregar_al_final(guerra_mesa.extraer())
        else:
            print('¡Guerra de nuevo!')
            if self.mazo_jugador1.esta_vacia or self.mazo_jugador2.esta_vacia:
                return
            else:
                self.guerra()

        self.turnos += 1

    def jugar(self):
        while self.turnos < self.max_turnos:
            self.jugar_turno()

        if self.mazo_jugador1.esta_vacia():
            print("¡Jugador 2 gana la partida!")
        elif self.mazo_jugador2.esta_vacia():
            print("¡Jugador 1 gana la partida!")
        else:
            print("La partida ha terminado en empate.")

juego = JuegoGuerra(semilla=802)
juego.jugar()
