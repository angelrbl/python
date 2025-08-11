class Pokemon:
    def __init__(self, name, pokeid, poketype, owner):
        self.name = name
        self.pokeid = pokeid
        self.poketype = poketype
        self.owner = owner
    
    def showPokemon(self, name, pokeid, poketype):
        print(f"INFO:\nName: {name}\nID: {pokeid}\nType: {poketype}")
    
    def showOwner(self, name, owner):
        print(f"This {name} is owned by {owner}")

if __name__ == "__main__":
    bulbasaur = Pokemon("bulbasaur", 1, "grass", "TensiK")
    bulbasaur.showPokemon(bulbasaur.name, bulbasaur.pokeid, bulbasaur.poketype)

