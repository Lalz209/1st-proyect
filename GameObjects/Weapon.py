class Weapon():
    def __init__(self, name: str, damage: list, optionNumber: int):
        self.name = name
        self.damage = damage
        self.optionNumber = optionNumber

    def __repr__(self):
        return f'\t-({self.optionNumber}) {self.name} Damage {self.damage[0]}-{self.damage[1]}.'

    def get_warrior_weapons():
        return [Weapon("Long Sword", [10,15], 1), Weapon("Dual Sword", [7,18], 2), Weapon("Axe", [12,13], 3)]
    
    def get_wizard_weapons():
        return [Weapon("Crosier", [12,17], 1), Weapon("Magic Wand", [9,21], 2), Weapon("Magic Book", [14,15], 3)]
    
    def get_Assassin_weapons():
        return [Weapon("Dual Knife", [15,20], 1), Weapon("Katana", [12,24], 2), Weapon("Hidden Shit", [17,18], 3)]
    
    def get_weapons(classType):
        match classType:
            case 'Warrior':
                return Weapon.get_warrior_weapons()
            case 'Wizard':
                return Weapon.get_wizard_weapons()
            case 'Assassin':
                return Weapon.get_Assassin_weapons()

    def get_weapons_text(classType):
        match classType:
            case 'Warrior':
                return '\n'.join([str(x) for x in Weapon.get_warrior_weapons()])
            case 'Wizard':
                return '\n'.join([str(x) for x in Weapon.get_wizard_weapons()])
            case 'Assassin':
                return '\n'.join([str(x) for x in Weapon.get_Assassin_weapons()])

