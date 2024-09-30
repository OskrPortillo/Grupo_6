from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def info_heroe(indice: int):
    indice = int(indice)
    info = ""
    for lista in matriz_data_heroes:
        info += (f"{lista[indice]:10}|")
    print (info)


def utn_mostrar_cantidad_heroes_femeninos(matriz_heroes) -> None:
    
    cantidad_filas = len(matriz_heroes)
    cantidad_columnas = len(matriz_heroes[0])
    cantidad_femenino = 0

    for fila in range(cantidad_filas):

        for columna in range (cantidad_columnas):
            if matriz_heroes[fila][columna] == "Femenino":
                cantidad_femenino += 1
    
    print(f"La cantidad de heroes femeninos es {cantidad_femenino}")
