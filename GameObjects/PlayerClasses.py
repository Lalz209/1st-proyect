class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def __repr__(self):
        return f"name: {self.name}, \n Type: {self.type}, \n Health: {self.Health}, \n Damage: {self.Damage}, \n Defense: {self.Defense}"
    
    def isAlive(self):
        return self.Health > 0


class Warrior(Player):
    description = "Melee fighter that use different kind of weapons, with a big damage"
    type = "Warrior"
    def __init__(self, name):
        super().__init__(name)
        self.Health = 200
        self.Defense = 15
        self.Damage = 20
    


class Wizard(Player):
    description = "Range weapons to cast spells. wizards have different kinf of spells for any situation."
    type = "Wizard"
    def __init__(self, name):
        super().__init__(name)
        self.Health = 150
        self.Defense = 10
        self.Damage = 30
    

    def turn():
        pass


class Assassin(Player):
    description = "Big damage. King of shadows, and hidding but any mistake is dead."
    type = "Assassin"
    def __init__(self, name):
        super().__init__(name)
        self.Health = 140
        self.Defense = 7
        self.Damage = 40
        self.weapon = 0
        
