import random
import dice
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

class Weapon(Item):
    def __init__(self, name:str,weight:int, damage_list:list,proficiency:str,properties:list):
        super().__init__(name,weight)
        self.damage_list = damage_list
        self.proficiency = proficiency
        self.properties = properties

class MeleeWeapon(Weapon):
    def __init__(self, name:str, weight:int, damage_list:list, proficiency:str, properties:list):
        super().__init__(name, weight, damage_list, proficiency, properties)

class Armour(Item):
    def __init__(self, name:str, weight:int, ac:int, dex_cap:int, stealth_disadvantage:bool,proficiency:str):
        super().__init__(name, weight)
        self.ac = ac
        self.dex_cap =dex_cap
        self.stealth_disadvantage = stealth_disadvantage
        self.proficiency = proficiency