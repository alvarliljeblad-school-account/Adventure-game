class Item:
    def __init__(self,name:str,potency:int):
        self.name: str = name
        self.potency: int = potency
    def gain(self,char):
        pass
    def activate(self,char):
        pass
    def discard(self,char):
        pass

class PassiveStrengthItem(Item):
    def gain(self, char):
        char.strength_bonus += self.potency
    def discard(self, char):
        char.strength_bonus -= self.potency

class HealingItem(Item):
    def activate(self, char):
        char.hp = min(char.hp+self.potency,char.max_hp)
        char.inventory.remove(self)
