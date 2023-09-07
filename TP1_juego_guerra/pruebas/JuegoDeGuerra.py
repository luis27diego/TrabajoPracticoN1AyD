from TP1_LDE_testing.ListaDobleEnLazada import ListaDobleEnlazada
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
        
class Mazo:
    def __init__(self):
        self.mazo = []
        self.jugador_1 = ListaDobleEnlazada()
        self.jugador_2 = ListaDobleEnlazada()

        for valor in valores:
            for palo in palos:
                self.mazo.append(Carta(valor,palo))
    
        random.shuffle(self.mazo)
        
        def pasador(self):
            lista = ListaDobleEnlazada()
            for carta in self.mazo:
                lista.agregar_al_final(carta)
            self.mazo = lista

        pasador(self)
        
        def repartir(self):
            for _ in range(26):
                carta1 = self.mazo.extraer(0)
                carta2 = self.mazo.extraer(0)
                self.jugador_1.agregar_al_inicio(carta1)
                self.jugador_2.agregar_al_inicio(carta2)

        repartir(self)
        

    
    def poner_arriba(self,Carta):
        self.mazo.agregar_al_inicio(Carta)


    def poner_abajo(self, carta):
        self.mazo.agregar_al_final(carta)


    def sacar_arriba(self):
        if self.mazo:
            return self.mazo.extraer(0)
        else:
            return None

        

        



class JuegoGuerra:
    def __init__(self, semilla=None):
        self.turnos = 0
        self.max_turnos = 10000
        self.mazo = Mazo()  # Crear una instancia de Mazo para obtener las listas de jugadores
        self.mazo_jugador1 = self.mazo.jugador_1
        self.mazo_jugador2 = self.mazo.jugador_2
        self.mesa = ListaDobleEnlazada()
        random.seed(semilla)


    def jugar_turno(self):
        if self.turnos >= self.max_turnos:
            print("La partida ha terminado en empate.")
            return
        if self.mazo_jugador1.esta_vacia(): 
            print("jugador 2 ganaa")
            return
        if self.mazo_jugador2.esta_vacia(): 
            print("jugador 1 ganaa")
            return

        carta_jugador1 = self.mazo_jugador1.extraer(0)
        carta_jugador2 = self.mazo_jugador2.extraer(0)

        carta_jugador1.boca_abajo = False
        carta_jugador2.boca_abajo = False



        print(f'Turno {self.turnos + 1}:')
        print(f'jugador1: {" ".join(str(carta) if not carta.boca_abajo else "-X" for carta in self.mazo_jugador1)}')
        print(f'jugador2: {" ".join(str(carta) if not carta.boca_abajo else "-X" for carta in self.mazo_jugador2)}')
        print(f'Carta jugador1: {carta_jugador1}')
        print(f'Carta jugador2: {carta_jugador2}') 


        carta_jugador1.boca_abajo = True
        carta_jugador2.boca_abajo = True


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

        for carta in self.mesa:
            carta.boca_abajo = True

        self.turnos += 1    

    def guerra(self):
        if self.turnos >= self.max_turnos:
            print("La partida ha terminado en empate.")
            return

        #guerra_mesa = ListaDobleEnlazada()

        for _ in range(3):
            if self.mazo_jugador1.esta_vacia(): 
                print("jugador 2 gana")
                return
            if self.mazo_jugador2.esta_vacia(): 
                print("jugador 1 gana")
                return 
            carta_jugador1 = self.mazo_jugador1.extraer(0)
            carta_jugador2 = self.mazo_jugador2.extraer(0)





            self.mesa.agregar_al_final(carta_jugador1)
            self.mesa.agregar_al_final(carta_jugador2)

        print('Cartas en la mesa durante la guerra:')
        for carta in self.mesa:
            print(f'{carta}', end=' ')
        print()
    
        if self.mazo_jugador1.esta_vacia(): 
            print("jugador 2 gana")
            return
        if self.mazo_jugador2.esta_vacia(): 
            print("jugador 1 gana")
            return    



        carta_jugador1 = self.mazo_jugador1.extraer(0)
        carta_jugador2 = self.mazo_jugador2.extraer(0)

        carta_jugador1.boca_abajo = False
        carta_jugador2.boca_abajo = False


        print(f'Quinta carta de Jugador 1: {carta_jugador1}')
        print(f'Quinta carta de Jugador 2: {carta_jugador2}')

        carta_jugador1.boca_abajo = True
        carta_jugador2.boca_abajo = True

        self.mesa.agregar_al_final(carta_jugador1)
        self.mesa.agregar_al_final(carta_jugador2)


        if valores.index(carta_jugador1.valor) > valores.index(carta_jugador2.valor):
            print('Jugador 1 gana la guerra.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador1.agregar_al_final(self.mesa.extraer())
        elif valores.index(carta_jugador1.valor) < valores.index(carta_jugador2.valor):
            print('Jugador 2 gana la guerra.')
            while not self.mesa.esta_vacia():
                self.mazo_jugador2.agregar_al_final(self.mesa.extraer())
        else:
            print('¡Guerra de nuevo!')
            if self.mazo_jugador1.esta_vacia or self.mazo_jugador2.esta_vacia:
                return
            else:
                self.guerra()

        self.turnos += 1

    def jugar(self):
        while self.turnos < self.max_turnos :
            if self.mazo_jugador1.esta_vacia() or self.mazo_jugador2.esta_vacia():
                return
            self.jugar_turno()

        if self.mazo_jugador1.esta_vacia():
            print("¡Jugador 2 gana la partida!")
        elif self.mazo_jugador2.esta_vacia():
            print("¡Jugador 1 gana la partida!")
        else:
            print("La partida ha terminado en empate.")

juego = JuegoGuerra(semilla=80)
juego.jugar()
