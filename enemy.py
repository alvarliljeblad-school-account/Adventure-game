from vector import Vec2
class Enemy:
    """Class for enemies"""
    def __init__(self,strength: int, hp: int, damage:int, pos:Vec2):
        self.strength: int = strength
        self.hp: int = hp
        self.max_hp: int = hp
        self.damage: int = damage
        self.pos: Vec2 = pos
    def take_turn(self,world):
        min_neighbour:int = world.dijkstra_grid[self.pos.y][self.pos.x]
        min_pos:Vec2 = self.pos
        print(min_neighbour)
        if self.pos.x != 0:
            if world.dijkstra_grid[self.pos.y][self.pos.x-1] < min_neighbour:
                min_neighbour = world.dijkstra_grid[self.pos.y][self.pos.x-1]
                min_pos = self.pos + Vec2(-1,0)
        print(min_neighbour)
        if self.pos.x != len(world.dijkstra_grid[self.pos.y])-1:
            if world.dijkstra_grid[self.pos.y][self.pos.x+1] < min_neighbour:
                min_neighbour = world.dijkstra_grid[self.pos.y][self.pos.x+1]
                min_pos = self.pos + Vec2(1,0)
        print(min_neighbour)
        if self.pos.y != 0:
            if world.dijkstra_grid[self.pos.y-1][self.pos.x] < min_neighbour:
                min_neighbour = world.dijkstra_grid[self.pos.y-1][self.pos.x]
                min_pos = self.pos + Vec2(0,-1)
        print(min_neighbour)
        if self.pos.y != len(world.dijkstra_grid)-1:
            if world.dijkstra_grid[self.pos.y+1][self.pos.x] < min_neighbour:
                min_neighbour = world.dijkstra_grid[self.pos.y+1][self.pos.x]
                min_pos = self.pos + Vec2(0,1)
        print(min_neighbour)
        print(world.dijkstra_grid)
        print(min_neighbour,min_pos)
        if min_neighbour != 0:
            self.pos = min_pos
        else:
            ... #Attack player