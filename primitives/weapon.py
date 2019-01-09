class Weapon:
  def __init__(self, name, cost, damage, hit_perc, crit_perc, spells = []):
    self.name = name
    self.cost = cost
    self.damage = damage
    self.hit_perc = hit_perc
    self.crit_perc = crit_perc
    self.spells = spells

