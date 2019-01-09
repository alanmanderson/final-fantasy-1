from primitives.base import Base

class CharClass(Base):
  def __init__(self, name, weapons, armor, spells = []):
    self.name = name
    self.weapons = weapons
    self.armor = armor
    self.spells = spells 
