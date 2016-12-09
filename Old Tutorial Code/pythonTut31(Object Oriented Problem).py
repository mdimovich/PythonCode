import random
import math

# Warriors will have names, health, and attack and block maximums
# They will have the capabilities to attack and block random amounts

# Attack random() (0.0 to 1.0 + 0.5) * maxAttack
# Block will use random
# Battle class capability of looping until 1 warrior dies
# Warriors will each get a turn to atk each other

# Function gets 2 warriors, 1 warrior attacks the other
# Attacks and blocks are integers


class Warrior:
    def __init__(self, name="Warrior", health=0, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max

    def attack(self):
        attack_amount = self.attack_max * (random.random() + 0.5)
        return attack_amount

    def block(self):
        block_amount = self.block_max * random.random()
        return block_amount

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over!")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over!")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warrior_A_AttackAmount = warriorA.attack()
        warrior_B_BlockAmount = warriorB.block()

        warriorBDamage = math.ceil(warrior_A_AttackAmount - warrior_B_BlockAmount)

        warriorB.health = warriorB.health - warriorBDamage

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, warriorBDamage))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    spartacus = Warrior("Spartacus", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, spartacus)

main()
