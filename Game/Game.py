from GameUI.Constants import Constants as gc
from GameObjects.Weapon import Weapon
from GameObjects.PlayerClasses import Warrior, Wizard, Assassin
import random

class Game():
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.playerTypes = [Warrior, Wizard, Assassin]
        self.isSinglePlayer = False

    @staticmethod
    def print_wall(num=1):
        """
        Print a wall of text of size passed in.
        Default size is 1.

        >>> print_wall(2)
        ////////////////////////////////////////
        ////////////////////////////////////////
        """
        print(f'{gc.wall_text}\n' * num, '\n')

    def equip_bot(self, bot):
        possible_weapons = bot.get_weapons()
        bot.weapon = possible_weapons[random.randint(0, len(possible_weapons)-1)]

    def equip_player(self, player):
        option = 0
        print(f"Please select your {player.type.lower()}'s weapon:")
        possible_weapons = Weapon.get_weapons(player.type)
        while option not in [1, 2, 3]:
            option = int(input(f'{Weapon.get_weapons_text(player.type)}\n'))
        player.weapon = possible_weapons[option-1]

    def create_player_random(self):
        name = gc.rand_player_names[random.randint(0, len(gc.rand_player_names)-1)]
        player_type = self.playerTypes[random.randint(0, 2)]
        return player_type(name)

    def create_player_with_input(self):
        name = input(gc.name_input)
        player_type = 0
        player_input_text = '\n'.join([f'\t({i+1}). {self.playerTypes[i].type}: {self.playerTypes[i].description}' for i in range(3)])
        while player_type not in [1, 2, 3]:
            player_type = int(input(f'{player_input_text}\n').lower())
        return self.playerTypes[player_type-1](name)
    
    def create_player(self, playerControlled=False):
        if playerControlled:
            return self.create_player_controlled()
        else:
            return self.create_player_with_input()
        
    def calculate_real_damage(self, player):
        return player.Damage + random.randint(player.weapon.damage[0], player.weapon.damage[1])

    def calculate_fight(self, player1, player2):
        def print_fight_status(player_number, damage):
            player_number -= 1 # to use as index 0 or 1
            players = [player1, player2]
            self.print_wall()
            print(f"{players[player_number].name} has caused {damage} of damage to {players[int(not bool(player_number))].name} and now {players[int(not bool(player_number))].name} health is {players[int(not bool(player_number))].Health}.") # when you convert 1 to boolean it becomes True, and 0 becomes False, so you can use this to get the other player
            self.print_wall()
        
        def print_player_turn(player_number):
            player_number -= 1
            self.print_wall()
            print(f"Player {player_number} Turn!")
            self.print_wall()


        self.equip_player(self.player1)
        if self.isSinglePlayer:
            self.equip_bot(self.player2)
        else:
            self.equip_player(self.player2)
        
        while player1.isAlive() and player2.isAlive():
            player_turn = random.randint(1, 2) # se puede cambiar por otra estrategia
            print_player_turn(player_turn)
            if player_turn == 1:
                damage = self.calculate_real_damage(player1)
                player2.Health -= damage
                if player2.Health < 0:
                    player2.Health = 0
                    break
            else:
                damage = self.calculate_real_damage(player2)
                player1.Health -= damage
                if player1.Health < 0:
                    player1.Health = 0
                    break
            

            print_fight_status(player_turn, damage)
    
    def game_loop(self):
        
        while True:
            self.print_wall(2)
            print("Welcome to the game! Let's start creating the players!")
            self.print_wall(2)
            print("let's begin with player 1!")
            self.player1 = self.create_player()
            self.print_wall(2)
            print("Excellent selection! Continue with player 2!")
            self.print_wall(2)
            self.player2 = self.create_player()
            self.print_wall(2)
            print("Nice! This will be an epic fight!")
        
            print("Lets present our fighters!!")
            print("player 1 description!\n", self.player1)
            print("player 2 description!\n", self.player2)
        
            self.calculate_fight(self.player1, self.player2)
        
            if self.player2.Health < 0:
                print(self.player2.name, " is Dead! ", self.player1.name, "won the fight!")
            elif self.player1.Health < 0:
                print(self.player1.name, " is Dead! ", self.player2.name, "won the fight!")
            else:
                print("It was a tie!")



if __name__ == "__main__":
    import doctest
    doctest.testmod()