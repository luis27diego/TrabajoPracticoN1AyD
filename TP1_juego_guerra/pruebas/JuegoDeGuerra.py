from TP1_LDE_testing.ListaDobleEnLazada import ListaDobleEnlazada
import random

valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['♠', '♥', '♦', '♣']

# Clase que representa una carta en el juego de la Guerra, se crean los atributos de la carta 
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        self.boca_abajo = True
        
    # Método especial para convertir la carta en una cadena legible.
    def __str__(self):
        
        if self.boca_abajo:
            return 'X'  # Si la carta está boca abajo, se representa con 'X'.
        
        else:
            return f'{self.valor}{self.palo}' # Si no, se muestra el valor y el palo de la carta.
        
# Clase que representa un mazo de cartas y las distribuye a dos jugadores.       
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

juego = JuegoGuerra(178)
juego.jugar()
