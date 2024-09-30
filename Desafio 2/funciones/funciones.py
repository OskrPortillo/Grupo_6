from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def info_heroe(indice: int):
    indice = int(indice)
    info = ""
    for lista in matriz_data_heroes:
        info += (f"{lista[indice]:10}|")
    print (info)