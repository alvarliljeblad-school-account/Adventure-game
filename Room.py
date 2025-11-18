import random
class Room:
    def enter(self,char):
        pass
class Chest(Room):
    def __init__(self,chest_item):
        self.chest_item = chest_item
    def enter(self, char):
        ...
class Trap(Room):
    def __init__(self,damage):
        self.damage = damage
    def enter(self, char):
        ...
class Monster(Room):
    def __init__(self, strength, damage):
        self.strength = strength
        self.damage = damage
    def enter(self, char):
        ...

def generate_room(char):
    doors = [Room.Chest(...),Room.Monster(random.randint(1,5),random.randint(1,3),Room.Trap(random.randint(1,3)))]
    doors = random.shuffle(doors)
    print("There are 3 doors, which do you enter")
    selection = input(" ->")
    if selection == "1":
        doors[0].enter(char)
    elif selection == "2":
        doors[1].enter(char)    
    elif selection == "3":
        doors[2].enter(char)
    else:
        print("Invalid input, you enter a door at random")
        random.choice(doors).enter(char)