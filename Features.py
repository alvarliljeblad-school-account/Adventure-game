from dice import Dice
from action import Action
class Feature:
    def calculate(self,character):
        pass

class HitPoints(Feature):
    def __init__(self,hit_dice: Dice):
        super().__init__()
        self.hit_dice: Dice = hit_dice
    def calculate(self, character):
        character.hit_dice = self.hit_dice
        character.max_hp = self.hit_dice.max_value-(self.hit_dice.average_value+0.5) + ((self.hit_dice.average_value+0.5)+character.con_mod)*character.level

class Proficiencies(Feature):
    def __init__(self,armour,weapons,tools,saves,skills):
        super().__init__()
        self.armour = armour
        self.weapons = weapons
        self.tools = tools
        self.saves = saves
        self.skills = skills
    def calculate(self, character):
        character.armour_proficiencies += self.armour
        character.weapon_proficiencies += self.weapons
        character.tool_proficiencies += self.tools
        character.save_proficiencies += self.saves
        character.skill_proficiencies += self.skills


class AbilityScoreIncrease(Feature):
    def __init__(self):
        super().__init__()
        self.ability_increases = {"str":100,"dex":0,"con":0,"int":0,"wis":0,"cha":0}
    def calculate(self, character):
        character.strength += self.ability_increases["str"]
        character.dexterity += self.ability_increases["dex"]
        character.constitution += self.ability_increases["con"]
        character.intelligence += self.ability_increases["int"]
        character.wisdom += self.ability_increases["wis"]
        character.charisma += self.ability_increases["cha"]


############### Fighter Features

class SecondWind(Feature):
    def __init__(self):
        super().__init__()
    def calculate(self, character):
        if "Second Wind" in character.action_uses:
            character.action_uses["Second Wind"] = 1
        character.action_list.append(Action("Second Wind",self.use))
    def use(self,character,world):
        character.hp += Dice("1d10").roll() + character.level
        
