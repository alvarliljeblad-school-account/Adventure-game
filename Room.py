import random
import Item
import gameInput
class Room:
    def enter(self,char):
        pass
class Chest(Room):
    def __init__(self,chest_item):
        self.chest_item = chest_item
    def enter(self, char):
        print(f"You find a chest containing a {self.chest_item}")
        selection = input("Will you pick it up?(y/n) ->")
        if selection == "y":
            char.inventory.append(self.chest_item)
        else:
            print("You pass the item")
class Trap(Room):
    def __init__(self,damage):
        self.damage = damage
    def enter(self, char):
        print(f"You walk into a trap and take {self.damage} damage")
        char.hp -= self.damage
class Monster(Room):
    def __init__(self, strength, damage,hp):
        self.strength = strength
        self.damage = damage
        self.hp = hp
    def enter(self, char):
        print(f"You encounter a monster with {self.strength} strength, {self.damage} damage and {self.hp} hp")
        print("Do you 1: fight or 2: run")
        selection = gameInput.get_str_input(["1","2"])
        if selection == "1":
            #If player is weaker, they will take a hit of damage when running away
            if char.strength < self.strength:
                print(f"you run and take {self.damage} damage")
                char.hp -= self.damage
            else:
                print("you run away")
        elif selection == "2":
            while self.hp > 0 and char.hp > 0:
                #Roll a d20 for each and add their strength
                char_roll = random.randint(1,20) + char.strength
                monster_roll = random.randint(1,20) + self.strength
                if char_roll >= monster_roll:
                    self.hp -= char.damage
                elif monster_roll > char_roll:
                    char.hp -= self.damage
            if self.hp <= 0:
                char.lvl +=1
                char.strength += 1

        

def generate_room(char):
    doors = [Room.Chest(Item.Item.generate),Room.Monster(random.randint(1,5),random.randint(1,3),random.randint(5,20)),Room.Trap(random.randint(1,3))]
    doors = random.shuffle(doors)
    print("There are 3 doors, which do you enter")
    selection = gameInput.get_str_input(["1","2","3"])
    if selection == "1":
        doors[0].enter(char)
    elif selection == "2":
        doors[1].enter(char)    
    elif selection == "3":
        doors[2].enter(char)