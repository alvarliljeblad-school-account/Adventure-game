from vector import Vec2
import random
import dice
class Enemy:
    """Class for enemies"""
    def __init__(self,
                 name:str,
                 ac:int, 
                 hp:dice.Dice, 
                 speed:int, 
                 proficiency_bonus:int, 
                 challange:float, str_mod:int ,
                 dex_mod:int,
                 con_mod:int,
                 int_mod:int,
                 wis_mod:int,
                 cha_mod:int, 
                 actions:int):
        self.name:str = name
        self.ac:int = ac
        self.hp:int = hp
        self.speed:int = speed
        self.proficiency_bonus:int = proficiency_bonus

        self.challange:float = challange
        
        self.str_mod:int = str_mod
        self.dex_mod:int = dex_mod
        self.con_mod:int = con_mod
        self.int_mod:int = int_mod
        self.wis_mod:int = wis_mod
        self.cha_mod:int = cha_mod

        self.actions:list = actions
        
        self.pos:Vec2
        
    def __str__(self):
        return f"Enemy at pos: {str(self.pos)}"
    def get_xp(self) -> int:
        return self.strength*self.hp*self.damage
    def get_strength(self) -> int:
        return self.strength
    def get_defence(self) -> int:
        return self.defence
    def take_damage(self, damage: int) -> int:
        self.hp -= damage
    def attack(self,opponent):
        attack_roll = random.randint(1,20)
        attack_value = attack_roll + self.get_strength()
        if attack_roll == 20:
            print(f"Critical hit! You take {self.damage*2} damage")
            opponent.take_damage(self.damage)
        elif attack_value >= opponent.get_defence():
            opponent.take_damage(self.damage)
            print(f"You take {self.damage} damage")
        else:
            print(f"The enemy misses")
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
            self.attack(world.player)