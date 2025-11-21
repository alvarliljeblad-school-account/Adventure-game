import gameInput
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
    def display_inventory(self):
        """Prints the constents of the playes inventory"""
        print("Inventory:")
        for i in range(len(self.inventory)):
            print(f"{i}: {self.inventory[i]}")
    def add_to_inventory(self, item):
        """Adds an item to invetory"""
        self.inventory.append(item)
        item.gain(self)
    def get_strength(self):
        """Return the characters strength with all bonuses added"""
        return self.strength+self.strength_bonus
    def use_item(self):
        """Lets the player choose an item and then activates that items activate function"""
        # If the inventory is empty you cannot use an item
        if len(self.inventory)==0:
            print("You have no items")
            return
        self.display_inventory()
        itemid = gameInput.get_str_input(list(range(len(self.inventory)))+["c"],"What item would you like to use or c to cancel -> ")
        if itemid == "c":
            print("You decide not to use an item")
            return
        self.inventory[int(itemid)].activate(self)