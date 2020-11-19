class Hero:
    def __init__(self, name, starting_health=100):

        self.name = name 
        self.starting_health = starting_health
        self.current_health = starting_health


if __name__ == "__main__":
    my_hero = Hero("Storm", 150)
    print(my_hero.name)
    print(my_hero.current_health)

from random import choice

def fight(self,opponent):
    return choice(self,opponent)

if __name__ == "__main__":
    hero1 = Hero("Storm")
    hero2 = Hero("Black Panther")
