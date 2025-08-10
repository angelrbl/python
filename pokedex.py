import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(poke):
    url = f"{base_url}pokemon/{poke}"
    response = requests.get(url)
    return response.json()
    

def show_pokemon_info(poke):
    print("Pokémon info: ")
    print(f"Name: {poke["name"]}")
    print(f"ID: {poke["id"]}")
    if len(poke["types"]) > 1:
        print(f"Types: {poke["types"][0]["type"]["name"]}, {poke["types"][1]["type"]["name"]}")
    else:
        print(f"Type: {poke["types"][0]["type"]["name"]}")

def input_pokemon():
    name_id = input("Please, input the name/ID of the desired pokémon: ")
    try:
        pokemon = get_pokemon_info(name_id)
        show_pokemon_info(pokemon)

        input_pokemon() if input("\nDo you want to search another pokémon? (y/n): ") == 'y' else print("See you soon!")
    except:
        print("An error ocurred or the pokémon was not found, please, try again...")
        input_pokemon()

if __name__ == "__main__":
    input_pokemon()