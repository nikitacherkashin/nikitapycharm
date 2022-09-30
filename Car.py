class car
  def __init__(self, consumption: float = 1.0, fuel = 10.0):
        self.consumption = consumption
        self fuel = fuel
        self.traveled = 0

    def __str__(self):
        return f"(consumption:{self.consumption},fuel:{self.fuel}"

    def go (self, distance = 0 )
        if distance < 0 :
            raise Exception ('Расстояние не можеть быть 0')
        counted_consumpion =self.consumption * distanse

        if self.fuel < counted_consumpion:
            raise NotEnoughFuel("нет топлива")
        self.fuel -= counted_consumpion
        self.traveled += distance

