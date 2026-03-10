import random

class Pokemon:
    def __init__(self, name, type_, health, attack):
        self.name = name
        self.type_ = type_
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_opponent(self, opponent):
        print(f"{self.name} attacks {opponent.name}!")
        opponent.take_damage(self.attack)
        print(f"{opponent.name} has {opponent.health} health left.")

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, pokemon):
        print(f"{pokemon.name} uses {self.name}!")
        if self.effect == 'heal':
            health_increase = random.randint(10, 30)
            pokemon.health += health_increase
            print(f"{pokemon.name} heals for {health_increase} health!")
        elif self.effect == 'boost_attack':
            attack_increase = random.randint(2, 8)
            pokemon.attack += attack_increase
            print(f"{pokemon.name}'s attack is boosted by {attack_increase}!")

def create_opponents():
    opponents = [
        Pokemon("Opponent 1", "Fire", 50, 5),
        Pokemon("Opponent 2", "Water", 50, 5),
        Pokemon("Opponent 3", "Grass", 50, 5),
        Pokemon("Opponent 4", "Electric", 50, 5),
        Pokemon("Opponent 5", "Psychic", 50, 5),
        Pokemon("Opponent 6", "Ice", 50, 5),
        Pokemon("Opponent 7", "Bug", 50, 5),
        Pokemon("Opponent 8", "Rock", 50, 5),
        Pokemon("Opponent 9", "Ghost", 50, 5),
        Pokemon("Opponent 10", "Dragon", 50, 5)
    ]
    return opponents

def create_items():
    items = [
        Item("Potion", "heal"),
        Item("Super Potion", "heal"),
        Item("Attack Boost", "boost_attack"),
        Item("Defensive Shield", "boost_attack"),
        Item("Rare Candy", "heal"),
        Item("Mighty Leaf", "boost_attack"),
        Item("Elixir", "heal"),
        Item("Revive", "heal"),
        Item("Berserk Mushroom", "boost_attack"),
        Item("Golden Egg", "heal")
    ]
    return items

def battle(pokemon, opponent):
    while pokemon.is_alive() and opponent.is_alive():
        pokemon.attack_opponent(opponent)
        if opponent.is_alive():
            opponent.attack_opponent(pokemon)
        print("---")

def main():
    players_choice = Pokemon("Pikachu", "Electric", 100, 10)
    opponents = create_opponents()
    items = create_items()

    for opponent in opponents:
        print(f"A wild {opponent.name} appears!")
        battle(players_choice, opponent)
        if not players_choice.is_alive():
            print("You were defeated!")
            break
        else:
            print(f"You defeated {opponent.name}!")
            item = random.choice(items)
            item.use(players_choice)
    else:
        print("You have defeated all opponents!")

if __name__ == "__main__":
    main()