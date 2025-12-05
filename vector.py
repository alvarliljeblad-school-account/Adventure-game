import math
class Vec2:
    def __init__(self,x:int,y:int):
        self.x:int = x
        self.y:int = y
    def __add__(self,other):
        return Vec2(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vec2(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return Vec2(self.x*other,self.y*other)
    def __abs__(self) -> float:
        return math.hypot(self.x,self.y)