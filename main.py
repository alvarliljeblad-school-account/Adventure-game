import Character
import Item
import Room
import random
def generate_room(char):
    doors = [Room.Chest(...),Room.Monster(random.randint(1,5),random.randint(1,3),Room.Trap(random.randint(1,3)))]
    doors = random.shuffle(doors)
    print("There are 3 doors, which do you enter")
    selection = input(" ->")
    if selection == "1":
        doors[0].enter(char)
    elif selection == "2":
        doors[1].enter(char)    
    elif selection == "3":
        doors[2].enter(char)
    else:
        print("Invalid input, you enter a door at random")
        random.choice(doors).enter(char)

def main():
    player = Character.Character(3,10)
    while player.hp > 0:
        print("""What would you like to do?
              1: See stats || 2: See inventory
              3: Use item  || 4: Enter a room
              q: quit game""")
        selection = input("Selection ->")
        if selection == "1":
            player.display_stats()
        elif selection == "2":
            player.display_inventory()
        elif selection == "3":
            ...
        elif selection == "4":
            ...
        elif selection == "q":
            return
        else:
            print("Invalid selection please try again")


if __name__ == "__main__":
    main()