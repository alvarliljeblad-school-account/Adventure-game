class Room:
    def enter(self,char):
        pass
class Chest(Room):
    def __init__(self,chest_item):
        self.chest_item = chest_item
    def enter(self, char):
        ...