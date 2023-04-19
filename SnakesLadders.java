public class Game {
    
    
    static Map<Integer, Integer> ladders = new Map<Integer, Integer>();
    static Map<Integer, Integer> snakes = new Map<Integer, Integer>();
	
    static {
        ladders.put(3, 11);
        ladders.put(6, 17);
        ladders.put(9, 18);
        ladders.put(10, 12);
        snakes.put(14, 4);
        snakes.put(19, 8);
        snakes.put(22, 20);
        snakes.put(24, 16);
    }
    
    public static Integer tirarDado(){
        Integer numero = Math.round((Math.random() * (6) + 1));  
        Return numero;
    }
    
    public static Integer moverJugador(Integer current_pos, Integer dado, Integer num_turno) {
        Integer new_pos = current_pos + dado;
        System.debug('\n' + num_turno + '. Dado arroja: ' + dado);
        System.debug('Jugador avanza a cuadro: ' + new_pos);

        if (ladders.containsKey(new_pos)) {
            System.debug('Subiste por una escalera! De la posicion ' + current_pos + ' a ' + ladders.get(new_pos));
            new_pos = ladders.get(new_pos);
        } else if (snakes.containsKey(new_pos)) {
            System.debug('Caiste en una serpiente! De ' + current_pos + ' a ' + snakes.get(new_pos));
            new_pos = snakes.get(new_pos);
        }
        return new_pos;
    }
    
    public static void jugar() {
        Integer pos_jugador = 0;
        Integer num_turno = 0;
        while (pos_jugador < 25) {
            Integer dado = tirarDado();
            pos_jugador = moverJugador(pos_jugador, dado, num_turno);
            num_turno++;
            if (pos_jugador >= 25) {
                System.debug('\nJugador ha superado o caido en el cuadro 25');
                System.debug('¡El jugador ha ganado!');
            }
        }
        System.debug('\nFin del juego');
    }
    
    public static void main() {
        jugar();
    }
    
}

/*
Este es un código en en Salesforce Apex en el Developer Console que implementa un juego simple de serpientes y escaleras. 
El objetivo del juego es que el jugador avance por un tablero de 25 cuadros, y gana si alcanza el cuadro 25 antes que sus oponentes.

El juego utiliza dos mapas, ladders y snakes, para representar las escaleras y las serpientes en el tablero. Estos mapas se inicializan en el bloque estático, que se ejecuta una sola vez cuando la clase se carga por primera vez.

La clase Game tiene tres métodos estáticos:

tirarDado() devuelve un número entero aleatorio entre 1 y 6.
moverJugador(Integer current_pos, Integer dado, Integer num_turno) toma la posición actual del jugador, el número que salió en el dado y el número del turno actual, y devuelve la nueva posición del jugador después de moverse. El método también comprueba si el nuevo cuadro tiene una escalera o una serpiente, y si es así, ajusta la posición del jugador en consecuencia.
jugar() es el método principal que ejecuta el juego. El método utiliza un bucle while para mover al jugador a través del tablero hasta que el jugador alcanza el cuadro 25. El método también cuenta el número de turnos que tarda el jugador en llegar al final.
El método main() es el punto de entrada del programa y llama al método jugar().

El código utiliza la función System.debug() para imprimir mensajes de depuración en la consola.
*/