from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        team_one: None
        team_two: None

def create_ability(self):
    name = input("What is the ability name?")
    max_damage = input("What is the max_damage of this ability?")
    return Ability(name, max_damage)

def create_weapon(self):
    name = input("What is the weapon name?")
    max_damage = input("What is the max_damage of this weapon?")
    return Weapon(name, max_damage)

def create_armor(self):
    name = input("What is this armor called?")
    max_block = input("What is the max_block of this armor?")
    return Armor(name, max_block)