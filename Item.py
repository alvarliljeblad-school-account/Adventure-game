import random
class Item:
    """Class for items"""
    def __init__(self,name:str,weight:int):
        """Each item has a name"""
        self.name: str = name
    def gain(self,char) -> None:
        """Function when the character gains the item"""
        pass
    def activate(self,char) -> None:
        """Function for when the character uses the item"""
        char.inventory.remove(self)
    def __str__(self) -> None:
        """Returns a string of the item"""
        return f"+{self.potency} {self.name}"

class MeleeWeapon(Item):
    def __init__(self, name,weight, damage, damage_type,proficiency):
        super().__init__(name,weight)
        self.damage = damage
        self.damage_type = damage_type
        self.proficiency = proficiency