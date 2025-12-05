from Character import Character
import Room
from gameInput import get_str_input
from world import World
MAP_FILE = "floor_layouts.txt"
def win() -> None:
    """Prints the win text"""
    print("You have won!!")
    print("Hooray!")

def death() -> None:
    """Prints the death/loss text"""
    print("You died")
    print("Boohoo")

def start() -> World:
    """Start function, contains all setup code executed when the game stars"""
    print("Welcome to the game")
    print("What floor would you like to go to")
    floor_id = get_str_input(["1"])
    player = Character(4,4)
    floor = World.open_layout_from_file(MAP_FILE,floor_id,player)
    return floor

def main() -> None:
    """Main function of the program, contains the mainloop"""
    floor = start()
    while True:
        floor.take_turn()


if __name__ == "__main__":
    main()