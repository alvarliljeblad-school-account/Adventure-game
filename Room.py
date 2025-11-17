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