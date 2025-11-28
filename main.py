import Character
import Room
import gameInput
from world import World

def win() -> None:
    """Prints the win text"""
    print("You have won!!")
    print("Hooray!")

def death() -> None:
    """Prints the death/loss text"""
    print("You died")
    print("Boohoo")

def main() -> None:
    """Main function of the program, contains the mainloop"""
    floor = World()
    floor.player = Character.Character(5,3) 
    floor.take_turn()


if __name__ == "__main__":
    main()