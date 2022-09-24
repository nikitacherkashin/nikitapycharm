from character import Character

class Nikotron(Character):

    def __init__(self, name, hp, damage, armor):
       Character.__init__(self, name, hp, damage, armor)
              ef count_edition_heal(self):
            return(self.max_hp + self.hp) / self.max_hp * self.damage

            def attack(self, target):
                 target.take_heal(self.heal + self.count_edition_heal())