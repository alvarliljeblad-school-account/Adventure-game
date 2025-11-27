from Character import Character
from vector import Vec2
from enemy import Enemy
import termcolor
class World:
    def __init__(self):
        self.player: Character = Character(3,10)
        self.enemies: list[Enemy] = []
        self.walls: list[list[bool]] = [[False for _ in range(10)] for _ in range(10)]
        self.dijkstra_grid: list[list[int]] = [[99999 if b else 1000 for b in a] for a in self.walls]
    def generate_dijkstra(self):
        self.dijkstra_grid = [[99999 if b else 1000 for b in a] for a in self.walls]
        changed = True
        while changed:
            changed = False
            for y in range(len(self.dijkstra_grid)):
                for x in range(len(self.dijkstra_grid[y])):
                    if self.walls[y][x]:
                        self.dijkstra_grid[y][x] == 99999
                    elif self.player.pos.x == x and self.player.pos.y == y:
                        self.dijkstra_grid[y][x] = 0
                    else:
                        min_neighbour = 1000
                        if x != 0:
                            min_neighbour = min(min_neighbour,self.dijkstra_grid[y][x-1])
                        if x != len(self.dijkstra_grid[y])-1:
                            min_neighbour = min(min_neighbour,self.dijkstra_grid[y][x+1])
                        if y != 0:
                            min_neighbour = min(min_neighbour,self.dijkstra_grid[y-1][x])
                        if y != len(self.dijkstra_grid)-1:
                            min_neighbour = min(min_neighbour,self.dijkstra_grid[y+1][x])
                        if min_neighbour +1 < self.dijkstra_grid[y][x]:
                            self.dijkstra_grid[y][x] = min_neighbour + 1
                            changed = True
    def __str__(self):
        floormap = [[termcolor.colored("▮ ", "white") if wall else termcolor.colored("▯ ","white") for wall in row] for row in self.walls]
        floormap[self.player.pos.y][self.player.pos.x] = termcolor.colored("P ", "light_magenta")
        for enemy in self.enemies:
            floormap[enemy.pos.y][enemy.pos.x] = termcolor.colored("E ","red")
        return "".join(["".join(row)+"\n" for row in floormap])
        

if __name__ == "__main__":
    test = World()
    test.enemies.append(Enemy(3,3))
    test.walls[3][2] = True
    test.generate_dijkstra()

    print(test)