import random

class Pokemon:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

class Opponent:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, pokemon):
        if 'heal' in self.effect:
            pokemon.heal(self.effect['heal'])
        elif 'boost' in self.effect:
            pokemon.attack += self.effect['boost']
        elif 'damage' in self.effect:
            # Apply damage logic if needed
            pass


def battle(pokemon_team, opponent):
    print(f"Battling {opponent.name}")
    for pokemon in pokemon_team:
        while opponent.pokemon.is_alive() and pokemon.is_alive():
            opponent.pokemon.take_damage(pokemon.attack)
            print(f"{pokemon.name} attacked {opponent.pokemon.name}!")
            if opponent.pokemon.is_alive():
                pokemon.take_damage(opponent.pokemon.attack)
                print(f"{opponent.pokemon.name} attacked {pokemon.name}!")


def main():
    # Create Pokemon
    pikachu = Pokemon("Pikachu", 100, 20)
    charizard = Pokemon("Charizard", 120, 25)
    # ... add more pokemon

    team = [pikachu, charizard] # Example team

    # Create opponents
    opponents = [Opponent("Opponent1", Pokemon("Squirtle", 80, 15)), 
                 Opponent("Opponent2", Pokemon("Bulbasaur", 90, 18))] # Add more opponents

    # Create items
    items = [
        Item("Potion", {'heal': 20}),
        Item("Max Potion", {'heal': 50}),
        # ... add more items with various effects
    ]

    # Example of a battle
    for opponent in opponents:
        battle(team, opponent)

if __name__ == "__main__":
    main()
