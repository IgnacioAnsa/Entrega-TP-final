from funciones.logica_juego import *

while True:
    
    print("\n--- Menú Principal ---")
    print("1 - Jugar Truco")
    print("2 - Salir")
    opcion = input("Elige una opción: ")

    match opcion:

        case "1":
            jugar_truco() 
        case "2":
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        case _:
            print("Opción inválida. Intenta nuevamente.")

