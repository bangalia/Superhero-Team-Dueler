from random import choice

class Hero:
    def __init__(self, name, starting_health=100):

        self.name = name 
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.name = name
    
    def fight(self,opponent):
    
    self.name
    return choice(hero1,hero2)


    def add_ability(self, ability):
    ''' Add ability to abilities list '''

    # We use the append method to add ability objects to our list.
    self.abilities.append(ability)



if __name__ == "__main__":
    my_hero = Hero("Storm", 150)
    print(my_hero.name)
    print(my_hero.current_health)


if __name__ == "__main__":
    hero1 = Hero("Storm")
    hero2 = Hero("Black Panther")
