import dice
import Item
def deal_single_damage(target, damage:int, damage_type:str):
    if damage_type in target.resistances:
        damage /= 2
    if damage_type in target.vulnerabilities:
        damage *= 2
    if damage_type in target.immunities:
        damage = 0
    target.hp -= damage

def deal_damage(attacker, target,damage_list:list):
    """Takes a list of damages and damage types and applies all of them"""
    # This function is needed for when for example a poisoned weapon is used, then the weapon deals both it's normal damage and the poison damage
    
    calculated_damage_list = []
    print(damage_list)
    for damage in damage_list:
        if type(damage[0]) == int:
            # Dealing a set ammount of damage
            dmg = damage[0]
        elif type(damage[0]) == dice.Dice:
            # Dealing a random amount of damage
            dmg = damage[0].roll()
        elif type(damage[0]) == str:
            # Dealing damage equal to an ability modifier
            if damage[0] == "str":
                dmg = attacker.str_mod
            elif damage[0] == "dex":
                dmg = attacker.dex_mod
            elif damage[0] == "con":
                dmg = attacker.con_mod
            elif damage[0] == "int":
                dmg = attacker.con_mod
            elif damage[0] == "wis":
                dmg = attacker.wis_mod
            elif damage[0] == "cha":
                dmg = attacker.cah_mod
        calculated_damage_list.append((dmg,damage[1]))
        deal_single_damage(target,dmg,damage[1])
    damage_string = ""
    for attribute in calculated_damage_list:
        damage_string += f"{str(attribute[0])} {attribute[1]}"
    print(f"You deal {damage_string} damage")
            

def attack(attacker, target, damage_list:list, attack_modifier:int):
    """Code for resolving an attack"""
    natural_attack_roll = dice.Dice("1d20").roll()
    attack_roll = natural_attack_roll + attack_modifier
    print(f"You roll a {natural_attack_roll} + {attack_modifier} = {attack_roll}")
    if natural_attack_roll == 20:
        # If the attacker rolls a natural 20 deal damage twice
        print("A critical Hit, you deal damage twice")
        deal_damage(attacker, target,damage_list)
        deal_damage(attacker, target,damage_list)
    elif natural_attack_roll == 1:
        # If the attacker rolls a natural 1 they always miss
        return
    elif attack_roll > target.ac:
        # if the attacker rolls higher than the targets 
        deal_damage(attacker, target,damage_list)
    elif attack_roll <= target.ac:
        # If the attacker rills lower or equal to the ac they miss
        return

def melee_weapon_attack(attacker, target, weapon:Item.MeleeWeapon):
    distance = abs(attacker.pos-target.pos) # Calculats the distance between the position of the attacker and the target
    if distance*5 > 5:
        # If the enmy is further away than the weapons range the attck fails
        # The distance is multiplied by 5 because one tile on the board represents 5 feet of distance
        print("The enemy is too far away")
        return

    # If the weapon ha the finesse prroperty the attacker may use ther dex modifier instead of strength when calculating attack modifier
    if "Finesse" in weapon.properties:
        modifier = max(attacker.str_mod,attacker.dex_mod)
    else:
        modifier = attacker.str_mod

    if weapon.proficiency in attacker.weapon_proficiencies:
        modifier += attacker.proficiency_bonus
    
    attack(attacker, target,weapon.damage_list,modifier)