def get_armor(party, town):
  armor_in_common = {}
  for char in party:
    for armor in town.armor:
      if armor in char.armor:
        if armor not in armor_in_common:
          armor_in_common[armor] = []
        armor_in_common[armor].append(char)
  return armor_in_common

def get_ideal_armor(party, armor):
  if len(party) == 0: return {}
  party_copy = party.copy()
  cur_char = party_copy.pop(0)
  best_item = None
  best_rest = get_ideal_armor(party_copy, armor.copy())
  best_absorb = get_total_absorb(best_rest)
  for i in range(len(armor)):
    if armor[i] in cur_char.armor:
      cur_armor = armor.copy()
      del cur_armor[i]
      rest = get_ideal_armor(party_copy, cur_armor)
      cur_absorb = get_total_absorb(rest) + armor[i].absorb
      if cur_absorb > best_absorb:
        best_absorb = cur_absorb
        best_item = armor[i]
        best_rest = rest
  best_rest[cur_char.name] = best_item
  return best_rest
  
def get_total_absorb(armor):
  total = 0
  for char, item in armor.items():
    if item is not None:
      total += item.absorb
  return total

def get_weapons_stats(weapons):
  stats = {'damage': 0, 'hit_perc': 0, 'crit_perc': 0, 'cost':  0, 'spells': []}
  for item in weapons:
    stats['damage'] += item.damage
    stats['hit_perc'] += item.hit_perc
    stats['crit_perc'] += item.crit_perc
    stats['cost'] += item.cost
    stats['spells'].extend(item.spells)
  return stats

def get_armor_stats(armor):
  stats = {'absorb': 0, 'evade': 0, 'cost': 0, 'resistance': []}
  for item in armor:
    stats['absorb'] += item.absorb
    stats['evade'] += item.evade
    stats['cost'] += item.cost
    stats['resistance'].extend(item.resistance)
  return stats
