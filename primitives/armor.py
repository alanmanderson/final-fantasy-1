from primitives.base import Base

class Armor(Base):
  def __init__(self, name, type, cost, absorb, evade, resistance = []):
    self.name = name
    self.type = type
    self.cost = cost
    self.absorb = absorb
    self.evade = evade
    self.resistance = resistance

