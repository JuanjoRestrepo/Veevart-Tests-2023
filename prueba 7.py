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



"""

Este código es una implementación en Python del juego de la serpiente y la escalera.

Primero, se definen los diccionarios ladders y snakes que representan las posiciones de las escaleras y serpientes en el tablero del juego.

La función tirarDado() genera un número aleatorio entre 1 y 6 para simular el lanzamiento del dado.

La función moverJugador() actualiza la posición del jugador en función del número de pasos dados. 
Si la nueva posición está en una escalera o serpiente, se mueve a la nueva posición correspondiente.

La función jugar() inicia el juego con la posición inicial del jugador en 0 y un contador de turnos en 0. 
El bucle principal del juego se ejecuta mientras la posición del jugador sea menor que 25. En cada iteración del bucle, 
se lanza el dado, se actualiza la posición del jugador y se incrementa el contador de turnos. 
Si el jugador llega a la posición 25 o la supera, se imprime un mensaje de que ha ganado el juego. 
Finalmente, se imprime un mensaje de fin del juego.

Para hacer el juego más realista, se han agregado pausas de tiempo en las funciones tirarDado() y moverJugador() utilizando la función time.sleep().
También se han utilizado f-strings para imprimir mensajes en la consola.


"""

