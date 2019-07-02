"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
import random

class character():
    def __init__(self, name, health, power, power2):
        self.name = name
        self.health = health
        self.power = power
        self.power2 = power2

    def attack(self, enemy):
        enemy.health -= self.power
        print('{} does {} to {}.'.format(self.name, self.power, enemy.name))

    def attack2(self, enemy):
        enemy.health -=self.power2
        print('critical strike! {} does {} to {}.'.format(self.name, self.power2, enemy.name))

    def print_status(self):
        print('{} has {} health and {} power.'.format(self.name, self.health, self.power))

    def alive(self):
        return self.health > 0
        
def main():
    hero1 = character('hero', 10, 5, 10)
    goblin1 = character('goblin', 6, 2, 2)

    while goblin1.alive() and hero1.alive():
        goblin1.print_status()
        hero1.print_status()
        print()
        print("what do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            if random.random() < 0.2:
                hero1.attack2(goblin1)
            else:
                hero1.attack(goblin1)
            if not goblin1.alive():
                print('you have slayed the goblin!')
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("goodbye.")
            break
        else:
            print("invalid input %r" % user_input)

        if goblin1.alive():
            # Goblin attacks hero
            goblin1.attack(hero1)
            if not hero1.alive():
                print('YOU DIED.')

                

main()