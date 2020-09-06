import numpy as np
import time
from game_functions import printf, inputf, y_or_n

class Trainer:
    def __init__(self, name: str, location: str, money=1000, pokemon={}):
        self.name = name
        self.money = money
        self.pokemon = pokemon
        self.location = location

    def current_location(self):
        return f"You are currently in {self.location}"

    def __str__(self):
        return f"Pkmn Trainer {self.name}'s Trainer Card'\nStats:\nPokemon: {self.pokemon}\nMoney: {self.money}"

    # def PokemonInventory(self): just commenting for a test

    # def CapturePokemon(self):
    # global capture
    # capture = True

class Pokemon:
    def __init__(self, name, types, moves, EVs, health="=" * 25, exp=0):
        self.name = name
        self.moves = moves
        self.attack = EVs["ATTACK"]
        self.defense = EVs["DEFENSE"]
        self.health = health
        self.types = types
        self.bars = 20  # Amount of health bars
        self.exp = exp

    def fight(self, Pokemon2):
        # This allow 2 pokemons fight each other
        # Print fight information
        self.Pokemon2 = Pokemon2
        print("-------POKEMON BATTLE-------")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(1)

        # Consider type advantages
        version = ["Fire", "Water", "Grass"]
        for i, k in enumerate(version):
            if self.types == k:
                # Both are the same type
                if Pokemon2.types == k:
                    string_1_attack = "It's not very effective..."
                    string_2_attack = "It's not very effective..."
                # Pokemon2 is STRONG against pokemon1
                if Pokemon2.types == version[(i + 1) % 3]:
                    Pokemon.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "It's not very effective..."
                    string_2_attack = "It's super effective!"
                # Pokemon 2 is WEAK against Pokemon 1
                if Pokemon2.types == version[(i + 2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = "It's super effective!"
                    string_2_attack = "It's not very effective..."
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("Pick a move: "))
            printf(f"{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            printf(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus give a defense boost
            for j in range(int(Pokemon2.bars + 0.1 * Pokemon2.defense)):
                Pokemon2.health += "="
            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            # Check if the pokemon has fainted
            if Pokemon2.bars <= 0:
                printf(f"\n... {Pokemon2.name} fainted")
                break
            # ----------------------------------If Pokemon2's hasn't fainted, then it's Pokemon2's turn-------------------------
            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print("f{i+1}.", x)
            index = int(input("Pick a move: "))
            printf(f"{Pokemon2.name} used {moves[index-1]}!")
            time.sleep(1)
            printf(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus give a defense boost
            for j in range(int(self.bars + 0.1 * self.defense)):
                Pokemon2.health += "="
            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            # Check if the pokemon has fainted
            if self.bars <= 0:
                printf("\n...", self.name + " fainted")
                break
        money = np.random.choice(5000)
        printf(f"Opponent paid you {money}.")
    def PokemonState(self):
        print(
            "Your pokemon has: ",
            self.health,
            "\nYour pokemon has: ",
            self.exp,
            "exp points",
            "\nYour pokemon has: ",
            self.attack,
            "attack",
            "\nYour pokemon has: ",
            self.defense,
            "defense",
        )


#--------------------Testing
Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})
#
# list_of_class_instances = {"Charizard": Charizard, "Blastoise": Blastoise, "Venusaur": Venusaur}
#
# for i in list_of_class_instances:
#     list_of_class_instances[i].PokemonState()

# Charizard.fight(Venusaur)
#
# Venusaur.PokemonState()

#
def pkmn_fight(player, rival_pkmn, catch=False):
    for pokemon in player.pokemon:
        pokemon_obj = player.pokemon[pokemon]
        if len(pokemon_obj.health) != 0:
            pokemon_obj.fight(rival_pkmn)
            break

    if catch:
        if y_or_n(inputf(f"Would you like to catch {rival_pkmn.name}?[Y/n]\t")):
            if y_or_n(inputf(f"Would you like to nickname {rival_pkmn.name}?[Y/n]\t")):
                nick = inputf(f"Enter {rival_pkmn.name}'s nickname:\t")
                player.pokemon[nick] = rival_pkmn


hero_volty = Trainer("Volty", "Pallet Town", money=1000, pokemon={"Flareo": Charizard})

pkmn_fight(hero_volty, Venusaur, catch=True)

print(hero_volty.pokemon)
