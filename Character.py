class Character:
    def __init__(self,strength, hp):
        self.strength: int = strength
        self.strength_bonus:int = 0
        self.hp: int = hp
        self.max_hp: int = hp
        self.inventory: list = []
        self.level:int = 1
    def display_stats(self):
        print(f"""
                Stats:
            Hp: {self.hp}/{self.max_hp}
            Level: {self.level}
            Strength: base: {self.strength} + items: {self.strength_bonus} = {self.strength+ self.strength_bonus}""")
    def display_inventory(self):
        print("Inventory:")
        for i in len(self.inventory):
            print(f"{i}: {self.inventory[i].name}")
