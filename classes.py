import numpy as np
import time
import os
import random
from game_functions import printf, inputf, y_or_n


turn = 0
loop = False

super_effective = {"normal":[],"fire":["grass","ice","bug","steel"],"water":["fire","ground","rock"],"electric":["water","flying"],"grass":["water","ground","rock"],"ice":["grass","ground","flying","dragon"],"fighting":["normal","ice","rock","dark","steel"],"poison":["grass","fairy"],"ground":["fire","electric","poison","rock","steel"],"flying":["grass","fighting","bug"],"psychic":["fighting","poison"],"bug":["grass","psychic","dark"],"rock":["fire","ice","flying","bug"],"ghost":["psychic","ghost"],"dragon":["dragon"],"dark":["psychic","ghost"],"steel":["ice","rock","fairy"],"fairy":["fighting","dragon","dark"]}
normal_effective = {"normal":["normal","fire","water","electric","grass","ice","fighting","poison","ground","flying","psychic","bug","dragon","dark","fairy"],"fire":["normal","electric","fighting","poison","ground","flying","psychic","ghost","dark","fairy"],"water":["normal","electric","ice","fighting","poison","flying","psychic","bug","ghost","dark","steel","fairy"],"electric":["normal","fire","ice","fighting","poison","psychic","bug","rock","ghost","dark","steel","fairy"],"grass":["normal","electric","ice","fighting","psychic","ghost","dark","fairy"],"ice":["normal","electric","fighting","poison","psychic","bug","rock","ghost","dark","fairy"],"fighting":["fire","water","electric","grass","fighting","ground","dragon"],"poison":["normal","fire","water","electric","ice","fighting","flying","psychic","bug","dragon","dark"],"ground":["normal","water","ice","fighting","ground","psychic","ghost","dragon","dark","fairy"],"flying":["normal","fire","water","ice","poison","ground","flying","psychic","ghost","dragon","dark","fairy"],"psychic":["normal","fire","water","electric","grass","ice","ground","flying","bug","rock","ghost","dragon","fairy"],"bug":["normal","water","electric","ice","ground","bug","rock","dragon"],"rock":["normal","water","electric","grass","poison","psychic","rock","ghost","dragon","dark","fairy"],"ghost":["fire","water","electric","grass","ice","fighting","poison","ground","flying","bug","rock","dragon","steel","fairy"],"dragon":["normal","fire","water","electric","grass","ice","fighting","poison","ground","flying","psychic","bug","rock","ghost","dark"],"dark":["normal","fire","water","electric","grass","ice","poison","ground","flying","bug","rock","dragon","steel"],"steel":["normal","grass","fighting","poison","ground","flying","psychic","bug","ghost","dragon","dark"],"fairy":["normal","water","electric","grass","ice","ground","flying","psychic","bug","rock","ghost","fairy"]}
not_very_effective = {"normal":["rock","steel"],"fire":["fire","water","rock","dragon"],"water":["water","grass","dragon"],"electric":["electric","grass","dragon"],"grass":["fire","grass","poison","flying","bug","dragon","steel"],"ice":["fire","water","ice","steel"],"fighting":["poison","flying","psychic","bug","fairy"],"poison":["poison","ground","rock","ghost"],"ground":["grass","bug"],"flying":["electric","rock","steel"],"psychic":["psychic","steel"],"bug":["fire","fighting","poison","flying","ghost","steel","fairy"],"rock":["fighting","ground","steel"],"ghost":["dark"],"dragon":["steel"],"dark":["fighting","dark","fairy"],"steel":["fire","water","electric","steel"],"fairy":["fire","poison","steel"]}
no_effect = {"normal":["ghost"],"fire":[],"water":[],"electric":["ground"],"grass":[],"ice":[],"fighting":["ghost"],"poison":["steel"],"ground":["flying"],"flying":[],"psychic":["dark"],"bug":[],"rock":[],"ghost":["normal"],"dragon":["fairy"],"dark":[],"steel":[],"fairy":[]}

