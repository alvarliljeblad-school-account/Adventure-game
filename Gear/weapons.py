import Item
import dice
class ImprovisedWeapons:
    unarmed = Item.MeleeWeapon("Unarmed Strike",0, [(1,"Bludgeoning"), ("str", "Bludgeoning")], "Unarmed", [])
class SimpleMeleeWeapons:
    club = Item.MeleeWeapon("Club", 2, [(dice.Dice("1d4"),"Bludgeoning")],"SWeapon",["Light"])
    dagger = Item.MeleeWeapon("Dagger",1, [(dice.Dice("1d4"), "Piercing")],"SWeapon",["Finesse","Light"])
    