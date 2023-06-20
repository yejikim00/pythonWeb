class Monster:
    def __init__(self, health, attack, speed):
        self.first = health
        self.second = attack
        self.third = speed

goblin = Monster(800, 120, 300)
wolf = Monster(1500, 200, 350)

print(goblin.first)
print(wolf.first)
