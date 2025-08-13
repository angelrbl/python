from pokemon import Pokemon
import requests
import pickle
import random
import time

file_name = "pokegame/data.pickle"
base_url = "https://pokeapi.co/api/v2/"
pokemon_data = []
pokemon_team = []
user = ""

# Esta función se encarga de recibir los datos de PokéAPI
def get_pokemon_info(poke):
    url = f"{base_url}pokemon/{poke}"
    response = requests.get(url)
    match response.status_code:
        case 200:
            return response.json()
        case 404:
            print("Something went wrong while trying to search a pokémon.")

# Estas funciones se encargan de guardar, cargar y borrar los cambios.
def save_values(pokemon_data, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(pokemon_data, f)

def load_values(file_name):
    try:
        with open(file_name, 'rb') as f:
            return pickle.load(f)
    except:
        save_values([], file_name)

def clear_values(file_name, data):
    data = []
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)
    main()

# esta lógica hace que tras cargar todos los pokémons capturados, solo los que le pertenecen al jugador deseado se carguen en el equipo
def load_team(data):
    pokemon_team = []
    for poke in data:
        if poke.owner == user:
            pokemon_team.append(poke)
    return pokemon_team

# Esta función se encarga de formalizar un pokémon deseado a un objeto
def convert_pokemon(poke):
    return Pokemon(poke["name"], poke["id"], poke["types"][0]["type"]["name"], user)

# Esta función se encarga de manejar el encuentro con un pokémon salvaje
def encounter_poke():
    wild_poke = get_pokemon_info(random.randint(1, 1025))
    print(f"\n{'Searching' if random.randint(1,2) ==  1 else 'Looking'} for wild pokemon...")
    for i in range(0, random.randint(2,7)):
        print(".")
        time.sleep(1)
    print(f"You {'encountered' if random.randint(1,2) ==  1 else 'found'} a wild {wild_poke['name']}.")
    action = input("Do you want to try and catch this pokémon? (y/n): ")
    match action:
        case 'y':
            catch_pokemon(wild_poke, pokemon_team)
        case 'n':
            print("Alright, going back home...")
            main()
        case _:
            print("Sorry, you wasted your chance and the pokémon ran away. Going back home...")
            main()

# This function handles the action of catching a pokémon
def catch_pokemon(poke, team):
    caught = True
    if len(pokemon_team) < 6:
        print(f"You threw a pokeball to {poke["name"]}")
        for i in range(0, 3):
            print('.')
            time.sleep(1)
            if random.randint(1, 2048) < poke["base_experience"]:
                caught = False
                print(f"{'The pokémon ran away' if random.randint(1,2) == 1 else 'The pokeball failed to hit the pokémon, and he got scared away'}")
                main()
                break
        if caught == True:
            print(f"Congratulations! You caught a wild pokémon. Welcome to the team, {poke["name"]}!\nGoing back home...")
            pokemon_data.append(convert_pokemon(poke))
            save_values(pokemon_data, file_name)
            main()
    else:
        print("Sorry, but your team is full. You should have thought about that earlier.")
        main()

# Esta función se encarga de enseñar el equipo pokémon de un jugador
def show_team(team):
    if len(team) > 0:
        print("\nYour team:")
        for poke in team:
            print(f"[{team.index(poke)}] {poke.name}")
    else:
        print("Sorry, but your team is empty. Going back home...")
        main()
    
# Tras enseñar el equipo del jugador, da la opción de ver cada pokémon individualmente
def see_team(team):
    show_team(team)
    action = input("See info of specific pokémon or press enter to go back home: ")
    match action:
        case '':
            main()
        case _:
            if int(action) >= 0 and int(action) < len(team):
                team[int(action)].showPokemon(team[int(action)].name, team[int(action)].pokeid, team[int(action)].poketype)
                main()
            else:
                print("The slot of the pokémon you introduced does not exist. Going back home...")
                main()

# Esta funcion te deja liberar un pokémon después de mostrar el equipo
def release_pokemon(team, data):
    show_team(team)
    action = input("Introduce the pokémon you want to release or press enter to go back home: ")
    match action:
        case '':
            main()
        case _:
            if int(action) >= 0 and int(action) < len(team):
                data.remove(team[int(action)])
                save_values(data, file_name)
                print(f"Bye, bye {team[int(action)].name}!")
                main()
            else:
                print("The slot of the pokémon you introduced does not exist. Going back home...")
                main()

# Esta función permite cambiar de jugador en el propio juego
def introduce_player():
    global user # poninedo "global" conseguimos acceder al valor ya creado que se llama "user"
    user = input("Please, type the name of the person who is playing: ")

# Salir del juego, no sin primero guardar
def exit():
    save_values(pokemon_data, file_name)
    print("Alright, see you soon!")

def main():
    pokemon_team = load_team(pokemon_data)
    print("\nHome:")
    print("[1] Go to the wilderness") 
    print("[2] See your team") 
    print("[3] Release pokémon") 
    print("[4] Change player") 
    print("[0] Exit")

    action = input("What do you want to do?: ")
    match action:
        case "1":
            encounter_poke()
        case "2":
            see_team(pokemon_team)
        case '3':
            release_pokemon(pokemon_team, pokemon_data)
        case '4':
            introduce_player()
            main()
        case 'clear':
            clear_values(file_name, pokemon_data)
        case _:
            print("Alright, see you soon!")

if __name__ == "__main__":
    introduce_player()
    pokemon_data = load_values(file_name)
    main()

# OBJETOS NO SON COMPATIBLES, DEBEMOS IMPORTAR PICKLE PARA PODER GUARDAR OBJETOS -> DONE
# CREAR UN CLI EN EL QUE PUEDAS IR A LA WILDERNESS Y TRAS ESPERAR UN NÚMERO ALEATORIO DE SEGUNDOS QUE TE APAREZCA UN POKÉMON -> DONE
# DAR LA OPCIÓN DE CAPTURAR O NO A ESE POKÉMON Y SI ES QUE SÍ QUE HAYA UNA PROBABILIDAD DE ATRAPARLO -> DONE
# TENER UN EQUIPO DE HASTA 6 POKÉMONS Y DAR LA OPCIÓN DE LIBERAR PARA PODER CAPTURAR NUEVOS Y MEJORES -> DONE
# CARGAR DIFERENTES PERFILES EN FUNCIÓN DE CADA DUEÑO Y QUE CADA UNO DE ELLOS TENGA SU EQUIPO -> DONE

# ARREGLAR BUG CUANDO ENSEÑAS EQUIPO SE AÑADEN POKEMONS MOMENTÁNEAMENTE Y LOS PRINTEA CON EL MISMO INDEX. IDEA -> PRINT(POKEMON_TEAM) -> DONE
# ARREGLAR BUG NO SE PUEDE CAMBIAR DE JUGADOR -> DONEc