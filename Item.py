import random
class Item:
    """Class for items"""
    def __init__(self,name:str,potency:int):
        """Each item has a name and potencty"""
        self.name: str = name
        self.potency: int = potency
    def gain(self,char) -> None:
        """Function when the character gains the item"""
        pass
    def activate(self,char) -> None:
        """Function for when the character uses the item"""
        char.inventory.remove(self)
    def discard(self,char) -> None:
        """Function for when the character loses the item"""
        pass
    def __str__(self) -> None:
        """Returns a string of the item"""
        return f"+{self.potency} {self.name}"
    def generate():
        """Creates a item of random type"""
        if random.randint(0,1) == 1:
            return PassiveStrengthItem.generate()
        else:
            return HealingItem.generate()

class PassiveStrengthItem(Item):
    """An item giving a passive strength bonus"""
    names = ["Amulet of strenth","Ring of strength","Bracer","Strength rune"]
    def gain(self, char) -> None:
        """Increases the characters strength bonus based on potency"""
        char.strength_bonus += self.potency
    def discard(self, char) -> None:
        """Decreases the characters strength bonus based on potency"""
        char.strength_bonus -= self.potency
    def generate():
        """Creates a passive strength item with a random name and potency"""
        return PassiveStrengthItem(random.choice(PassiveStrengthItem.names),random.randint(1,4))

class HealingItem(Item):
    """An item that can be used to regain health"""
    names = ["Health potion","Healing draught","Medicine box"]
    def activate(self, char) -> None:
        """The player regains health base on the items potency"""
        char.hp = min(char.hp+self.potency,char.max_hp)
        char.inventory.remove(self)
    def generate():
        """Creates a heling item with a random name and potency"""
        return HealingItem(random.choice(HealingItem.names),random.randint(1,4))