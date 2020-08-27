"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero:
    
    
    def __init__(self, health, power):
        self.health = health
        self.power = power
        

    def attack(self, target):
        target.health -= self.power
        print("You do %d damage to the goblin." % self.power)

    def alive(self):
        self.health > 0
        return self.health

    def status(self):
        print("You have %d health and %d power." % (self.health, self.power))




class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, target):
        target.health -= self.power
        print("You do %d damage to the hero." % self.power)
    
    def alive(self):
        self.health > 0
        return self.health

    def status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))



Codysseus = Hero(10, 5)
Krenko = Goblin(6, 2)



def main():
    

    
    
    
    while Krenko.alive() > 0 and Codysseus.alive() > 0:
        Codysseus.status()
        Krenko.status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            Codysseus.attack(Krenko)
            
            if Krenko.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if Krenko.health > 0:
            # Goblin attacks hero
            Krenko.attack(Codysseus)
            
            if Codysseus.health <= 0:
                print("You are dead.")

main()
