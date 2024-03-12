class Player:
    def __init__(self, name, type):
        self.name = name       
        self.defense = 10
        self.type = type

# Pedir al usuario que ingrese el nombre del jugador
player_name = input("Ingresa el nombre del jugador 1: ")


def select_role():
    player_type = input("Please select an option: \nWarrior: Melee fighter that use different kind of weapons, with a big damage\nWizard: Range weapons to cast spells. wizards have different kinf of spells for any situation. \nAssasin: Big damage. King of shadows, and hidding but any mistake is dead.\n  ").lower()
    
    return player_type


# Crear una instancia de la clase Player con el nombre proporcionado
player1 = Player(player_name, select_role())

# Ahora player1 tiene el nombre ingresado por el usuario
print("El nombre del jugador 1 es:", player1.name)
print(player1.defense)
print(player1.type)