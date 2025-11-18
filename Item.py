import random
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
    def __str__(self):
        return f"+{self.potency} {self.name}"
    def generate():
        if random.randint(0,1) == 1:
            return PassiveStrengthItem.generate()
        else:
            return HealingItem.generate()

class PassiveStrengthItem(Item):
    names = ["Amulet of strenth","Ring of strength","Bracer","Strength rune"]
    def gain(self, char):
        char.strength_bonus += self.potency
    def discard(self, char):
        char.strength_bonus -= self.potency
    def generate():
        return PassiveStrengthItem(random.choice(PassiveStrengthItem.names),random.randint(1,4))

class HealingItem(Item):
    names = ["Health potion","Healing draught","Medicine box"]
    def activate(self, char):
        char.hp = min(char.hp+self.potency,char.max_hp)
        char.inventory.remove(self)
    def generate():
        return HealingItem(random.choice(HealingItem.names),random.randint(1,4))

