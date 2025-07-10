import requests #para hacer solicitudes HTTP a la api


def obtener_datos_pokemon(nombre):

    nombre = nombre.lower()
    url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{nombre}' #llamamos con la direccion de api oficial de pokeapi, al nombre que vamos a ingresar en la funcion
    url_species = f'https://pokeapi.co/api/v2/pokemon-species/{nombre}' #llamamos con el mismo nombre, la especie, segun el pokeapi aqui se encuentra el capture rate
    r_pokemon = requests.get(url_pokemon) #solicitudes HTTP para obtener los datos
    r_species = requests.get(url_species) #solicitudes http para obtener datos de la especie donde se clasifica el capture rate



    #Se valida que los request de http sean exitosos (codigo 2000)
    if r_pokemon.status_code != 200 or r_species.status_code != 200:
        raise Exception("Pokemon no encontrado") #si no se cumple el if lanzamos el error
    
    #almacenamos el json reibido
    data_pokemon=r_pokemon.json()
    data_species=r_species.json()
    print(data_species.keys())
    
    #para extraer el valor clave para nuestro proyecto el HP, mandamos un for que recorra la lista de stats 

    hp = None

    for stat in data_pokemon['stats']:
        if stat['stat']['name']=="hp":
            hp = stat['base_stat']
            break

    #obtenemos el capture rate del json del api

    capture_rate=data_species['capture_rate']

    if capture_rate is None:
        raise Exception("NO HAY CAPTURE RATE")

    return hp, capture_rate 

if __name__ == "__main__":
    nombre = input("ingrese el nombre del pokemon  ")

    try:
        hp, capture_rate=obtener_datos_pokemon(nombre)
        print(f"pokemon: {nombre.capitalize()}")
        print(f"HP base: {hp}")

        print(f"Capture rate: {capture_rate}")

    except Exception as e: #salimos del try para imprimir el error nque pueda mostrar
        print(str(e))