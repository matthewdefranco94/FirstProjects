#Attempts to compare different weapon's damage over a period of time

import random
import numpy as np
from collections import Counter


class Weapon:
    weapon_speed = float(input("Input your weapon's speed: "))
    weapon_top_end = float(input("Weapon's top end damage: "))
    weapon_bottom_end = float(input("Weapon's bototm ened damage: "))
    weapon_skill = int(input("Do you have added weapon skill, if so, how much? "))
    total_hit = float(input("How much weapon hit do you have? "))

random_weapon_damage = random.randint(weapon_bottom_end , weapon_top_end)


class Attack:
    def attack(self, miss_chance , glancing_chance , non_glancing_chance):
        random_weapon_damage = random.randint(weapon_bottom_end , weapon_top_end)
        attack = (input("Did you attack your target? "))
        random_weapon_damage = random.randint(weapon_bottom_end , weapon_top_end)
        random_attack_value = random.randint(0,100,1)
        missed_attack = float(16)
        chance_glance = float(40)
        missed_attack_penalty = 0
        glanced_attack_penatly = random_weapon_damage * 0.35
        non_glancing_hit = 1 - (miss_chance + glancing_chance)