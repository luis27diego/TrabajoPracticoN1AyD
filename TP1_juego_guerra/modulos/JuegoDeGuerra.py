from TP1_juego_guerra.modulos.Mazo import Mazo    # Importa la clase Mazo desde el archivo mazo.py
from TP1_ListaDobleEnlazada.modulos.ListaDobleEnlazada import ListaDobleEnlazada

valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['♠', '♥', '♦', '♣']

# Clase que representa el juego de la Guerra.
class JuegoGuerra:
    def __init__(self, semilla=None):
        self.turnos = 0
        self.max_turnos = 10000
        self.mazo = Mazo(semilla)  # Crear una instancia de Mazo para crear el mazo y repartir las cartas a los jugadores
        self.mazo_jugador1 = self.mazo.jugador_1
        self.mazo_jugador2 = self.mazo.jugador_2
        self.mesa = ListaDobleEnlazada()   # Se crea la mesa

    # Método para jugar un turno del juego.
    def jugar_turno(self):
        
        # Si la cantidad de turnos jugadores supera el limite en este caso 10000 termina en empate
        if self.turnos >= self.max_turnos:
            print("La partida ha terminado en empate.")
            return
        
        # Si el jugador 1 se queda sin cartas el jugador 2 gana
        if self.mazo_jugador1.esta_vacia(): 
            print("jugador 2 ganaa")
            return
        
        # Si el jugador 2 se queda sin cartas el jugador 1 gana
        if self.mazo_jugador2.esta_vacia(): 
            print("jugador 1 ganaa")
            return
        
        # Extraemos las cartas de la parte superior de los mazos de los jugadores
        carta_jugador1 = self.mazo_jugador1.extraer(0)
        carta_jugador2 = self.mazo_jugador2.extraer(0)

        # Revelamos las cartas, estableciendo 'boca_abajo' en False
        carta_jugador1.boca_abajo = False
        carta_jugador2.boca_abajo = False


        # Mostramos información sobre el turno actual
        print(f'Turno {self.turnos + 1}:')
        print(f'jugador1: {" ".join(str(carta) if not carta.boca_abajo else "-X" for carta in self.mazo_jugador1)}')
        print(f'jugador2: {" ".join(str(carta) if not carta.boca_abajo else "-X" for carta in self.mazo_jugador2)}')
        print(f'Carta jugador1: {carta_jugador1}')
        print(f'Carta jugador2: {carta_jugador2}') 

        # Volvemos a ocultar las cartas
        carta_jugador1.boca_abajo = True
        carta_jugador2.boca_abajo = True

        # Agregamos las cartas a la mesa
        self.mesa.agregar_al_final(carta_jugador1)
        self.mesa.agregar_al_final(carta_jugador2)

        if valores.index(carta_jugador1.valor) > valores.index(carta_jugador2.valor):
            # Jugador 1 gana el turno
            print('Jugador 1 gana el turno.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador1.agregar_al_final(self.mesa.extraer(0))

        elif valores.index(carta_jugador1.valor) < valores.index(carta_jugador2.valor):
            # Jugador 2 gana el turno
            print('Jugador 2 gana el turno.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador2.agregar_al_final(self.mesa.extraer(0))
        else:
            # Empieza una guerra si las cartas tienen el mismo valor
            print('¡Guerra!')
            self.guerra()

        # Ocultamos todas las cartas en la mesa nuevamente
        for carta in self.mesa:
            carta.boca_abajo = True

        self.turnos += 1    

    # Método para la guerra durante el juego.
    def guerra(self):

        # Si la cantidad de turnos jugadores supera el limite en este caso 10000 termina en empate
        if self.turnos >= self.max_turnos:
            print("La partida ha terminado en empate.")
            return

        # For para extraer 3 cartas de cada jugador y agregarlas a la mesa
        for _ in range(3):
            if self.mazo_jugador1.esta_vacia(): 
                # Si el jugador 1 se queda sin mazo, el jugador 2 gana la guerra

                print("jugador 2 gana")
                return
            
            if self.mazo_jugador2.esta_vacia(): 
                # Si el jugador 2 se queda sin mazo, el jugador 1 gana la guerra
                print("jugador 1 gana")
                return 
            
            # Extraemos las cartas de la parte superior de los mazos de los jugadores
            carta_jugador1 = self.mazo_jugador1.extraer(0)
            carta_jugador2 = self.mazo_jugador2.extraer(0)

            # Agregamos las cartas a la mesa
            self.mesa.agregar_al_final(carta_jugador1)
            self.mesa.agregar_al_final(carta_jugador2)

        # Mostramos las cartas en la mesa durante la guerra
        print('Cartas en la mesa durante la guerra:')
        for carta in self.mesa:
            print(f'{carta}', end=' ')
        print()
    
        if self.mazo_jugador1.esta_vacia(): 
            # Si el jugador 1 se queda sin cartas durante la guerra, el jugador 2 gana la guerra
            print("jugador 2 gana")
            return
        
        if self.mazo_jugador2.esta_vacia(): 
            # Si el jugador 2 se queda sin cartas durante la guerra, el jugador 1 gana la guerra
            print("jugador 1 gana")
            return    
        
        # Extraemos una carta adicional de cada jugador para luego comparar
        carta_jugador1 = self.mazo_jugador1.extraer(0)
        carta_jugador2 = self.mazo_jugador2.extraer(0)

        # Revelamos las cartas 
        carta_jugador1.boca_abajo = False
        carta_jugador2.boca_abajo = False

        # Mostramos las cartas de los jugadores
        print(f'Quinta carta de Jugador 1: {carta_jugador1}')
        print(f'Quinta carta de Jugador 2: {carta_jugador2}')

        # Volvemos a ocultar las cartas adicionales
        carta_jugador1.boca_abajo = True
        carta_jugador2.boca_abajo = True

        # Agregamos las cartas adicionales a la mesa
        self.mesa.agregar_al_final(carta_jugador1)
        self.mesa.agregar_al_final(carta_jugador2)

        if valores.index(carta_jugador1.valor) > valores.index(carta_jugador2.valor):
            # Jugador 1 gana la guerra
            print('Jugador 1 gana la guerra.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador1.agregar_al_final(self.mesa.extraer())

        elif valores.index(carta_jugador1.valor) < valores.index(carta_jugador2.valor):
            # Jugador 2 gana la guerra
            print('Jugador 2 gana la guerra.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador2.agregar_al_final(self.mesa.extraer())

        else:
            # Se produce otra guerra si las cartas tienen el mismo valor
            print('¡Guerra de nuevo!')
            if self.mazo_jugador1.esta_vacia or self.mazo_jugador2.esta_vacia:
                return
            else:
                self.guerra()

        self.turnos += 1

    # Método para jugar una partida.
    def jugar(self):

        # Mientras la cantidad de turnos no supere a la cantidad no supere a la cantidad de maxima de turnos se sigue jugando
        while self.turnos < self.max_turnos :

            # Si un jugador se queda sin mazo return 
            if self.mazo_jugador1.esta_vacia() or self.mazo_jugador2.esta_vacia():
                return
            self.jugar_turno()

        # Comprobar el resultado de la partida al final.
        if self.mazo_jugador1.esta_vacia():
            print("¡Jugador 2 gana la partida!")
        elif self.mazo_jugador2.esta_vacia():
            print("¡Jugador 1 gana la partida!")
        else:
            print("La partida ha terminado en empate.")