import Features
class CharacterClass:
    features = {}
    def __init__(self):
        pass

class Fighter(CharacterClass):
    features = {1:[Features.AbilityScoreIncrease(),Features.SecondWind()]}