import Character
import Room
import gameInput

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
    #Create a player character        
    player = Character.Character(3,10)
    #Keep lopping if the player is alive
    while player.hp > 0:
        #check for if the player has won
        if player.level >= 10:
            win()
        #Take player input and decide what to do
        print("""What would you like to do?
              1: See stats || 2: See inventory
              3: Use item  || 4: Enter a room
              q: quit game""")
        selection = gameInput.get_str_input(["1","2","3","4","q"],"Selection ->")
        if selection == "1":
            player.display_stats() #prints stats
            input("Press enter to continue") # Pause to let the player read stats
        elif selection == "2":
            player.display_inventory() # Prints the players inventory
            input("Press enter to continue") # Pause to let the player read stats
        elif selection == "3":
            player.use_item() # Lets the player choose an item to use
        elif selection == "4":
            Room.generate_room(player) # Lets the player choose between 3 doors to enter
        elif selection == "q":
            return # Exits the main function therefore closing the program
        else:
            print("Invalid selection please try again") # Case for if the player gives invalid input
    #If the loop ends, the player has died
    death()


if __name__ == "__main__":
    main()