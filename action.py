class Action:
    def __init__(self,name:str,function):
        self.name = name
        self.function = function
    def use(self,character):
        self.function(character)