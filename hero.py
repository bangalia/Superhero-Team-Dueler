from random import choice

class Hero:
    def __init__(self, name, starting_health=100):

        self.name = name 
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.name = name
    
    def fight(self,hero1,hero2):
        for fight in fight:
            if self.abilities == 0:
                return print("draw")

    
    def add_ability(self, ability):

    # We use the append method to add ability objects to our list.
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
            if current_health = 0:
                return defense = 0 
            else for armor in self.armor:
                defense += armor.defense

    def take_damage(self, damage):
        return self.current_health - self.defend.damage     


if __name__ == "__main__":
    my_hero = Hero("Storm", 150)
    print(my_hero.name)
    print(my_hero.current_health)


if __name__ == "__main__":
    hero1 = Hero("Storm")
    hero2 = Hero("Black Panther")

if _name == "__main__":
    ability = Ability("Lightning Strike", 80)
    another_ability = Ability("Plasma Blast", 75)
    hero = Hero("Storm", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)

