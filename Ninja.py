from character import Character

class Ninja(Character):

    def __init__(self, name, hp, damage, armor):
        Character.__init__(self, name, hp, damage, armor)
    def count_edition_damage(self):
        return (self.max_hp = 100)

    def attack(self, target):
        target.take_damage(self.damage = 10






        """каждый удар добавляет 10% к базовому урону; суммируется до 5 раз (максимальный множитель +50%), после чего множитель обнуляется;"""