import Item
class LightArmour:
    Padded = Item.Armour("Padded armour", 8, 11, 255, True, "LArmour")
    Leather = Item.Armour("Leather armour", 10, 11, 255, False, "LArmour")
    Studded = Item.Armour("Studed leather armour", 13, 12, 255, False, "LArmour")
class MediumArmour:
    Hide = Item.Armour("Hide armour", 12, 12, 2, False, "MArmour")
    ChainShirt = Item.Armour("Chain shirt", 20, 13, 2, False, "MArmour")
    ScaleMail = Item.Armour("Scale mail", 45, 14, 2, True, "MArmour")
    Breastplate = Item.Armour("Breastplate", 20, 14, 2, False, "MArmour")
    HalfPlate = Item.Armour("Half plate armour", 40, 15, 2, True, "MArmour")
class HeavyArmour:
    RingMail = Item.Armour("Ring mail", 40, 14, 0, True, "HArmour")
    ChainMail = Item.Armour("Chain mail", 55, 16, 0, True, "HArmour")
    Splint = Item.Armour("Splint armour", 60, 17, 0 , True, "HHrmour")
    Plate = Item.Armour("Plate armour", 65, 18, 0, True, "Harmour")