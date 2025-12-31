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
        challange=0.25,
        str_mod=-1,
        dex_mod=2,
        con_mod=0,
        int_mod=0,
        wis_mod=-1,
        cha_mod=-1,
        actions=[goblin_scimiar]
        )