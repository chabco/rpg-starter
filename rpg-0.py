"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
import random

class character():
    def __init__(self, name, health, power, power2, heal, back, elem):
        self.name = name
        self.health = health
        self.power = power
        self.power2 = power2
        self.heal = heal
        self.back = back
        self.elem = elem

    def attack(self, enemy):
        enemy.health -= self.power
        print('{} does {} to {}.'.format(self.name, self.power, enemy.name))

    def attack2(self, enemy):
        enemy.health -= self.power2
        print('critical strike! {} does {} to {}.'.format(self.name, self.power2, enemy.name))

    def regenerate(self):
        self.health += self.heal
        print('{} healed for {} health points.'.format(self.name, self.heal))
    
    def thorns(self, enemy):
        enemy.health -= self.back
        print('{} returns damage to {} for {} points'.format(self.name, enemy.name, self.back))

    def elemental(self, enemy):
        enemy.health -= self.elem
        print('{} unleashes the power of thoros on {} for {} points.'.format(self.name, enemy.name, self.elem))

    def print_status(self):
        print('{} has {} health, {} power and {} elemental power.'.format(self.name, self.health, self.power, self.elem))

    def alive(self):
        return self.health > 0
        
def main():
    hero1 = character('hero', 20, 5, 10, 0, 0, 0)
    goblin1 = character('goblin', 14, 4, 6, 0, 0, 0)
    medic = character('medic', 12, 2, 4, 2, 0, 0)
    shadow = character('shadow', 1, 7, 14, 0, 0, 0)
    zombie = character('zombie', 0, 5, 5, 0, 0, 0)
    thornmail = character('thornmail', 50, 1, 2, 0 , 2, 0)
    mage = character('mage', 10, 0, 0, 0, 0, 20)
    shadow_attacked = 0

    while goblin1.alive() and hero1.alive() and medic.alive() and shadow.alive() and thornmail.alive():
        goblin1.print_status()
        hero1.print_status()
        medic.print_status()
        shadow.print_status()
        zombie.print_status()
        thornmail.print_status()
        mage.print_status()
        print()
        print("what do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            if random.random() <= 0.2:
                hero1.attack2(goblin1)
            elif random.random() <= 0.1:
                mage.elem(goblin1)
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
            # goblin attacks hero, medic, shadow, zombie, or thornmail
            if random.random() < 0.14:
                goblin1.attack(hero1)

            elif random.random() < 0.14:
                goblin1.attack(medic)

                if medic.alive():
                    # medic heals at 20% chance
                    if random.random() < 0.2:
                        medic.regenerate()

            elif random.random() < .14:
                shadow_attacked += 1
                print('goblin attempts to attack shadow!')
                if shadow_attacked >= 10:
                    goblin1.attack(shadow)
                    print('goblin finally hit the shadow! game over.')

            elif random.random() < .14:
                goblin1.attack(zombie)
                print('zombie takes damage but remains in battle!')

            elif random.random() < .14:
                goblin1.attack(thornmail)
                thornmail.thorns(goblin1)
            
            elif random.random() < .14:
                goblin1.attack(mage)



        if not hero1.alive() and medic.alive() and shadow.alive() and thornmail.alive() and mage.alive():
            print('game over.')

main()