import Features
class CharacterClass:
    features = {}
    def __init__(self):
        pass

class Fighter(CharacterClass):
    features = {
        1:[
            Features.Proficiencies(["LArmour","MArmour","HArmour"],["SWeapon","MWeapon"],[],["str","con"],["Acrobatics","History"])
            ,Features.AbilityScoreIncrease()
            ,Features.SecondWind()
        ]
    }