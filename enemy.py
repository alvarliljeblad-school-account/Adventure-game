from vector import Vec2
class Enemy:
    """Class for enemies"""
    def __init__(self,strength, hp):
        self.strength: int = strength
        self.hp: int = hp
        self.max_hp: int = hp
        self.damage: int = 3
        self.pos: Vec2 = Vec2(0,0)
        