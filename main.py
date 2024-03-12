import random

class Player:
    def __init__(self, name):
        self.name = name       
        


class Warrior(Player):
     def __init__(self, name):
          super().__init__(name)
          
     Health = 200
     Defense = 15
     Damage = 20
     weapon = ""

    
class Wizard(Player):
     def __init__(self, name):
          super().__init__(name)

     Health = 150
     Defense = 10
     Damage = 30
     weapon = ""

class Assasin(Player):
     def __init__(self, name):
          super().__init__(name)

     Health = 140
     Defense = 7
     Damage = 40
     weapon = ""

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

player1 = create_player()
print(player1.name)
print(player1.Defense)
