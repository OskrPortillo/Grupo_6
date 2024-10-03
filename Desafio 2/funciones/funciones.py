from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def info_heroe(indice: int):
    info = ""
    for lista in matriz_data_heroes:
        dato = str(lista[indice])
        info += (f"{dato[:25]:<25}|")
    print (info)

def mostar_matriz_como_planilla():
    for indice in range(len(matriz_data_heroes[0])):
        info_heroe(indice)
        
def selection_sort(matriz_heroes, orden_ascendente = True) -> None:
    """
    Función que recibe una matriz y la ordenada de forma ascendente

    Args:
        matriz_heroes (_type_): lista[lista]
        orden_ascendente (bool, optional): booleano que determina 
        si el ordenamiento es ascendente o descendente.
    """
    #Uso la fila de apodos para comparar y ordenar.
    fila_comparacion = 2
    columnas = len(matriz_heroes[2])        
    
    for indice in range(columnas - 1):
        indice_extremo = indice

        for sub_indice in range(indice + 1, columnas):

            if orden_ascendente:
                if matriz_heroes[fila_comparacion][sub_indice] < matriz_heroes[fila_comparacion][indice_extremo]:
                    indice_extremo = sub_indice
            else:
                if matriz_heroes[fila_comparacion][sub_indice] > matriz_heroes[fila_comparacion][indice_extremo]:
                    indice_extremo = sub_indice
        
        # Intercambiar todas las filas para mantener la relación entre columnas
        if indice_extremo != indice:
            for fila in matriz_heroes:
                fila[indice], fila [indice_extremo] = fila[indice_extremo], fila[indice]

      

def utn_ordenar_apodo_descendente(matriz_heroes)->None:
    """
    Función que ordena la matriz de héroes por apodo en orden descendente 
    y muestra la información de cada héroe.

    Args:
        matriz_heroes (_type_): lista[lista]
    """
    
    selection_sort(matriz_heroes, orden_ascendente = False)
    
    for indice in range(len(matriz_heroes[0])):
        info_heroe(indice)


def buscar_maxima_altura(matriz_heroes) -> float:
    """
    Función que busca y retorna la altura máxima entre los héroes

    Args:
        matriz_heroes (_type_): lista[lista]

    Returns:
        float: Retorna la altura maxima encontrada entre los heroes.
    """

    maxima_altura = None
    cantidad_columnas = len(matriz_heroes[5])

    for columna in range(cantidad_columnas):
        if not maxima_altura or matriz_heroes[5][columna] > maxima_altura:
            maxima_altura = matriz_heroes[5][columna]

    return float(maxima_altura)

def utn_mostrar_heroes_maxima_altura(matriz_heroes)->None:
    """
    Función que muestra los héroes con la altura máxima.

    Args:
        matriz_heroes (_type_): lista[lista]
    """

    max_altura = buscar_maxima_altura(matriz_heroes)
    
    #fila de altura
    cantidad_columnas = len(matriz_heroes[5]) 

    for columna in range(cantidad_columnas):
        if matriz_heroes[5][columna] == max_altura:
            info_heroe(columna)



def utn_filtrar_no_binarios_poder_10_a_50(matriz_heroes)->None:
    """
    Función que muestra los héroes no-binarios cuyo poder este comprendido
    entre 10 y 50 inclusive.

    Args:
        matriz_heroes (_type_): lista[lista]
    """
    #Fila de genero
    cantidad_columnas = len(matriz_heroes[3])

    for columna in range (cantidad_columnas):
        if matriz_heroes[3][columna] == "No-Binario" and  10 <= matriz_heroes[4][columna] <= 50:
            info_heroe(columna)


def utn_filtrar_heroes_femeninos_poder_mayor_a_60(matriz_heroes)->None:
    """
    Función que muestra los héroes femeninos cuyo poder sea mayor a 60.

    Args:
        matriz_heroes (_type_): lista[lista]
    """
    #Fila de genero
    cantidad_columnas = len(matriz_heroes[3])

    for columna in range (cantidad_columnas):
        if matriz_heroes[3][columna] == "Femenino" and matriz_heroes[4][columna] > 60:
            info_heroe(columna)
            

