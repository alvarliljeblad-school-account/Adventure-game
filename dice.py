class Dice:
    def __init__(self,ammount,sides=0):
        if type(ammount) == int:
            self.ammount = ammount
            self.sides = sides
        else:
            self.ammount = int(ammount.split("d")[0])
            self.sides = int(ammount.split("d")[1])
        self.max_value = sides
        self.average_value = (self.sides/2)+0.5