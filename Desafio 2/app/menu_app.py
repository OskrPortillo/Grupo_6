from UTN_Heroes_Dataset.utn_funciones import *

from funciones import (
    mostrar_menu, 
    utn_mostrar_cantidad_heroes_femeninos,
    utn_mostrar_heroes_poder_mayor_a_75,
    utn_filtrar_heroes_femeninos_poder_mayor_a_60,
    utn_filtrar_no_binarios_poder_10_a_50,
    utn_mostrar_heroes_maxima_altura,
    utn_ordenar_apodo_descendente,
    cant_heroes_masculinos, heroes_mayores_a_160m,
    masc_poder_menor_60, minimo_poder,
    cant_debiles, nombres_alfabeticos,
    ordenar_por_altura, mostar_matriz_como_planilla
    
    )

from validaciones import validar_opcion


def utn_heroes_app(matriz_heroes):
    
    while True:

        mostrar_menu()
        opcion = validar_opcion(1,13)
        play_sound()

        match opcion:
            case 1:
                utn_mostrar_cantidad_heroes_femeninos(matriz_heroes)
            case 2:
                cant_heroes_masculinos()
            case 3:
                utn_mostrar_heroes_poder_mayor_a_75(matriz_heroes)
            case 4:
                heroes_mayores_a_160m()
            case 5:
                utn_filtrar_heroes_femeninos_poder_mayor_a_60(matriz_heroes)
            case 6:
                masc_poder_menor_60()
            case 7:
                utn_filtrar_no_binarios_poder_10_a_50(matriz_heroes)
            case 8:
                cant_debiles()
            case 9:
                utn_mostrar_heroes_maxima_altura(matriz_heroes)
            case 10: 
                nombres_alfabeticos()
                mostar_matriz_como_planilla()
            case 11:
                utn_ordenar_apodo_descendente(matriz_heroes)
            case 12:
                ordenar_por_altura()
                mostar_matriz_como_planilla()
            case 13: # Salir del programa
                break
            
        clear_console()