import Item
import dice
class SimpleMeleeWeapons:
    club = Item.MeleeWeapon("Club", 2, [(dice.Dice("1d4"),"Bludgeoning")],"SWeapon",["Light"])
    dagger = Item.MeleeWeapon("Dagger",1, [(dice.Dice("1d4"), "Piercing")],"SWeapon",["Finesse","Light"])
    