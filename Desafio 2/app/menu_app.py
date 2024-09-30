from UTN_Heroes_Dataset.utn_funciones import *

from funciones import (
    mostrar_menu, utn_mostrar_cantidad_heroes_femeninos,
    cant_heroes_masculinos, heroes_mayores_a_160m
    
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
                pass
            case 4:
                heroes_mayores_a_160m()
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10: 
                pass
            case 11:
                pass
            case 12:
                pass
            case 13: # Salir del programa
                break
            
        clear_console()