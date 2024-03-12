import random

class role():
    def __init__(self, name, type):
        self.name = input("What is your name?: ")
        self.type = input("Please select a class for your character: \nWarrior: Melee fighter that use different kind of weapons, with a big damage\nWizard: Range weapons to cast spells. wizards have different kinf of spells for any situation. \nAssasin: Big damage. King of shadows, and hidding but any mistake is dead.\n  ")
        