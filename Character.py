import gameInput
from vector import Vec2
import termcolor
class Character:
    """Class for the player character, containing stats and methods for displaying them"""
    def __init__(self,strength:int, hp:int):
        self.strength: int = strength
        self.strength_bonus:int = 0
        self.hp: int = hp
        self.max_hp: int = hp
        self.inventory: list = []
        self.level:int = 1
        self.damage: int = 3
        self.max_inventory: int = 5
        self.pos: Vec2 = Vec2(0,0)
        self.actions = 1
        self.movement = 5
    def display_stats(self) -> None:
        """Prints the players current stats"""
        print(f"""
                Stats:
            Hp: {self.hp}/{self.max_hp}
            Level: {self.level}
            Strength: base: {self.strength} + items: {self.strength_bonus} = {self.strength+ self.strength_bonus}""")
    def display_inventory(self) -> None:
        """Prints the constents of the playes inventory"""
        print("Inventory:")
        for i in range(len(self.inventory)):
            print(f"{i}: {self.inventory[i]}")
    def add_to_inventory(self, item) -> None:
        """Adds an item to invetory"""
        #Check if inventory is
        if len(self.inventory) == self.max_inventory:
            print("Your inventory is full")
            self.display_inventory()
            print("What item do you want to discard, c to cancel")
            choise = gameInput.get_str_input(list(range(self.inventory))+["c"])
            if choise == "c":
                print("You choose to not discard an item")
                return
            else:
                self.inventory.pop(int(choise)).discard(self)

        self.inventory.append(item)
        item.gain(self)
    def get_strength(self) -> int:
        """Return the characters strength with all bonuses added"""
        return self.strength+self.strength_bonus
    def use_item(self) -> None:
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
    def take_turn(self, world):
        remaining_actions = self.actions
        remaining_movement = self.movement
        while remaining_actions > 0 or remaining_movement > 0:
            print(f"Hp: {self.hp}/{self.max_hp}, Str: {self.get_strength()}, Level: {self.level}, Actions: {remaining_actions}/{self.actions}, Movement: {remaining_movement}/{self.movement}")
            print(world)
            print("""A: Left  S: Down   W: Up   D: Right    T: Attack   I: Show inventory   C:Check stats   P:Pass""")
            inp = gameInput.get_str_input(["A","S","W","D","T","I","C","P"])
            if inp == "p":
                remaining_actions = 0
                remaining_movement = 0
            elif inp == "i":
                self.display_inventory()
                gameInput.pause()
            elif inp == "c":
                self.display_stats()
                gameInput.pause()
            elif inp == "a":
                if world.walls[self.pos.y][self.pos.x-1]:
                    print("There is a wall in the way")
                elif remaining_movement > 0:
                    self.pos.x-=1
                    remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))
            elif inp == "d":
                if world.walls[self.pos.y][self.pos.x+1]:
                    print("There is a wall in the way")
                elif remaining_movement > 0:
                    self.pos.x+=1
                    remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))
            elif inp == "w":
                if world.walls[self.pos.y-1][self.pos.x]:
                    print("There is a wall in the way")
                elif remaining_movement > 0:
                    self.pos.y-=1
                    remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))
            elif inp == "s":
                if world.walls[self.pos.y+1][self.pos.x]:
                    print("There is a wall in the way")
                elif remaining_movement > 0:
                    self.pos.x+=1
                    remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))