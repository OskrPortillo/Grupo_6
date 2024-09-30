from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def info_heroe(indice: int):
    info = ""
    for lista in matriz_data_heroes:
        dato = str(lista[indice])
        info += (f"{dato[:25]:<25}|")
    print (info)


def utn_mostrar_heroes_poder_mayor_a_75(matriz_heroes)-> None:
    
    cantidad_columnas = len(matriz_heroes[4])
    for columna in range(cantidad_columnas):
        if matriz_heroes[4][columna] > 75:
            info_heroe(columna)

def utn_mostrar_cantidad_heroes_femeninos(matriz_heroes) -> None:
    """
    Función que cuenta la cantidad de héroes de género femenino en 
    una matriz dada y muestra el resultado.
    Args:
        matriz_heroes (_type_): list[list]
    """
   
    cantidad_columnas = len(matriz_heroes[3])
    cantidad_femenino = 0

    for columna in range (cantidad_columnas):
        if matriz_heroes[3][columna] == "Femenino":
            cantidad_femenino += 1
    
    print(f"La cantidad de heroes femeninos es {cantidad_femenino}")


def cant_heroes_masculinos():
    contador = 0
    for i in matriz_data_heroes[3]:
        if i == "Masculino":
            contador += 1
    print(contador)

#info_heroe(0)


def heroes_mayores_a_160m():
    contador = 0
    for i in range (len (matriz_data_heroes[-1])):
        if matriz_data_heroes[-1][i] > 160:
            contador += 1
            info_heroe(i)
    print(contador)



if __name__ == '__main__':
    # Aca pone las funciones para ver si funcionan, solo sirven aca.
    # Despues yo las linkeo para que anden con el menu.
    cant_heroes_masculinos()
    heroes_mayores_a_160m()