class Character:
    def __init__(self, name, hp, damage, armor, mega_armor):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.armor = armor
        self.mega_armor = armor
    def __str__(self):
        return f'{self.name} (hp:{self.hp},' \
               f' damage:{self.damage},' \
               f' megarmor: {self.armor})'
               f' armor: {self.armor})'


    def take_damage(self, damage):
        self.hp -= abs(damage)

    def attack(self, target):
       if target.take_damage(self.damage):
            mega_armor + 1

