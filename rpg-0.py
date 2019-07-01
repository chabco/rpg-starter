"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class hero():
    def __init__(self, hero_health, hero_power):
        self.hero_health = hero_health
        self.hero_power = hero_power

    def attack(self, enemy):
        enemy.goblin_health -= self.hero_power
        print("You do %d damage to the goblin." % self.hero_power)
        if enemy.goblin_health <= 0:
            print("The goblin is dead.")

    def alive(self):
        return self.hero_health > 0
            
class goblin():
    def __init__(self, goblin_health, goblin_power):
        self.goblin_health = goblin_health
        self.goblin_power = goblin_power

    def attack(self, hero):
        hero.hero_health -= self.goblin_power
        print("The goblin does %d damage to you." % self.goblin_power)
        if hero.hero_health <= 0:
            print("You are dead.")

    def alive(self):
        return self.goblin_health > 0

def main():
    hero1 = hero(10, 5)
    goblin1 = goblin(6, 2)

    while goblin1.alive() and hero1.alive():
        print("You have %d health and %d power." % (hero1.hero_health, hero1.hero_power))
        print("The goblin has %d health and %d power." % (goblin1.goblin_health, goblin1.goblin_power))
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
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin1.goblin_health > 0:
            # Goblin attacks hero
            goblin1.attack(hero1)

main()