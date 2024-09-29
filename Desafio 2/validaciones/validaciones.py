def validar_opcion(num_min: int, num_max:int):
    numero = int(input("Ingrese un numero: "))
    while numero > num_max or numero < num_min:
        numero = int(input("Error, ingrese un numero valido: "))
    return int(numero)

print(validar_opcion(2, 9))