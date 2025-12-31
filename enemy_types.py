import enemy
import dice
import action

def goblin_scimiar():
    ...

class enemyTable:
    goblin = enemy.Enemy(
        name="Goblin",
        ac=15,
        hp=7,
        speed=30,
        proficiency_bonus=2,
        xp=50,
        str_mod=-1,
        dex_mod=2,
        con_mod=0,
        int_mod=0,
        wis_mod=-1,
        cha_mod=-1,
        resistances=[],
        vulnerabilities=[],
        immunities=[],
        actions=[goblin_scimiar]
        )