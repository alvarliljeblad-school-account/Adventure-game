import Character
import Item
import Room
import random


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