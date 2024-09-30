import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("Bienvenido al Espacio!, ingresá tu nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Mamut", 70, 15),
    ]

    enemigos_derrotados = []


    print("Comienza la aventura")

#   Este while hace que siempre se juege hasta que se decide no jugar más 

#   while True:   # lo reemplazamos

    while enemigos:     # mientras haya enemigos

        enemigo_actual = random.choice(enemigos)    # "Choice" elige al azar uno de la lista enemigos
        
        if enemigo_actual in enemigos_derrotados:   # si ya luchamos contra ese enemigo vuelve a
            continue                                # elegir otro

        print(f"Te enfrentas contra {enemigo_actual.nombre}")
        while enemigo_actual.salud > 0:             # mientras el enemigo tenga salud positiva
            accion = input("Qué vas a hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                danio_jugador = jugador.atacar()
                print(f"Atacaste a {enemigo_actual.nombre} y le causaste {danio_jugador} de daño")
                enemigo_actual.recibir_danio(danio_jugador)

                if enemigo_actual.salud > 0:
                    danio_enemigo = enemigo_actual.atacar()
                    print(f"{enemigo_actual.nombre} te atacó y te hizo {danio_enemigo} de daño")
                    jugador.recibir_danio(danio_enemigo)
            elif accion == "huir":
                print("decidiste huir del combate")
                break                               # break para salir de while y cambiar de enemigo

        if jugador.salud <= 0:
            print("Perdiste la batalla!")
            break                                   # cortás la batalla porque no tenés más salud

        if enemigo_actual.salud <= 0:                   # si el enemigo es derrotado
            enemigos_derrotados.append(enemigo_actual)  # se suma a la lista de enemigos derrotados
            enemigos.remove(enemigo_actual)             # y se saca de la lista de enemigos
                                                        # y así no se vuelve a luchar contra ese

        jugador.ganar_experiencia(20)

        continuar = input("Querés seguir jugando (s/n): ").lower()

        if continuar != "s":
            print("Gracias por jugar Batalla Campal!!!")
            break                                   # Corta el primer while, no quiere seguir jugando
    
    if not enemigos:
        print("Felicitaciones, derrotaste a todos!!!")


if __name__ == "__main__":            # Esto nos asegura que sólo podemos ejecutar este script
    main()                            # desde el programa principal
                                      # y evitar que se ejecute desde otro lado siendo llamado como
                                      # un modulo de otro "main".

