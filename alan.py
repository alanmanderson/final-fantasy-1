from ff1 import *
from utils import *

party = [red_mage, black_belt, black_mage, fighter]
#global cornelia

armor = coneria.armor + provaka.armor + elf_land.armor + melmond.armor
helmets = [item for item in armor if item.type == 'helmet']
shields = [item for item in armor if item.type == 'shield']
gloves = [item for item in armor if item.type == 'gloves']
chest_armor = [item for item in armor if item.type == 'armor']

party_len = len(party)
print(helmets * party_len)
print(cap.absorb)
print(fighter.armor)
armor = get_ideal_armor(party, helmets)# * party_len)
print(armor)
# armor = get_ideal_armor(party, shields * party_len)
# print(armor)
# armor = get_ideal_armor(party, gloves * party_len)
# print(armor)
# armor = get_ideal_armor(party, chest_armor * party_len)
# print(armor)

