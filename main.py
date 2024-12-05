from funciones.logica_juego import *
from funciones.complementarias import *

while True:
    
    print("\n--- Menú Principal ---")
    print("1 - Jugar Truco")
    print("2 - Salir")
    print("3 - mostrar ranking historico")

    opcion = input("Elige una opción: ")

    match opcion:

        case "1":
            jugar_truco() 
        case "2":
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        case "3":
            print("mostrar ranking historico")
            print(leer_puntajes())
        case _:
            print("Opción inválida. Intenta nuevamente.")
