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