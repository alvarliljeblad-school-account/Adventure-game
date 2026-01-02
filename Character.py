import gameInput
from vector import Vec2
import termcolor
import random
import math
import Item
from dice import Dice
import CharacterClass
from action import Action
import Gear.Armour
import combat
import Gear.weapons
class Character:
    """Class for the player character, containing stats and methods for displaying them"""
    level_thresholds:dict = {1:0,2:300,3:900,4:2700,5:6500,6:14000,7:23000,8:34000,9:48000,10:64000}
    def __init__(self):
        #Xp, character level and other simple stats not dependent on class or ability scores
        self.xp: int = 0 # Xp base stat
        self.level:int # Level is determinded from xp stat
        self.proficiency_bonus:int # The bonus given if character is proficient in something, Determined from level
        self.charcter_class:CharacterClass.CharacterClass = CharacterClass.Fighter()
        self.name:str

        #The characters ability scores
        self.strength: int = 10
        self.dexterity:int = 10
        self.constitution: int = 10
        self.intelligence:int = 10
        self.wisdom: int = 10
        self.charisma:int = 10

        # Ability modifiers detirmined by the ability scores
        self.str_mod:int
        self.dex_mod:int
        self.con_mod:int
        self.int_mod:int
        self.wis_mod:int
        self.cha_mod:int

        # Lists of character features
        self.armour_proficiencies: list[str]
        self.weapon_proficiencies: list[str]
        self.save_proficiencies: list[str]
        self.skill_proficiencies: list[str]
        self.saving_throws:dict = {"str":0,"dex":0,"con":0,"int":0,"wis":0,"cha":0}
        self.resistances:list = []
        self.vulnerabilities:list = []
        self.immunities:list = []
        self.features:list
        self.action_list: list
        self.inventory: list = []
        self.Lhand:Item.Item = None
        self.Rhand:Item.Item = None
        self.armour:Item.Armour = None
        

        #Other stats determined from base stats
        self.hit_dice: Dice = Dice("1d10")
        self.max_hp: int = 0
        self.hp: int = 0
        self.ac:int = 0
        self.actions:int = 0
        self.movement:int = 0
        self.action_uses:dict = {} 

        self.pos: Vec2 = Vec2(0,0)
        #Characters inventory
        self.calculate_stats()
        self.hp = self.max_hp
        print(self.level)
    def calculate_stats(self):
        """Recalculates the characters stats and abilities"""
        #determine character level
        for i in range(1,len(self.level_thresholds)+1):
            if self.level_thresholds[i] <= self.xp:
                self.level = i
        #Detirmine proficciency bonus
        self.proficiency_bonus = math.ceil(self.level/4)+1
        self.armour_proficiencies =[]
        self.weapon_proficiencies = ["Unarmed"]
        self.save_proficiencies = []
        self.skill_proficiencies = []

        # Get Feats
        self.features = []
        self.action_list = []
        for level in range(1,self.level+1):
            self.features += self.charcter_class.features[level]
        for feat in self.features:
            feat.calculate(self)
        
        self.action_list.append(Action("Attack",self.try_attack))
        

        #Detirmine ability modifiers
        self.str_mod = math.floor((self.strength-10)/2)
        self.dex_mod = math.floor((self.dexterity-10)/2)
        self.con_mod = math.floor((self.constitution-10)/2)
        self.int_mod = math.floor((self.intelligence-10)/2)
        self.wis_mod = math.floor((self.wisdom-10)/2)
        self.cha_mod = math.floor((self.charisma-10)/2)

        if self.armour == None:
            self.ac = 10+self.dex_mod
        else:
            self.ac = self.armour.ac + max(self.dex_mod, self.armour.dex_cap)

        self.max_hp = self.charcter_class.max_hp
        self.max_inventory = 3*self.strength
        self.actions = 1
        self.movement = 30
        self.remaining_actions = self.actions
        self.remaining_movement = self.movement
        self.defence = math.floor(self.strength/2)
        for item in self.inventory:
            item.gain(self)
    def read_character(path):
        file = open(file=path)
        attribute_line = file.readline(0)
        file.close()
        attribute_line = attribute_line.strip()
        attributes = attribute_line.split(" ")
        char = Character()
        char.xp = int(attributes[0])
        char.pos = Vec2(int(attributes[1]),int(attributes[2]))
        ... #add inventory import 
    def write_character(self,path):
        ... # add character saving

    def display_stats(self) -> None:
        """Prints the players current stats"""
        print(f"""
                Stats:
            Hp: {self.hp}/{self.max_hp}
            AC: {self.ac}
            Level: {self.level}/Xp:{self.xp}
            Strength: {self.strength} ({self.str_mod:+})
            Dexterity: {self.dexterity} ({self.dex_mod:+})
            Constitution: {self.constitution} ({self.con_mod:+})
            Intelligence: {self.intelligence} ({self.int_mod:+})
            Wisdom: {self.wisdom} ({self.wis_mod:+})
            Charisma: {self.charisma} ({self.cha_mod:+})""")
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
        return self.str_mod
    def get_defence(self) -> int:
        return self.defence
    def take_damage(self, damage: int) -> None:
        self.hp -= damage
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

    def try_attack(self,world):
        self.remaining_actions-=1
        print("What enemy do you want to attack, write enemy number")
        enemy_inp = int(gameInput.get_str_input(range(len(world.enemies))))
        print("What weapon do you use:")
        possible_attacks = ["P"]
        if self.Lhand != None:
            print(f"L: {self.Lhand}")
            possible_attacks.append("L")
        if self.Rhand != None:
            print(f"R: {self.Rhand}")
            possible_attacks.append("R")
        print("P:Punch")
        weapon_inp = gameInput.get_str_input(possible_attacks)
        if weapon_inp == "l":
            weapon = self.Lhand
        if weapon_inp == "r":
            weapon = self.Rhand
        if weapon_inp == "p":
            weapon = Gear.weapons.ImprovisedWeapons.unarmed

        combat.melee_weapon_attack(self,world.enemies[enemy_inp],weapon)
        


    def take_action(self,world):
        print("What action do you want to do?")
        for i,action in enumerate(self.action_list):
            print(f"{i}:{action.name}")
        inp = int(gameInput.get_str_input(list(range(len(self.action_list)))))
        self.action_list[inp].function(self,world)
    def take_turn(self, world):
        #Check if dead
        if self.hp <= 0:
            return False
        self.calculate_stats() # Recalculate stats
        self.remaining_actions = self.actions
        self.remaining_movement = self.movement
        while self.remaining_actions > 0 or self.remaining_movement > 0:
            print(f"Hp: {self.hp}/{self.max_hp}, Str: {self.get_strength()}, Level: {self.level}, Actions: {self.remaining_actions}/{self.actions}, Movement: {self.remaining_movement}/{self.movement}")
            print(world)
            print("""A: Left  S: Down   W: Up   D: Right    T: Attack   I: Show inventory   C:Check stats   P:Pass  E: Use action""")
            inp = gameInput.get_str_input(["A","S","W","D","T","I","C","P","E"])
            if inp == "p":
                self.remaining_actions = 0
                self.remaining_movement = 0
            elif inp == "i":
                self.display_inventory()
                gameInput.pause()
            elif inp == "c":
                self.display_stats()
                gameInput.pause()
            elif inp == "t":
                self.try_attack(world)
            elif inp == "e":
                if self.remaining_actions > 0:
                    self.take_action(world)
                else:
                    print(termcolor.colored("Out of actions","red"))
            elif inp == "a":
                if world.walls[self.pos.y][self.pos.x-1]:
                    print("There is a wall in the way")
                elif self.remaining_movement > 0:
                    self.pos.x-=1
                    self.remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))
            elif inp == "d":
                if world.walls[self.pos.y][self.pos.x+1]:
                    print("There is a wall in the way")
                elif self.remaining_movement > 0:
                    self.pos.x+=1
                    self.remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))
            elif inp == "w":
                if world.walls[self.pos.y-1][self.pos.x]:
                    print("There is a wall in the way")
                elif self.remaining_movement > 0:
                    self.pos.y-=1
                    self.remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))
            elif inp == "s":
                if world.walls[self.pos.y+1][self.pos.x]:
                    print("There is a wall in the way")
                elif self.remaining_movement > 0:
                    self.pos.y+=1
                    self.remaining_movement-=1
                else:
                    print(termcolor.colored("Out of movement","red"))
            #Remove dead enemies
            world.enemies = list(filter(lambda a: a.hp > 0, world.enemies))
        return True