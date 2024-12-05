import csv

# Archivo para guardar puntajes históricos
archivo_puntajes = "./archivo/registro.csv"

def registrar_puntaje(nombre: str, puntos: int) -> None:
    # Leer el historial de puntajes (sin sobrescribir)
    historico = leer_puntajes()
    
    # Si el jugador ya existe, se actualiza solo si el nuevo puntaje es mayor
    if nombre in historico:
        if puntos > historico[nombre]:
            historico[nombre] = puntos
    else:
        historico[nombre] = puntos

    # Guardar los puntajes actualizados
    guardar_puntajes(historico)

def leer_puntajes() -> dict:
    try:
        with open(archivo_puntajes, mode="r", newline="") as archivo:
            lector = csv.reader(archivo)
            # Leer el archivo y crear un diccionario, ignorando la cabecera
            return {fila[0]: int(fila[1]) for i, fila in enumerate(lector) if i > 0 and fila}
    except FileNotFoundError:
        return {}

def guardar_puntajes(historico: dict) -> None:
    # Leer el archivo para verificar si es necesario agregar la cabecera
    try:
        with open(archivo_puntajes, mode="r", newline="") as archivo:
            lector = csv.reader(archivo)
            datos_existentes = list(lector)
    except FileNotFoundError:
        datos_existentes = []

    # Escribir los puntajes actualizados en el archivo
    with open(archivo_puntajes, mode="w", newline="") as archivo:
        escritor = csv.writer(archivo)

        # Si el archivo está vacío (o no tiene cabecera), escribir la cabecera
        if not datos_existentes:
            escritor.writerow(["Jugador", "Puntos"])

        # Ordenar los jugadores por los puntos de mayor a menor
        ranking = sorted(historico.items(), key=lambda x: x[1], reverse=True)

        # Escribir el ranking de jugadores en el archivo
        for nombre, puntos in ranking:
            escritor.writerow([nombre, puntos])



