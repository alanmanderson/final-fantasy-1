import unittest
import utils
from primitives.armor import Armor
from primitives.weapon import Weapon
from primitives.charclass import CharClass

class TestUtils(unittest.TestCase):
  def test_get_armor_stats(self):
    cloth = Armor('cloth', 'armor', 10, 1, 2, ['lightning'])
    wooden_armor = Armor('wooden_armor', 'armor', 50, 4, 8, ['fire'])
    stats = utils.get_armor_stats([cloth, wooden_armor])
    self.assertDictEqual(stats, {'absorb': 5, 'cost': 60, 'evade': 10, 'resistance': ['lightning', 'fire']})

  def test_get_weapons_stats(self):
    sword = Weapon('sword', 45, 50, .01, .5, ['fire'])
    dagger = Weapon('dagger', 12, 13, .1, .3, ['lightning'])
    stats = utils.get_weapons_stats([sword, dagger])
    self.assertDictEqual(stats, {'cost': 57, 'damage': 63, 'hit_perc': .11, 'crit_perc': .8, 'spells': ['fire', 'lightning']})

  def test_get_ideal_armor_empty_armor(self):
    party = []
    armor = []
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {})

  def test_get_ideal_armor_empty_party(self):
    party = []
    armor = []
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {})

  def test_get_ideal_armor(self):
    chain_armor = Armor('chain armor', 'armor', 10, 100, 0)
    paper_armor = Armor('paper armor', 'armor', 10, 1, 0)
    wooden_armor = Armor('wooden armor', 'armor', 10, 50, 0)
    alice = CharClass('alice', [], [chain_armor])
    bob = CharClass('bob', [], [chain_armor, paper_armor, wooden_armor])
    party = [alice, bob]
    armor = [chain_armor, paper_armor, wooden_armor]
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {'alice': chain_armor, 'bob': wooden_armor})

  def test_get_ideal_armor_with_negative(self):
    armor = [Armor('nails', 'helmet', 10, -5, 0)]
    party = [CharClass('nailman', [], armor)]
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {'nailman': None})

  def test_get_ideal_armor_with_multiples_alternate_order(self):
    armor = [
      Armor('cap', 'helmet', 1, 1, 0),
      Armor('iron helmet', 'helmet', 10, 10, 0) 
    ] * 4 
    party = [CharClass('nailman', [], armor)]
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {'nailman': armor[1]})

  def test_get_ideal_armor_with_multiples(self):
    armor = [Armor('cap', 'helmet', 1, 1, 0)] * 4
    armor.append(Armor('iron helmet', 'helmet', 10, 10, 0))
    party = [CharClass('nailman', [], armor)]
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {'nailman': armor[4]})

  def test_get_ideal_armor_with_large_arrays(self):
    armor = [
      Armor('nails', 'armor', 10, -5, 0),
      Armor('paper_armor', 'armor', 10, 1, 0),
      Armor('chain_armor', 'armor', 10, 100, 0),
      Armor('steel_armor', 'armor', 10, 101, 0),
      Armor('fire_armor', 'armor', 10,95, 0),
      Armor('ice_armor', 'armor', 10, 95, 0)
    ]
    party = [
      CharClass('mage', [], [armor[i] for i in [1,2,3]]),
      CharClass('fighter', [], [armor[i] for i in [0]]),
      CharClass('red mage', [], [armor[i] for i in [1,4]]),
      CharClass('black belt', [], [armor[i] for i in [5]])
    ]
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {'mage': armor[3], 'fighter': None, 'red mage': armor[4], 'black belt': armor[5]})

  def test_regression_fail_to_assign_wooden(self):
    armor = [
      Armor('cap', 'helmet', 10, 1, 0),
      Armor('wooden_helmet', 'helmet', 10, 5, 0),
      Armor('iron_helmet', 'helmet', 10, 10, 0),
    ] * 4
    party = [
      CharClass('mage', [], [armor[i] for i in [0]]),
      CharClass('red mage', [], [armor[i] for i in [0]]),
      CharClass('fighter', [], [armor[i] for i in [0, 1, 2]]),
      CharClass('black belt', [], [armor[i] for i in [0]])
    ]
    ideal_armor = utils.get_ideal_armor(party, armor)
    self.assertDictEqual(ideal_armor, {'mage': armor[0], 'fighter': armor[2], 'red mage': armor[0], 'black belt': armor[0]})

if __name__ == '__main__':
  unittest.main()
