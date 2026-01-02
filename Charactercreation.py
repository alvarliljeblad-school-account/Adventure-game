import Character
import gameInput
import CharacterClass
import dice
def create_custom_character():
    char = Character.Character()
    print("What class you want your character to be?")
    print("Fighter")
    inp = gameInput.get_str_input(["Fighter"])
    if inp == "Fighter":
        char.charcter_class = CharacterClass.Fighter()
    distribute_ability_scores(char)
    gain_equipment(char)
    print("You start with your inventory containing")
    print("You have to equip them manually")
    char.display_inventory()
    print("Character creation is now done")
    gameInput.pause()

def distribute_ability_scores(char:Character.Character):
    print("Next up is distibuting ability scores")
    gameInput.pause()
    print("You will distribute 6 scores for the 6 different stats")
    print("Strength(Str), Dexterity(Dex), Constitution(Con), Intelligence(Int), Wisdom(Wis) and Charisma(Cha)")
    gameInput.pause()
    ability_scores = [roll_stat() for _ in range(6)]
    ability_scores.sort()
    print("The scores to distribute are:")
    print(ability_scores)
    print("What score do you put in strength?")
    inp = gameInput.get_str_input(ability_scores)
    char.strength = int(inp)
    ability_scores.remove(inp)
    print("What score do you put in dexterity?")
    inp = gameInput.get_str_input(ability_scores)
    char.dexterity = int(inp)
    ability_scores.remove(inp)
    print("What score do you put in constitution?")
    inp = gameInput.get_str_input(ability_scores)
    char.constitution = int(inp)
    ability_scores.remove(inp)
    print("What score do you put in intelligence?")
    inp = gameInput.get_str_input(ability_scores)
    char.intelligence = int(inp)
    ability_scores.remove(inp)
    print("What score do you put in wisdom?")
    inp = gameInput.get_str_input(ability_scores)
    char.wisdom = int(inp)
    ability_scores.remove(inp)
    print("What score do you put in charisma?")
    inp = gameInput.get_str_input(ability_scores)
    char.charisma = int(inp)
    ability_scores.remove(inp)
    
def gain_equipment(char:Character.Character):
    char.inventory += char.charcter_class.starting_equipment

def load_preset():
    ...
def create_character() -> Character.Character:
    print("Do you want to create a custom character(C) or use a premade one(P)?")
    inp = gameInput.get_str_input(["C","P"])
    if inp == "c":
        create_custom_character()
    else:
        load_preset()


def roll_stat() -> int:
    """Rolls 4d6 and removes the lowest"""
    dice_list = [dice.Dice("1d6").roll() for _ in range(4)]
    dice_list.sort()
    dice_list.pop(0)
    return int(sum(dice_list))+1


if __name__ == "__main__":
    print(roll_stat())