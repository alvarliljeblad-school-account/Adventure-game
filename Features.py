class Feature:
    pass

class AbilityScoreIncrease(Feature):
    def __init__(self):
        super().__init__()
        self.increases = {"str":2,"dex":1,"con":3,"int":1,"wis":4,"cha":6}