import Features
class CharacterClass:
    features = {}
    def __init__(self):
        pass

class Fighter(CharacterClass):
    features = {0:Features.AbilityScoreIncrease()}