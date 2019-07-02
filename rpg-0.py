"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print('{} does {} to {}.'.format(self.name, self.power, enemy.name))

    def print_status(self):
        print('{} has {} health and {} power.'.format(self.name, self.health, self.power))

    def alive(self):
        return self.health > 0

class hero(character):
    def __init__(self, hero_health, hero_power):
        super().__init__(health, power, alive, print_status)

            
class goblin(character):
    def __init__(self, goblin_health, goblin_power):
        super().__init__(health, power, alive, print_status)


def main():
    hero1 = character('hero', 10, 5)
    goblin1 = character('goblin', 6, 2)

    while goblin1.alive() and hero1.alive():
        goblin1.print_status()
        hero1.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero1.attack(goblin1)
            if not goblin1.alive():
                print('You have slayed the goblin!')
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin1.alive():
            # Goblin attacks hero
            goblin1.attack(hero1)
            if not hero1.alive():
                print('YOU DIED.')

                

main()