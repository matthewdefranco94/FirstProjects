
import random
import WeaponSimulation
import numpy as np
import random
import matplotlib

def damage(weapon_top_end, weapon_bottom_end, added_weapon_skill, total_hit , crit_chance):
    glancing_chance_eff = 0.40
    glancing_dam_red_base = 0.30
    weapon_skill_reduction = 0.03
    base_miss = 0.28
    critical_strike_modifier = 1.5
    
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
