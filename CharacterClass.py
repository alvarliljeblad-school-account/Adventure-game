import Features
import Gear.Armour
import Gear.weapons
class CharacterClass:
    starting_equipment = []
    features = {}
    def __init__(self):
        pass

class Fighter(CharacterClass):
    starting_equipment = [Gear.Armour.HeavyArmour.ChainMail,Gear.weapons.MartialMeleeWeapons.Battleaxe]
    features = {
        1:[
            Features.Proficiencies(["LArmour","MArmour","HArmour"],["SWeapon","MWeapon"],["str","con"],["Acrobatics","History"])
            ,Features.SecondWind()
        ]
    }