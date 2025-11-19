class Character:
    """Class for the player character, containing stats and methods for displaying them"""
    def __init__(self,strength, hp):
        self.strength: int = strength
        self.strength_bonus:int = 0
        self.hp: int = hp
        self.max_hp: int = hp
        self.inventory: list = []
        self.level:int = 1
        self.damage: int = 3
    def display_stats(self):
        """Prints the players current stats"""
        print(f"""
                Stats:
            Hp: {self.hp}/{self.max_hp}
            Level: {self.level}
            Strength: base: {self.strength} + items: {self.strength_bonus} = {self.strength+ self.strength_bonus}""")
        input("Press enter to continue") # to pause until the player presses enter
    def display_inventory(self):
        """Prints the constents of the playes inventory"""
        print("Inventory:")
        for i in range(len(self.inventory)):
            print(f"{i}: {self.inventory[i]}")
        input("Press enter to continue") #Pause until the player presses enter
    def add_to_inventory(self, item):
        """Adds an item to invetory"""
        self.inventory.append(item)
        item.gain(self)
    def get_strength(self):
        return self.strength+self.strength_bonus