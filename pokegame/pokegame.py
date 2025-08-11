from pokemon import Pokemon
import requests
import json
import random

file_name = "pokegame/data.json"
base_url = "https://pokeapi.co/api/v2/"
pokemon_team = []

def get_pokemon_info(poke):
    url = f"{base_url}pokemon/{poke}"
    response = requests.get(url)
    return response.json()

def save_values(pokemon_team, file_name):
    with open(file_name, 'w') as f:
        json.dump(pokemon_team, f)

def load_values(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:
        save_values([], file_name)

if __name__ == "__main__":
    load_values(file_name)
    pokemon_team = [Pokemon("bulbasaur", 1, "grass", "TensiK"), Pokemon("charmander", 4, "fire", "TensiK"), Pokemon("squirtle", 7, "water", "TensiK")]
    save_values(pokemon_team, file_name)
    print("Pokémon team")
    for poke in pokemon_team:
        poke.showPokemon(poke.name, poke.pokeid,poke.poketype)

# OBJETOS NO SON COMPATIBLES, DEBEMOS IMPORTAR PICKLE PARA PODER GUARDAR OBJETOS
# CREAR UN CLI EN EL QUE PUEDAS IR A LA WILDERNESS Y TRAS ESPERAR UN NÚMERO ALEATORIO DE SEGUNDOS QUE TE APAREZCA UN POKÉMON
# DAR LA OPCIÓN DE CAPTURAR O NO A ESE POKÉMON Y SI ES QUE SÍ QUE HAYA UNA PROBABILIDAD DE ATRAPARLO
# TENER UN EQUIPO DE HASTA 6 POKÉMONS Y DAR LA OPCIÓN DE LIBERAR PARA PODER CAPTURAR NUEVOS Y MEJORES
# CARGAR DIFERENTES PERFILES EN FUNCIÓN DE CADA DUEÑO Y QUE CADA UNO DE ELLOS TENGA SU EQUIPO