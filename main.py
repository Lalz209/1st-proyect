import random

class Player:
    def __init__(self, name):
        self.name = name     

    def isAlive(self):
      return self.Health > 0 
    
    

class Warrior(Player):
     def __init__(self, name):
          super().__init__(name)
          
     Health = 200
     Defense = 15
     Damage = 20
     weapon = 0
     type = "Warrior"



class Wizard(Player):
     def __init__(self, name):
          super().__init__(name)

     Health = 150
     Defense = 10
     Damage = 30
     weapon = 0
     type = "Wizard"

     def turn():
         pass
          


class Assasin(Player):
     def __init__(self, name):
          super().__init__(name)

     Health = 140
     Defense = 7
     Damage = 40
     weapon = 0
     type = "Assasin"




def select_role():
    player_type = 0
    while player_type != 1 and player_type != 2 and player_type != 3:
      player_type = int(input("Please select an option: \nWarrior(1): Melee fighter that use different kind of weapons, with a big damage\nWizard(2): Range weapons to cast spells. wizards have different kinf of spells for any situation. \nAssasin(3): Big damage. King of shadows, and hidding but any mistake is dead.\n  ").lower())
    
    return player_type


def create_player():
    option = select_role()
    name = input("What is yor name?: ")
    if option == 1:
         player = Warrior(name)
    elif option == 2:
         player = Wizard(name)
    elif option == 3:
         player = Assasin(name)
    return player


def equipment(player):
      option = 0
      if player.type == "Warrior":
        while option != 1 and option != 2 and option != 3:
          option = int(input("Please select your warrior's weapon: \n-Long Sword(1): Damage 10-15. \n-Dual Sword(2): Damage 7-18 \n-Axe(3): Damage 12-13\n"))
        return option
      elif  player.type == "Wizard":
        while option != 1 and option != 2 and option != 3:
          option = int(input("Please select your wizard's weapon: \n-Crosier(1): Damage 12-17. \n-Magic Wand(2): Damage 9-21 \n-Magic Book(3): Damage 14-15\n"))
        return option
      elif  player.type == "Assasin":
        while option != 1 and option != 2 and option != 3:
          option = int(input("Please select your assain's weapon: \n-Dual Knife(1): Damage 15-20. \n-Katana(2): Damage 12-24 \n-Hidden Shit(3): Damage 17-18\n"))
        return option


def real_damage(player, option):

    if player.type == "Warrior":
        if option == 1:
            return player.Damage + random.randint(10,15)
        elif option == 2:
            return player.Damage + random.randint(7,18)
        elif option == 3:
            return player.Damage + random.randint(12,13)
    if player.type == "Wizard":
        if option == 1:
            return player.Damage + random.randint(12,17)
        elif option == 2:
            return player.Damage + random.randint(9,21)
        elif option == 3:
            return player.Damage + random.randint(14,15)
    if player.type == "Assasin":
        if option == 1:
            return player.Damage + random.randint(15,20)
        elif option == 2:
            return player.Damage + random.randint(12,24)
        elif option == 3:
            return player.Damage + random.randint(17,18)
        
    
def Fight(player, plaier):
    
        plaier.Health -= real_damage(player, equipment(player))
        print(plaier.Health)

def turn():
    while player.isAlive() and plaier.isAlive():
    Fight()




player1 = create_player()
player2 = create_player()



""""
print("////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////")
print("Welcome to the game! Let's start creating the players!")
print("////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////")
print("let's begin with player 1!")
player1 = create_player()
print("////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////")
print("Excellent selection! Continue with player 2!")
print("////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////")
player2 = create_player()
print("////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////")
print("Nice! This will be an epic fight!")

print("Lets present our figthers!!")
print("player 1 description! \n name: ", player1.name, " \n Type: ", player1.type, "\n Health: ", player1.Health, "\n Damage: ", player1.Damage, "\n Defense: ", player1.Defense)
print("player 2 description! \n name: ", player2.name, " \n Type: ", player2.type, "\n Health: ", player2.Health, "\n Damage: ", player2.Damage, "\n Defense: ", player2.Defense)
"""