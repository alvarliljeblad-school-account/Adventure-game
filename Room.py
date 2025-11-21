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
            char.add_to_inventory(self.chest_item)
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
        while self.hp > 0 and char.hp > 0:
            print("Do you 1: fight or 2: run")
            selection = gameInput.get_str_input(["1","2"])
            if selection == "2":
                #If player is weaker, they will take a hit of damage when running away
                if char.get_strength() < self.strength:
                    print(f"you run and take {self.damage} damage")
                    char.hp -= self.damage
                else:
                    print("you run away")
                return
            elif selection == "1":
                #Roll a d20 for each and add their strength
                char_roll = random.randint(1,20)
                char_total = char_roll+char.get_strength()
                print(f"You roll a {char_roll} for at total of {char_total}")
                monster_roll = random.randint(1,20)
                monster_total = monster_roll+self.strength
                print(f"The monster rolls a {monster_roll} for a total of {monster_total}")
                if char_total >= monster_total:
                    self.hp -= char.damage
                    print(f"You deal {char.damage} damage to the monster")
                elif monster_total > char_total:
                    char.hp -= self.damage
                    print(f"the monster deals {self.damage} damage to you")
        if self.hp <= 0:
            print("You level up, your strength increases by 1")
            char.level +=1
            char.strength += 1


        

def generate_room(char):
    doors = [Chest(Item.Item.generate()),Monster(random.randint(1,5),random.randint(1,3),random.randint(5,20)),Trap(random.randint(1,3))]
    random.shuffle(doors)
    print(doors)
    print("There are 3 doors, which do you enter")
    selection = gameInput.get_str_input(["1","2","3"])
    if selection == "1":
        doors[0].enter(char)
    elif selection == "2":
        doors[1].enter(char)    
    elif selection == "3":
        doors[2].enter(char)