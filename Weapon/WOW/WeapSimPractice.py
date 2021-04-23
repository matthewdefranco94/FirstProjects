#practice

import sys

sys.path.append ('../../../../../../Desktop/Projects')

import random
import WeaponSimulation
import numpy as np
import random
import matplotlib
import WeaponSimInput

#Attacks have a 40% chance to glance for 30% less damage, weaponskill reduces the 30% damage penatly
#Weapon skill affecting glancing penalty
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

class WeaponInput:
    WeaponStats = {
        "weapon_top_end" : 435,
        "weapon_bottom_end" : 235,
        "weapon_speed" : 3.8,
        # "added_weapon_skill" : 0,
        # "crit_chance" : 40,
        # "total_hit" : 9,
        # "fight_duration" : 120
    }


def main():
    weapon_top_end = float(WeaponInput.WeaponStats["weapon_top_end"])
    weapon_bottom_end = float(WeaponInput.WeaponStats["weapon_bottom_end"])
    weapon_speed = float(WeaponInput.WeaponStats["weapon_speed"])
    added_weapon_skill = int(WeaponInput.WeaponStats["added_weapon_skill"])
    crit_chance = float(WeaponInput.WeaponStats["crit_chance"])
    total_hit = int(WeaponInput.WeaponStats["total_hit"])
    fight_duration = int(WeaponInput.WeaponStats["fight_duration"])

    static_weap_DPS = ((weapon_top_end + weapon_bottom_end) / 2) / weapon_speed
    static_weap_DPS = round(static_weap_DPS)
    total_dmg = []
    num_attacks = float(fight_duration) / float(weapon_speed)
    num_attacks = round(num_attacks)

   #attack iterator
    for i in range(round(num_attacks)):
        damage_result = damage(weapon_top_end, weapon_bottom_end, added_weapon_skill, total_hit, crit_chance)
        total_dmg.append(damage_result)
    print(np.round(total_dmg))
        

    print(f"Your total damage across {num_attacks} attacks is {round(sum(total_dmg))}")
    #Damage per second accounting for other variables
    DPS = float(sum(total_dmg)) / round(fight_duration)
    DPS = round(DPS)
    print("You deal an average of " + str(DPS) + " DPS over a " + str(round(fight_duration / 60)) + " minute long fight.")
    print("Your static weapon DPS is " + str(static_weap_DPS) + ".")
    
    #number of missed attacks
    miss_count = total_dmg.count(0)
    print("Your number of missed attacks is " + str(miss_count) + ".")

main()


# import tkinter as tk
# from tkinter import *

# Simulator = tk.Tk()


# Simulator.title("Fury Simulator")
# Simulator.geometry("900x300")

# instructions = tk.Label(Simulator , text = "This is intended to be a ghetto simulation.\n"
# "Most buffs are held constant.")
# instructions.pack()

# #Create an entry box
# weapon_label = tk.Label(Simulator , text = 'Enter weapon here: ')
# weapon_label.pack()
# weapon_input = tk.Entry(Simulator)
# weapon_input.pack()

# #create listbox
# weapons_list = Listbox(Simulator , width = 50 , height = 5)
# weapons_list.pack()


# #pulls list of weapons user can select
# weapon_query = []
# weapon_query.__getitem__


# duration_label = tk.Label(Simulator , text = 'Number of iterations:')
# duration_label.pack()
# duration_label1 = Spinbox(Simulator , from_ = 60 , to_= 600)
# duration_label1.pack()

# button = tk.Button(Simulator , text = "Begin Simulation" )
# button.pack()

# Simulator.mainloop()