def utn_mostrar_heroes_poder_mayor_a_75(matriz_heroes)-> None:
    """
    Función que muestra los héroes cuyo poder sea mayor a 75.

    Args:
        matriz_heroes (_type_): lista[lista]
    """
    #Fila de poder
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

def cant_heroes_masculinos() -> str:
    #Funcion que calcula la cantidad de heroes masculinos en la matriz
    contador = 0
    for genero in matriz_data_heroes[3]:
        #Recorro la sub-lista de generos
        if genero == "Masculino":
            #En cada iteracion verifico el genero, y si es masculino incremento en 1 el contador de masculinos
            contador += 1
    print(f"La cantidad de heroes masculinos es: {contador}")

def heroes_mayores_a_160m() -> str:
    #Funcion que muestra los datos asociados de los heroes ccon una altura mayor a 160m
    for i in range (len (matriz_data_heroes[-1])):
        if matriz_data_heroes[-1][i] > 160:
            #Si la altura en el indice de la iteracion es mayor a 160 lo paso como parametro a la funcion que muestra los datos de un heroe especifico
            info_heroe(i)

def masc_poder_menor_60() -> str:
    #Funcion que filtra y muestra los heroes con poder menor a 60
    for i in range (len(matriz_data_heroes[0])):
        if matriz_data_heroes[3][i] == "Masculino" and int(matriz_data_heroes[-2][i]) < 60:
            info_heroe(i)
        
def minimo_poder() -> int:
    #Funcion que retorna el poder mas bajo
    mas_debil = None
    for i in matriz_data_heroes[-2]:
        if mas_debil == None or (i <= mas_debil):
            mas_debil = i
    return mas_debil

def cant_debiles() -> int:
    #Funcion que retorna la cantidad de heroes cuyo poder es igual al minimo
    contador = 0
    for i in matriz_data_heroes[-2]:
        if i == minimo_poder():
            #Comparo el contenido del indice actual en la lista de poderes con el valor retornado de la funcion creada anteriormente
            contador += 1
    print(f"{contador} heroe/s con el minimo poder de {minimo_poder()}")

def nombres_alfabeticos() -> None:
    # Funcion que ordena alfabeticamente los nombres de la lista de nombres
    for i in range(len(matriz_data_heroes[0]) - 1):
        # Recorro el resto de los elementos para comparar cuales cumplen el criterio
        # de ordenamiento 
        for j in range(i + 1, len(matriz_data_heroes[0])):
            # Si los elementos no estan ordenados, los intercambio
            if matriz_data_heroes[0][i] > matriz_data_heroes[0][j]:
                #(lista[i], lista[j]) = (lista[j], lista[i])
                aux = matriz_data_heroes[0][i]
                matriz_data_heroes[0][i] = matriz_data_heroes[0][j]
                matriz_data_heroes[0][j] = aux

def ordenar_por_altura() ->None:
    #Funcion que ordena la lista de alturas segun el valor que ingrese el usuario
    orden = int(input("Ingrese modo de ordenamiento:\n1-Ascendente\n2-Descendente\nOPCION: "))
    #Se solicita al usuario ingresar el numero asociado al tipo de ordenamiento los cuales son mostrados en un mensaje
    if orden == 1:
        for i in range(len(matriz_data_heroes[-1]) - 1):
            for j in range(i + 1, len(matriz_data_heroes[-1])):
                if matriz_data_heroes[-1][i] > matriz_data_heroes[-1][j]:
                    aux = matriz_data_heroes[-1][i]
                    matriz_data_heroes[-1][i] = matriz_data_heroes[-1][j]
                    matriz_data_heroes[-1][j] = aux
    elif orden == 2:
        for i in range(len(matriz_data_heroes[-1]) - 1):
            for j in range(i + 1, len(matriz_data_heroes[-1])):
                if matriz_data_heroes[-1][i] < matriz_data_heroes[-1][j]:
                    aux = matriz_data_heroes[-1][i]
                    matriz_data_heroes[-1][i] = matriz_data_heroes[-1][j]
                    matriz_data_heroes[-1][j] = aux

if __name__ == '__main__':
    #print((matriz_data_heroes[-1][-1]))
    #print(cant_debiles())
    #ordenar_por_altura()
    print("b">"a")
    #info_heroe(-1)