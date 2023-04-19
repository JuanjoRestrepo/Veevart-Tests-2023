import random
import time


ladders = {3: 11, 6: 17, 9: 18, 10: 12 }
snakes = {14: 4, 19: 8, 22: 20, 24: 16}

def tirarDado():
    time.sleep(1)
    dado = random.randint(1,6)
    return dado
    
def moverJugador(current_pos, dado, num_turno):
    
    #Actualiza la posición del jugador en función del número de pasos dados.
    #Si la posición resultante está en una escalera o serpiente, se mueve a la nueva posición.
    new_pos = current_pos + dado
    print(f"\n{num_turno}. Dado arroja: {dado}")
    time.sleep(1)
    print(f"Jugador avanza a cuadro: {new_pos}")
    if new_pos in ladders:
        print(f"¡Subiste por una escalera! De la posicion {current_pos} a {ladders[new_pos]}")
        new_pos = ladders[new_pos]
    elif new_pos in snakes:
        print(f"¡Caiste en una serpiente! De {current_pos} a {snakes[new_pos]}")
        new_pos = snakes[new_pos]
       
    return new_pos

def jugar():
    # Posición inicial del jugador
    pos_jugador = 0
    # Cantidad de turnos que lleva el juego
    num_turno = 0

    # Bucle principal del juego
    while pos_jugador < 25:
        # Lanzar el dado
        dado = tirarDado()
        pos_jugador = moverJugador(pos_jugador, dado, num_turno)

        # Incrementar el contador de turnos
        num_turno += 1
        time.sleep(0.5)

        if pos_jugador >= 25:
             print(f"  \nJugador ha superado o caido en el cuadro 25")
             print("   ¡El jugador ha ganado!")
        
    print("\nFin del juego")


# comenzar el juego
jugar()

