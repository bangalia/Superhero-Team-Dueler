import random

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
        # TODO: Create instance variables for the values passed in.
    
    def block(self):
        random_value = random.randint(0,self.max_block)
        return random_value

        random.randint(2,20)
    
    def attack(self):
        random_value = random.randint(0,self.max_block)
        return random_value

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())

