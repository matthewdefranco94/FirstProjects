#practice

import sys

sys.path.append ('../../../../../../Desktop/Projects')

import random
# import WeaponSimulation
import numpy as np
import random
import matplotlib
from dataclasses import dataclass



#Attacks have a 40% chance to glance for 30% less damage, weaponskill reduces the 30% damage penatly
#Weapon skill affecting glancing penalty
def damage(weapon_top_end, weapon_bottom_end, added_weapon_skill, total_hit , crit_chance):
    glancing_chance_eff = 0.40
    glancing_dam_red_base = 0.30
    weapon_skill_reduction = 0.03
    base_miss = 0.28
    critical_strike_modifier = 1.5

    weapon_top_end = int(weapon_top_end)
    weapon_bottom_end = int(weapon_bottom_end)
    added_weapon_skill = int(added_weapon_skill)
    total_hit = int(total_hit)
    crit_chance = int(crit_chance)
    
    eff_miss = base_miss - total_hit / 100

    # Check if the attack landed at all
    hit_type = random.uniform(.01, 1.0)
    if hit_type > eff_miss:
        random_weapon_damage = random.randint(weapon_bottom_end , weapon_top_end)
        # Check if a regular or glancing attack
        # Regular hit
        if hit_type > eff_miss + glancing_chance_eff:
            # Critical strike
            if random.uniform(.01 , 1.0) <= crit_chance:
                effective_weapon_damage = random_weapon_damage * critical_strike_modifier
            # Non Crit
            else:
                effective_weapon_damage = random_weapon_damage
        # Glancing hit
        else:
            glancing_penalty = (glancing_dam_red_base) - added_weapon_skill * weapon_skill_reduction
            effective_weapon_damage = random_weapon_damage * (1 - glancing_penalty)
    else:
        effective_weapon_damage =  0

    return effective_weapon_damage



@dataclass
class SimulationResult():
    number_of_attacks : int
    total_damage : list[int]
    fight_duration : float
    average_DPS : float
    weapon_DPS : float

#see this as a template for below 

def do_simulation( weapon_bottom_end , 
                    weapon_top_end ,
                    weapon_speed ,
                    total_hit , 
                    crit_chance ,
                    added_weapon_skill ,
                    fight_duration ,):

    # print(weapon_top_end)
    # print(weapon_bottom_end)
    # print(weapon_speed)


    static_weap_DPS = ((weapon_top_end + weapon_bottom_end) / 2) / weapon_speed
    static_weap_DPS = round(static_weap_DPS)


    num_attacks = float(fight_duration) / float(weapon_speed)
    num_attacks = round(num_attacks)


    attack_damages = []
    #attack iterator
    for i in range(round(num_attacks)):
        damage_result = damage(weapon_top_end, weapon_bottom_end, added_weapon_skill, total_hit, crit_chance)
        attack_damages.append(damage_result)

    average_DPS = sum(attack_damages) / num_attacks

    # damage_distribution = []
    # for i in range(user_iterations.get()):
    #     result = average_DPS*(user_iterations)
    #     damage_distribution.append(result)

    # print(damage_distribution)


    return SimulationResult(num_attacks, attack_damages , fight_duration , 
    average_DPS , static_weap_DPS)

   

