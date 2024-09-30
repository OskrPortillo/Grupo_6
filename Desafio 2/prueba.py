from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def info_heroe(indice):
    indice = int(indice)
    info = ""
    for i in matriz_data_heroes:
        info += (f"{i[indice]:10}|")
    print (info)

info_heroe(1)