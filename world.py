from Character import Character
from vector import Vec2
from enemy import Enemy
import termcolor
class World:
    def __init__(self):
        self.player: Character
        self.enemies: list[Enemy] = []
        self.walls: list[list[bool]] = [[False for _ in range(10)] for _ in range(10)]
        self.dijkstra_grid: list[list[int]] = [[99999 if b else 1000 for b in a] for a in self.walls]
    def generate_dijkstra(self) -> None:
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
    def open_layout_from_file(filename:str,floor_id:str,start_player:Character):
        """Returns a world from a layout file"""
        # Read file
        file = open(file=filename,mode="r")
        rawlines = file.readlines()
        file.close()
        rawlines = [line.strip() for line in rawlines] # Strip lines
        reading_mode = "" # Has not found the correct place to read
        map_objects = {"0":[0]} # Definition of all floor objects
        world_size = Vec2(5,5) # Default world size
        walls = [] # A nested list containing all walls
        player:Character = start_player # A referance to the player character
        enemies = [] # A list containig all enemies
        for line in rawlines: # Go line by line
            command_parts = line.split(" ") # Split the command
            if command_parts[0] == "@":
                # Look for the correct floor id denote by the @ sign
                if command_parts[1] == floor_id:
                    reading_mode = "data"
            elif reading_mode == "data":
                # Read data about the floor
                if command_parts[0] == "#": # Definitions for following map
                    map_objects[command_parts[1]] = command_parts[2::]
                elif command_parts[0] == "%": # Data
                    if command_parts[1] == "size":
                        # Sets map size
                        world_size = Vec2(int(command_parts[2]),int(command_parts[3]))
                    elif command_parts[1] == "map":
                        # Denotes that the map comes at the next line
                        reading_mode = "map"
                    elif command_parts[1] == "end":
                        # Ends the section
                        reading_mode = ""
            elif reading_mode == "map":
                # Code for reading the map
                mapline = [] # one line in the map
                for char in line:
                    # Lookup character in map objects
                    # Check if there is a wall
                    if map_objects[char][0] == "w":
                        mapline.append(True)
                    else:
                        mapline.append(False)
                    if map_objects[char][0] == "e":
                        # Check for enemies and add them to enemies
                        attributes = map_objects[char]
                        enemies.append(Enemy(attributes[1],attributes[2],attributes[3],Vec2(len(mapline)-1,len(walls))))
                    if map_objects[char][0] == "p":
                        # Check for player and set player position
                        player.pos = Vec2(len(mapline)-1,len(walls))
                # add the line to the bigger wall grid
                walls.append(mapline)
                # Check if the map is done
                if len(walls) == world_size.y:
                    reading_mode = "data"
    
        # When done create the world object and return it
        floor = World()
        floor.enemies = enemies
        floor.player = player
        floor.walls = walls
        floor.generate_dijkstra()
        return floor 
    def take_turn(self) -> None:
        self.player.take_turn(self)
        [enemy.take_turn() for enemy in self.enemies]

    def __str__(self) -> str:
        floormap = [[termcolor.colored("▮ ", "white") if wall else termcolor.colored("▯ ","white") for wall in row] for row in self.walls]
        floormap[self.player.pos.y][self.player.pos.x] = termcolor.colored("P ", "light_magenta")
        for enemy in self.enemies:
            floormap[enemy.pos.y][enemy.pos.x] = termcolor.colored("E ","red")
        return "".join(["".join(row)+"\n" for row in floormap])
        

if __name__ == "__main__":
    print(World.open_layout_from_file("floor_layouts.txt","1",Character(1,1)))