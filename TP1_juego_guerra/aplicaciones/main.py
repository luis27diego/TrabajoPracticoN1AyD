# Archivo principal (main.py)
from TP1_juego_guerra.modulos.JuegoDeGuerra import JuegoGuerra

def main():
    juego = JuegoGuerra(178)
    juego.jugar()

if __name__ == "__main__":
    main()
