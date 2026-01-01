import Item
import dice
class ImprovisedWeapons:
    unarmed = Item.MeleeWeapon("Unarmed Strike",0, [(1,"Bludgeoning"), ("str", "Bludgeoning")], "Unarmed", [])
class SimpleMeleeWeapons:
    club = Item.MeleeWeapon("Club", 2, [(dice.Dice("1d4"),"Bludgeoning")],"SWeapon",["Light"])
    dagger = Item.MeleeWeapon("Dagger", 1, [(dice.Dice("1d4"), "Piercing")],"SWeapon",["Finesse","Light"])
    greatclub = Item.MeleeWeapon("Greatclub", 10, [(dice.Dice("1d8"),"Bludgeoning")],"SWeapon",["Two-Handed"])
    Handaxe = Item.MeleeWeapon("Handaxe",2,[(dice.Dice("1d6"),"Slashing")], "SWeapon", ["Light"])
    Javelin = Item.MeleeWeapon("Javelin", 2, [(dice.Dice("1d6"), "Piercing")], "SWeapon", [])
    LightHammer = Item.MeleeWeapon("Light hammer", 2, [(dice.Dice("1d4"), "Bludgeoning")], "SWeapon",["Light"])
    Mace = Item.MeleeWeapon("Mace", 4, [(dice.Dice("1d6"),"Bludgeoning")], "SWeapon", [])
    Quarterstaff = Item.MeleeWeapon("Quarterstaff", 4, [(dice.Dice("1d8"), "Bludgeoning")], "Sweapon", ["Two-Handed"])
    Sickle = Item.MeleeWeapon("Sickle", 2, [(dice.Dice("1d4"), "Slashing")], "SWeapon", ["Light"])
    Spear = Item.MeleeWeapon("Spear", 3, [(dice.Dice("1d8"), "Piercing")], "SWeapon", ["Two-Handed"])
class MartialMeleeWeapons:
    Battleaxe = Item.MeleeWeapon("Battleaxe", 4, [(dice.Dice("1d10"), "Slashing")], "MWeapon", ["Two-Handed"])
    Flail = Item.MeleeWeapon("Flail", 2, [(dice.Dice("1d8"), "Bludgeoning")], "MWeapon", [])