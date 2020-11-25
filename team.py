from random import choice
class Team:
    def __init__(self,name):
        self.name = name
        self.heroes = list()

    def remove_hero(self,name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            return hero
    
    def add_hero(self,heroes):
        self.hero.append(heroes)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths 
            print("{} Kill/Deaths:{}".format(hero.name,kd))
    
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            self.current_health = 100

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)
        
        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random.choice(living_heroes)
            random.choice(living_opponents)