class Trainer:
    def __init__(self, name: str, location: str, money=1000, pokemon={}):
        self.name = name
        self.money = money
        self.pokemon = pokemon
        self.location = location

    def current_location(self):
        return f"You are currently in {self.location}"

    def __str__(self):
        pokemon = ", ".join(pkmn for pkmn in self.pokemon)
        return f"Pkmn Trainer {self.name}'s Trainer Card'\nStats:\nPokemon: {pokemon}\nMoney: {self.money}"

    # def PokemonInventory(self): just commenting for a test

    # def CapturePokemon(self):
    # global capture
    # capture = True


class Pokemon:
    def __init__(self, name, types, moves, EVs, health="=" * 50, exp=0):
        self.name = name
        self.moves = moves
        self.attack = EVs["ATTACK"]
        self.defense = EVs["DEFENSE"]
        self.health = health
        self.types = types.split('-')
        self.bars = 50  # Amount of health bars
        self.exp = exp

    def local_fight(self, Pokemon2):
        # This allow 2 pokemons fight each other
        # Print fight information
        self.Pokemon2 = Pokemon2
        print("-------POKEMON BATTLE-------")
        print(f"\n{self.name}")
        print("TYPE/", "-".join(self.types))
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", "-".join(Pokemon2.types))
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))

        input("\nPress ENTER to continue...")
        os.system("clear")

        # type advantage calculator
        def effectiveness_calc(Pokemon1_types, Pokemon2_types):
            effectiveness = 1
            for pkmn1_type in Pokemon1_types:
                for pkmn2_type in Pokemon2_types:
                    if pkmn2_type in super_effective[pkmn1_type]:
                        effectiveness += 0.5
                    elif pkmn2_type in not_very_effective[pkmn1_type]:
                        effectiveness -= 0.25
                    elif pkmn2_type in no_effect[pkmn1_type]:
                        effectiveness = 0

            return effectiveness

        # modifies attack stat and changes script accordingly
        def attack_modifier(attack_stat, effectiveness):
            # Pokemon's typing doesnt affect the opponent pkmn
            if effectiveness == 0:
                attack_stat *= effectiveness
                return "It has no effect!"
            # Pokemon's typing is WEAK against opponent pkmn
            elif effectiveness > 0 and effectiveness < 1:
                attack_stat *= effectiveness
                return "It's not very effective..."
            # Pokemon has NORMAL effect against opponent pokemon
            elif effectiveness == 1:
                attack_stat *= effectiveness
                return ""
            # Pokemon is STRONG against opponent Pokemon
            elif effectiveness > 1:
                attack_stat *= effectiveness
                return "It's super effective!"

        # Consider type advantages
        self_effectiveness = effectiveness_calc(self.types, Pokemon2.types)
        pkmn2_effectiveness = effectiveness_calc(Pokemon2.types, self.types)

        # modifying attack stats according to type advantage
        string_1_attack = attack_modifier(self.attack, self_effectiveness)
        string_2_attack = attack_modifier(Pokemon2.attack, pkmn2_effectiveness)
        

        def Pokemon1_turn():
            while (self.bars > 0) and (Pokemon2.bars > 0):
                # Print the health of each pokemon
                if loop == False:
                    print(
                        f"{self.name}\t\tHLTH ({self.health.count('=')}) \t{self.health}"
                    )
                    print(
                        f"{Pokemon2.name}\t\tHLTH ({Pokemon2.health.count('=')}) \t{Pokemon2.health}\n"
                    )

                print(f"Go {self.name}!")
                for i, x in enumerate(self.moves):
                    print(f"{i+1}.", x)
                while True:
                    try:
                        index = int(input("Pick a move: "))
                    except ValueError:
                        print("Invalid move, try again.")
                        continue
                    if index>4:
                        print("Invalid number, try again.")
                        continue
                    break
                printf(f"{self.name} used {self.moves[index-1]}!")
                time.sleep(1)
                printf(string_1_attack)

                # Determine damage
                Pokemon2.bars -= self.attack
                Pokemon2.health = ""

                # Add back bars plus give a defense boost
                for _ in range(int(Pokemon2.bars + 0.1 * Pokemon2.defense)):
                    Pokemon2.health += "="
                time.sleep(1)
                global turn
                turn = 1
                time.sleep(0.5)

                # Check if the pokemon has fainted
                if Pokemon2.bars <= 0:
                    printf(f"\n... {Pokemon2.name} fainted")
                    turn = 10
                    break
                else:
                    os.system("clear")
                    print(
                        f"{self.name}\t\tHLTH ({self.health.count('=')}) \t{self.health}"
                    )
                    print(
                        f"{Pokemon2.name}\t\tHLTH ({Pokemon2.health.count('=')}) \t{Pokemon2.health}\n"
                    )
                    break

        # ----------------------------------If Pokemon2's hasn't fainted, then it's Pokemon2's turn-------------------------
        def Pokemon2_turn():

            while (self.bars > 0) and (Pokemon2.bars > 0):
                print(f"\nGo {Pokemon2.name}!")
                for i, x in enumerate(Pokemon2.moves):
                    print(f"{i+1}.", x)
                while True:
                    try:
                        index = int(input("Pick a move: "))
                    except ValueError:
                        print("Invalid move, try again.")
                        continue
                    break
                printf(f"{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
                time.sleep(1)
                printf(string_2_attack)

                # Determine damage
                self.bars -= Pokemon2.attack
                self.health = ""

                # Add back bars plus give a defense boost
                for _ in range(int(self.bars + 0.1 * self.defense)):
                    self.health += "="
                time.sleep(1)
                print(
                    f"{self.name}\t\tHLTH ({self.health.count('=')}) \t{self.health}"
                )

                print(
                    f"{Pokemon2.name}\t\tHLTH ({Pokemon2.health.count('=')}) \t{Pokemon2.health}\n"
                )
                global loop
                global turn
                loop = True
                turn = 0
                time.sleep(0.5)

                # Check if the pokemon has fainted
                if self.bars <= 0:
                    printf("\n..." + self.name + " fainted")
                    turn = 10
                    money = np.random.choice(5000)
                    printf(f"Opponent paid you {money}.")
                    break
                else:
                    os.system("clear")
                    print(
                        f"{self.name}\t\tHLTH ({self.health.count('=')}) \t{self.health}"
                    )
                    print(
                        f"{Pokemon2.name}\t\tHLTH ({Pokemon2.health.count('=')}) \t{Pokemon2.health}\n"
                    )
                    Pokemon1_turn()

        if turn == 0:
            Pokemon1_turn()
        if turn == 1:
            Pokemon2_turn()

    def wild_fight(self, Pokemon2):
        # This allow 2 pokemons fight each other
        # Print fight information
        self.Pokemon2 = Pokemon2
        print("-------POKEMON BATTLE-------")
        print(f"\n{self.name}")
        print("TYPE/", "-".join(self.types))
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", "-".join(Pokemon2.types))
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))

        input("\nPress ENTER to continue...")
        os.system("clear")

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
                    Pokemon2.attack *= 1.5
                    self.attack /= 1.5
                    string_1_attack = "It's not very effective..."
                    string_2_attack = "It's super effective!"
                # Pokemon 2 is WEAK against Pokemon 1
                if Pokemon2.types == version[(i + 2) % 3]:
                    self.attack *= 1.5
                    Pokemon2.attack /= 1.5
                    string_1_attack = "It's super effective!"
                    string_2_attack = "It's not very effective..."

        def Player_turn():
            while (self.bars > 0) and (Pokemon2.bars > 0):
                # Print the health of each pokemon
                if loop == False:
                    print(
                        f"{self.name}\t\tHLTH ({self.health.count('=')}) \t{self.health}"
                    )
                    print(
                        f"{Pokemon2.name}\t\tHLTH ({Pokemon2.health.count('=')}) \t{Pokemon2.health}\n"
                    )

                print(f"Go {self.name}!")
                for i, x in enumerate(self.moves):
                    print(f"{i+1}.", x)
                while True:
                    try:
                        index = int(input("Pick a move: "))
                    except ValueError:
                        print("Invalid move, try again.")
                        continue
                    if index>4:
                        print("Invalid number, try again.")
                        continue
                    break
                printf(f"{self.name} used {self.moves[index-1]}!")
                time.sleep(1)
                printf(string_1_attack)

                # Determine damage
                Pokemon2.bars -= self.attack
                Pokemon2.health = ""

                # Add back bars plus give a defense boost
                for _ in range(int(Pokemon2.bars + 0.1 * Pokemon2.defense)):
                    Pokemon2.health += "="
                time.sleep(1)
                global turn
                turn = 1
                time.sleep(0.5)

                # Check if the pokemon has fainted
                if Pokemon2.bars <= 0:
                    printf(f"\n... {Pokemon2.name} fainted")
                    turn = 10
                    break
                else:
                    os.system("clear")
                    print(
                        f"{self.name}\t\tHLTH ({self.health.count('=')}) \t{self.health}"
                    )
                    print(
                        f"{Pokemon2.name}\t\tHLTH ({Pokemon2.health.count('=')}) \t{Pokemon2.health}\n"
                    )
                    break

        # ----------------------------------If Pokemon2's hasn't fainted, then it's Pokemon2's turn-------------------------
        def Wild_Pokemon_Turn():

            while (self.bars > 0) and (Pokemon2.bars > 0):
                index = random.randrange(1,5)
                printf(f"{Pokemon2.name} turn!")
                input("\nPress ENTER to continue...")
                printf(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
                time.sleep(1)
                printf(string_2_attack)

                # Determine damage
                self.bars -= Pokemon2.attack
                self.health = ""

                # Add back bars plus give a defense boost
                for _ in range(int(self.bars + 0.1 * self.defense)):
                    self.health += "="
                time.sleep(1)
                global loop
                global turn
                loop = True
                turn = 0
                time.sleep(0.5)

                # Check if the pokemon has fainted
                if self.bars <= 0:
                    printf("\n..." + self.name + " fainted")
                    turn = 10
                    break
                else:
                    os.system("clear")
                    print(
                        f"{self.name}\t\tHLTH ({self.health.count('=')}) \t{self.health}"
                    )
                    print(
                        f"{Pokemon2.name}\t\tHLTH ({Pokemon2.health.count('=')}) \t{Pokemon2.health}\n"
                    )
                    Player_turn()

        if turn == 0:
            Player_turn()
        if turn == 1:
            Wild_Pokemon_Turn()

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



#
# def pkmn_battle(player, wild_pkmn):
#     for pokemon in player.pokemon:
#         pokemon_obj = player.pokemon[pokemon]
#         if len(pokemon_obj.health) != 0:
#             pokemon_obj.local_fight(wild_pkmn)
#             break

#     if y_or_n(inputf(f"Would you like to catch {wild_pkmn.name}?[Y/n]\t")):
#         if y_or_n(inputf(f"Would you like to nickname {wild_pkmn.name}?[Y/n]\t")):
#             nick = inputf(f"Enter {wild_pkmn.name}'s nickname:\t")
#             player.pokemon[nick] = wild_pkmn
#         else:
#             player.pokemon[wild_pkmn.name] = wild_pkmn


# def trainer_battle(player, trainer):
#     for pokemon in player.pokemon:
#         pokemon_obj = player.pokemon[pokemon]
#         print(player.pokemon)
#         while len(pokemon_obj.health) != 0:
#             for rival_pkmn in rival.pokemon:
#                 rival_pkmn_obj = rival.pokemon[rival_pkmn]
#                 pokemon_obj.local_fight(rival_pkmn_obj)


# def give_pkmn(player, pkmn):
#     printf(f"{player.name} received {pkmn.name}!")
#     if y_or_n(inputf(f"Would you like to nickname {pkmn.name}?[Y/n]\t")):
#         nick = inputf(f"Enter {pkmn.name}'s nickname:\t")
#         player.pokemon[nick] = pkmn
#     else:
#         player.pokemon[pkmn.name] = pkmn

# player = Trainer("Klaus", "Pallet Town", 0, {"charizard": Charizard })
# rival = Trainer("Ben", "Pallet Town", 0, {"venusaur": Venusaur, "blastoise": Blastoise})

# trainer_battle(player, rival)
