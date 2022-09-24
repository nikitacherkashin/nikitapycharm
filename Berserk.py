from character import Character

class Berserk(Character):

    def __init__(self, name, hp, damage, armor):
        Character.__init__(self, name, hp, damage, armor)
    def count_edition_damage(self):
        return(self.max_hp - self.hp) / self.max_hp * self.damage

    def attack(self, target):
        target.take_damage(self.damage + self.count_edition_damage())