from vector import Vec2
class Enemy:
    """Class for enemies"""
    def __init__(self,strength, hp,damage,pos):
        self.strength: int = strength
        self.hp: int = hp
        self.max_hp: int = hp
        self.damage: int = damage
        self.pos: Vec2 = Vec2(2,2)
    def take_turn(self,world):
        ...
        