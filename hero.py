import random  
from ability import Ability 
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):

        self.name = name 
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.name = name
    
      
    def add_ability(self, ability):
        self.abilities.append(ability)

#abilities = list()

#abilities.append(Hero())
#abilities.append(Hero())

#for ability in hero_abilities:
    #ability.attack()

    def add_armor(self, armor):
        self.armor.append(armor)
    
    def add_weapon(self,weapon):
        self.weapon.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilites:
            total_damage += ability.attack()
            return int(total_damage)

    def defend(self):
        defense = 0
        for armor in self.armor:
            defense += armor.defense()
        return defense

    def take_damage(self, damage):
        return self.current_health - (damage+self.defend(damage))    
    
    def fight(self,opponent):
        if len(self.abilities)==0 or len(self.abilities)==0:
            while(self.is_alive() and opponent.is_alive()):
                print(f"{self.name} has attacked {opponent.name}")
                opponent.take_damage(self.attack())
                print(f"{opponent.name}'s remaining health is {opponent.current_health}")
                print(f"{opponent.name} has attacked {self.name}")
                self.take_damage(opponent.attack())
                print(f"{self.name}'s remaining health is {self.current_health}")
            
    
            if not self.is_alive():
                print(f"{opponent.name} won!")
            elif not opponent.is_alive():
                print(f"{self.name} won!")
        else:
            print("Draw!")


    def is_alive(self):
        if self.current_health <= 0:
            return False 
        else:
            return True
    
    def __init__(self,name,health=100):
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        self.kills += num_kills
    
    def add_death(self, num_deaths):
        self.deaths += num_deaths

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

