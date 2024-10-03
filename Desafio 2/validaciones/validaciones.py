def validar_opcion(num_min: int, num_max: int) -> int:
    """
    Funcion que solicita al usuario que ingrese una opción dentro de un rango determinado 
    y valida que la entrada sea un número válido dentro de ese rango.
    Args:
        num_min (int): El valor mínimo para la opción.
        num_max (int): El valor máximo para la opción.

    Returns:
        int: El número entero que el usuario ha ingresado, validado para estar 
        dentro del rango especificado [num_min, num_max]
    """
    opcion = input(f'Ingrese una opcion [{num_min} - {num_max}]:')
    
    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
        return validar_opcion(num_min, num_max)
    
    return int(opcion)