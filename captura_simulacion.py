import requests #para hacer solicitudes HTTP a la api

import random #libreria para randomizar numeros
import time
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_datos_pokemon(nombre):

    nombre = str(nombre).lower()
    url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{nombre}' #llamamos con la direccion de api oficial de pokeapi, al nombre que vamos a ingresar en la funcion
    url_species = f'https://pokeapi.co/api/v2/pokemon-species/{nombre}' #llamamos con el mismo nombre, la especie, segun el pokeapi aqui se encuentra el capture rate

    #avance 2
    
    r_pokemon = requests.get(url_pokemon) #solicitudes HTTP para obtener los datos
    r_species = requests.get(url_species) #solicitudes http para obtener datos de la especie donde se clasifica el capture rate



    #Se valida que los request de http sean exitosos (codigo 2000)
    if r_pokemon.status_code != 200 or r_species.status_code != 200:
        raise Exception("Pokemon no encontrado") #si no se cumple el if lanzamos el error
    
    #almacenamos el json reibido
    data_pokemon=r_pokemon.json()
    data_species=r_species.json()
    
    #print(data_species.keys())
    
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


    #obtenermos el ID del pokemon para nuestra generacion aleatoria
    id_pokemon = data_pokemon['id']

    nombre = data_pokemon['name']

    #agregamos los dos nuevos valores al return
    return hp, capture_rate,  id_pokemon,  nombre


def generate_pkm(): #Funcion de generacion de pokemon aleatoria
    num_r=random.randint(1,151)
    return obtener_datos_pokemon(num_r)

   
        


def play():

    
    try:
        pasos= int(input("Cuantos pasos deseas avanzar?: "))
        if pasos <=0 :
            print("Pasos invalidos, ingresa nuevamente")
            return
    except ValueError:
        print("Entrada incorrecta. ")
        return
    
    print(f"Entrenador RED avanzara {pasos} pasos...")
    print("Ha aparecido un POKEMON salvaje! ")
    time.sleep(1.5)

    
    hp, capture_rate, id_pokemon, nombre =generate_pkm()
    print(f"#Pokedex: {id_pokemon}")
        
    print(f"pokemon: {nombre.capitalize()}")
    print(f"HP base: {hp}")

    print(f"Capture rate: {capture_rate}")
    time.sleep(2.5)
    limpiar_consola()
def menu():
    while True:
        print("Simulador de captura pokemon")
        opcion = input("Avanzar? (s/n) ")
        if opcion == 's':
            play()
        elif opcion == 'n':
            print("Fin del simulador")
        else:
            print("Entrada incorrecta")
            
if __name__ == "__main__":
    menu()


