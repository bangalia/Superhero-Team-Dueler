from random import choice

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

    def attack(self):
        print('bolt')

abilities = list()

abilities.append(Hero())
abilities.append(Hero())

for ability in hero_abilities:
    ability.attack()

    def attack(self):
        total_damage = 0
        for ability in self.abilites:
            total_damage += ability.attack()
            return total_damage


    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self):
        defense = 100
        if current_health =str(0):
            return defense = 0 
         else for armor in self.armor:
            defense += armor.defense

    def take_damage(self, damage):
        return self.current_health - (self.defend(damage))    
    
    def fight(self,hero1,hero2):
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

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)

