from primitives.town import Town
from primitives.weapon import Weapon
from primitives.charclass import CharClass
from primitives.armor import Armor
from primitives.spell import Spell
from primitives.item import Item

global fire
global lit 
global lock
global slep
global dark
global ice 
global slow
global tmpr
global hold
global lit2
global fir2
global lok2
global fast
global ice2
global conf
global slp2
global fir3
global bane
global slo2
global warp
global lit3
global qake
global rub 
global stun
global blnd
global brak
global ice3
global sabr
global zap 
global xxxx
global nuke
global stop
 
global cure
global fog 
global harm
global ruse
global invs
global lamp
global alit
global mute
global cur2
global hrm2
global heal
global afir
global pure
global fear
global aice
global amut
global cur3
global hrm3
global hel2
global life
global inv2
global fog2
global soft
global exit
global cur4
global hrm4
global hel3
global arub
global xfer
global fade
global lif2
global wall

fire = Spell('fire', 100)
lit = Spell('lit', 100)
lock = Spell('lock', 100)
slep = Spell('slep', 100)
dark = Spell('dark', 400)
ice = Spell('ice', 400)
slow = Spell('slow', 400)
tmpr = Spell('tmpr', 400)
hold = Spell('hold', 1500)
lit2 = Spell('lit2', 1500)
fir2 = Spell('fir2', 1500)
lok2 = Spell('lok2', 1500)
fast = Spell('fast', 4000)
ice2 = Spell('ice2', 4000)
conf = Spell('conf', 4000)
slp2 = Spell('slp2', 4000)
fir3 = Spell('fir3', 8000)
bane = Spell('bane', 8000)
slo2 = Spell('slo2', 8000)
warp = Spell('warp', 8000)
lit3 = Spell('lit3', 20000)
qake = Spell('qake', 20000)
rub = Spell('rub', 20000)
stun = Spell('stun', 20000)
blnd = Spell('blnd', 45000)
brak = Spell('brak', 45000)
ice3 = Spell('ice3', 45000)
sabr = Spell('sabr', 45000)
zap = Spell('zap', 60000)
xxxx = Spell('xxxx', 60000)
nuke = Spell('nuke', 60000)
stop = Spell('stop', 60000)

cure = Spell('cure', 100)
fog = Spell('fog', 100)
harm = Spell('harm', 100)
ruse = Spell('ruse', 100)
invs = Spell('invs', 400)
lamp = Spell('lamp', 400)
alit = Spell('alit', 400)
mute = Spell('mute', 400)
cur2 = Spell('cur2', 1500)
hrm2 = Spell('hrm2', 1500)
heal = Spell('heal', 1500)
afir = Spell('afir', 1500)
pure = Spell('pure', 4000)
fear = Spell('fear', 4000)
aice = Spell('aice', 4000)
amut = Spell('amut', 4000)
cur3 = Spell('cur3', 8000)
hrm3 = Spell('hrm3', 8000)
hel2 = Spell('hel2', 8000)
life = Spell('life', 8000)
inv2 = Spell('inv2', 20000)
fog2 = Spell('fog2', 20000)
soft = Spell('soft', 20000)
exit = Spell('exit', 20000)
cur4 = Spell('cur4', 45000)
hrm4 = Spell('hrm4', 45000)
hel3 = Spell('hel3', 45000)
arub = Spell('arub', 45000)
xfer = Spell('xfer', 60000)
fade = Spell('fade', 60000)
lif2 = Spell('lif2', 60000)
wall = Spell('wall', 60000)

global wooden_nun
global small_dagger
global wooden_staff
global rapier
global iron_hammer
global short_sword
global hand_axe
global scimtar
global iron_nun
global large_dagger
global iron_staff
global sabre
global long_sword
global great_axe
global falchon
global silver_dagger
global silver_sword
global silver_hammer
global silver_axe
global flame_sword
global ice_sword
global dragon_sword
global giant_sword
global sun_sword
global coral_sword
global were_sword
global rune_sword
global power_staff
global light_axe
global heal_staff
global mage_staff
global defense
global wizard_staff
global vorpal
global cat_claw
global thor_hammer
global bane_sword
global katana
global xcalber
global masmune

wooden_nun = Weapon('wooden nunchuck', 10, 12, 0, .01)
small_dagger = Weapon('small dagger', 5, 5, 10, .015)
wooden_staff = Weapon('wooden staff', 5, 6, 0, .02)
rapier = Weapon('rapier', 10, 9, 5, .025)
iron_hammer = Weapon('iron hammer', 10, 9, 0, .03)
short_sword = Weapon('short sword', 550, 15, 10, .035)
hand_axe = Weapon('hand axe', 550, 16, 5, .04)
scimtar = Weapon('scimtar', 200, 10, 10, .045)
iron_nun = Weapon('iron nun', 200, 16, 0, .05)
large_dagger = Weapon('large dagger', 175, 7, 10, .055)
iron_staff = Weapon('iron staff', 200, 14, 0, .06)
sabre = Weapon('sabre', 450, 13, 5, .065)
long_sword = Weapon('long sword', 1500, 20, 10, .07)
great_axe = Weapon('great axe', 2000, 22, 5, .075)
falchon = Weapon('falchon', 450, 15, 10, .08)
silver_dagger = Weapon('silver dagger', 800, 10, 15, .085)
silver_sword = Weapon('silver sword', 4000, 23, 15, .09)
silver_hammer = Weapon('silver hammer', 2500, 12, 5, .095)
silver_axe = Weapon('silver axe', 4500, 25, 10, .1)
flame_sword = Weapon('flame sword', 10000, 26, 20, .104)
ice_sword = Weapon('ice sword', 15000, 29, 25, .109)
dragon_sword = Weapon('dragon sword', 8000, 19, 15, .114)
giant_sword = Weapon('giant sword', 8000, 21, 20, .119)
sun_sword = Weapon('sun sword', 20000, 32, 30, .124)
coral_sword = Weapon('coral sword', 8000, 19, 15, .129)
were_sword = Weapon('were sword', 6000, 18, 15, .134)
rune_sword = Weapon('rune sword', 5000, 18, 15, .139)
power_staff = Weapon('power staff', 12344, 12, 0, .144)
light_axe = Weapon('light axe', 10000, 28, 15, .149, ['hrm2'])
heal_staff = Weapon('heal staff', 25000, 6, 0, .154, ['heal'])
mage_staff = Weapon('mage staff', 30000, 12, 10, .159, ['fir2'])
defense = Weapon('defense', 40000, 30, 35, .164, ['ruse'])
wizard_staff = Weapon('wizard staff', 50000, 15, 15, .169, ['conf'])
vorpal = Weapon('vorpal', 30000, 24, 25, .174)
cat_claw = Weapon('cat claw', 65000, 22, 35, .179)
thor_hammer = Weapon('thor hammer', 40000, 18, 15, .184, ['lit2'])
bane_sword = Weapon('bane sword', 60000, 22, 20, .189, ['bane'])
katana = Weapon('katana', 60000, 33, 35, .194)
xcalber = Weapon('xcalber', 60000, 45, 35, .199)
masmune = Weapon('masmune', 60000, 56, 50, .204)


global chain_armor
global cloth
global wooden_armor
global iron_armor
global steel_armor
global silver_armor
global flame_armor
global ice_armor
global opal_armor
global dragon_armor
global copper_bracelet
global silver_bracelet
global gold_bracelet
global opal_bracelet
global white_robe
global black_robe
global wooden_shield
global iron_shield
global silver_shield
global flame_shield
global ice_shield
global opal_shield
global aegis_shield
global buckler
global pro_cape
global cap
global wooden_helmet
global iron_helmet
global silver_helmet
global opal_helmet
global heal_helmet
global ribbon
global gloves
global copper_gloves
global iron_gloves
global silver_gloves
global zeus_gloves
global power_gloves
global opal_gloves
global pro_ring

chain_armor = Armor('chain_armor', 'armor', 80, 15, 15)
cloth = Armor('cloth', 'armor', 10, 1, 2)
wooden_armor = Armor('wooden armor', 'armor', 50, 4, 8)
iron_armor = Armor('iron armor', 'armor', 800, 24, 23)
steel_armor = Armor('steel armor', 'armor', 45000, 34, 33)
silver_armor = Armor('silver armor', 'armor', 7500, 18, 8)
flame_armor = Armor('flame armor', 'armor', 30000, 34, 10, ['cold'])
ice_armor = Armor('ice armor', 'armor', 30000, 34, 10, ['fire'])
opal_armor = Armor('opal armor', 'armor', 60000, 42, 10, ['lightning'])
dragon_armor = Armor('dragon armor', 'armor', 60000, 42, 10, ['cold', 'fire', 'lightning'])
copper_bracelet = Armor('copper bracelet', 'armor', 1000, 4, 1)
silver_bracelet = Armor('silver bracelet', 'armor', 10000, 15, 1)
gold_bracelet = Armor('gold bracelet', 'armor', 10000, 24, 1)
opal_bracelet = Armor('opal bracelet', 'armor', 65000, 31, 1)
white_robe = Armor('white robe', 'armor', 2, 24, 2, ['death', 'fire'])
black_robe = Armor('black robe', 'armor', 2, 24, 2, ['cold', 'time'])
wooden_shield = Armor('wooden shield', 'shield', 15, 2, 0)
iron_shield = Armor('iron shield', 'shield', 100, 4, 0)
silver_shield = Armor('silver shield', 'shield', 2500, 8, 0)
flame_shield = Armor('flame shield', 'shield', 10000, 12, 0, ['cold'])
ice_shield = Armor('ice shield', 'shield', 10000, 12, 0, ['fire'])
opal_shield = Armor('opal shield', 'shield', 15000, 16, 0, ['ligtning'])
aegis_shield = Armor('aegis shield', 'shield', 40000, 16, 0, ['poison'])
buckler = Armor('buckler', 'shield', 2500, 2, 0)
pro_cape = Armor('pro cape', 'shield', 2000, 8, 2)
cap = Armor('cap', 'helmet', 80, 1, 1)
wooden_helmet = Armor('wooden helmet', 'helmet', 100, 3, 3)
iron_helmet = Armor('iron helmet', 'helmet', 450, 5, 5)
silver_helmet = Armor('silver helmet', 'helmet', 2500, 6, 3)
opal_helmet = Armor('opal helmet', 'helmet', 10000, 8, 3)
heal_helmet = Armor('heal helmet', 'helmet', 20000, 6, 3)
ribbon = Armor('ribbon', 'helmet', 2, 1, 1, ['cold', 'death', 'earth', 'fire', 'lightning', 'poison', 'status', 'time'])
gloves = Armor('gloves', 'gloves', 60, 1, 1)
copper_gloves = Armor('copper gloves', 'gloves', 200, 2, 3)
iron_gloves = Armor('iron gloves', 'gloves', 750, 4, 5)
silver_gloves = Armor('silver gloves', 'gloves', 5000, 6, 3)
zeus_gloves = Armor('zeus gloves', 'gloves', 15000, 6, 3)
power_gloves = Armor('power gloves', 'gloves', 10000, 6, 3)
opal_gloves = Armor('opal gloves', 'gloves', 20000, 8, 3)
pro_ring = Armor('pro ring', 'gloves', 20000, 8, 1, ['death'])

global heal_potion
global pure_potion
global tent
global soft_potion
global tent
global cabin
global house
global lute
global crown
global key
global rod
global floater
global cube
global oxyale
global chime
global tnt
global herb
global crystal
global ruby
global bottle
global tail
global slab
global adamant

heal_potion = Item('heal', 60)
pure_potion = Item('pure', 75)
tent = Item('tent', 75)
soft_potion = Item('soft_potion', 800)
cabin = Item('cabin', 250)
house = Item('house', 3000)
lute = Item('lute', 0)
crown = Item('crown', 0)
key = Item('key', 0)
rod = Item('rod', 0)
floater = Item('floater', 0)
cube = Item('cube', 0)
oxyale = Item('oxyale', 0)
chime = Item('chime', 0)
tnt = Item('tnt', 0)
herb = Item('herb', 0)
crystal = Item('crystal', 0)
ruby = Item('ruby', 0)
bottle = Item('bottle', 50000)
tail = Item('tail', 0)
slab = Item('slab', 0)
adamant = Item('adamant', 0)

global fighter
global thief
global black_belt
global red_mage
global white_mage
global black_mage
global knight
global ninja
global master
global red_wizard
global white_wizard
global black_wizard

fighter = CharClass(
  'fighter',
  [
    small_dagger, wooden_staff, rapier, iron_hammer, short_sword, hand_axe, scimtar, large_dagger, 
    iron_staff, sabre, long_sword, great_axe, falchon, silver_dagger, silver_sword, silver_hammer, 
    silver_axe, flame_sword, ice_sword, dragon_sword, giant_sword, sun_sword, coral_sword, were_sword,
    rune_sword, power_staff, light_axe, masmune
  ],
  [
    cloth, wooden_armor, chain_armor, iron_armor, steel_armor, silver_armor, flame_armor, ice_armor, 
    copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, wooden_shield, iron_shield, 
    silver_shield, flame_shield, ice_shield, buckler, pro_cape, cap, wooden_helmet, iron_helmet,
    silver_helmet, ribbon, gloves, copper_gloves, iron_gloves, silver_gloves, power_gloves, pro_ring
  ],
  [])
thief = CharClass(
  'thief',
  [
    small_dagger, rapier, scimtar, large_dagger, sabre, falchon, silver_dagger, dragon_sword, coral_sword, 
    rune_sword, masmune
  ],
  [
    cloth, wooden_armor, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, buckler, pro_cape,
    cap, ribbon, gloves, pro_ring
  ],
  [])
black_belt = CharClass(
  'black_belt',
  [
    wooden_nun, wooden_staff, iron_nun, iron_staff, power_staff, masmune
  ],
  [
    cloth, wooden_armor, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, cap, ribbon, gloves,
    pro_ring
  ],
  [])
red_mage = CharClass(
  'red mage',
  [
    small_dagger, wooden_staff, rapier, short_sword, scimtar, large_dagger, sabre, long_sword, falchon,
    silver_dagger, silver_sword, flame_sword, ice_sword, dragon_sword, giant_sword, sun_sword,
    coral_sword, were_sword, rune_sword, masmune
  ],
  [
    cloth, chain_armor, wooden_armor, silver_armor, copper_bracelet, silver_bracelet, gold_bracelet,
    opal_bracelet, buckler, pro_cape, cap, ribbon, gloves, pro_ring
  ],
  [
    lit, fire, lock, slep, dark, ice, slow, tmpr, hold, lit2, fir2, lok2, fast, ice2, conf, slp2, 
    fire, slo2, cure, fog, invs, lamp, alit, mute, cur2, afir, pure, aice, cur3
  ])
white_mage = CharClass(
  'white mage',
  [
    wooden_staff, iron_hammer, silver_hammer, power_staff, heal_staff, masmune
  ],
  [
    cloth, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, pro_cape, cap, ribbon, gloves, 
    pro_ring
  ],
  [
    ruse, cure, harm, fog, invs, lamp, alit, mute, cur2, hrm2, heal, afir, pure, fear, aice, amut, cur3, 
    hrm3, hel2, life, inv2, fog2, soft, hel3, arub
  ])
black_mage = CharClass(
  'black mage',
  [
    small_dagger, wooden_staff, large_dagger, silver_dagger, power_staff, mage_staff, masmune
  ],
  [
    cloth, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, pro_cape, cap, ribbon, 
    gloves, pro_ring
  ],
  [
    lit, fire, lock, slep, dark, ice, slow, tmpr, hold, lit2, fir2, lok2, fast, ice2, conf, slp2, 
    fir3, bane, slo2, lit3, qake, rub, stun, blnd,ice3
  ])
knight = CharClass(
  'knight',
  [
    small_dagger, wooden_staff, rapier, iron_hammer, short_sword, hand_axe, scimtar, large_dagger,
    iron_staff, sabre, long_sword, great_axe, falchon, silver_dagger, silver_sword, silver_hammer, 
    silver_axe, flame_sword, ice_sword, dragon_sword, giant_sword, sun_sword, coral_sword, were_sword,
    rune_sword, power_staff, light_axe, defense, vorpal, cat_claw, thor_hammer, bane_sword, xcalber,
    masmune
  ],
  [
    cloth, wooden_armor, chain_armor, iron_armor, steel_armor, silver_armor, flame_armor, ice_armor,
    opal_armor, dragon_armor, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet,
    wooden_shield, iron_shield, silver_shield, flame_shield, ice_shield, opal_shield, aegis_shield, 
    buckler, pro_cape, cap, wooden_helmet, iron_helmet, silver_helmet, opal_helmet, heal_helmet, 
    ribbon, gloves, copper_gloves, iron_gloves, silver_gloves, zeus_gloves, power_gloves, opal_gloves,
    pro_ring
  ],
  [
    ruse, cure, fog, invs, lamp, alit, mute, cur2, afir
  ])
ninja = CharClass(
  'ninja',
  [
    wooden_nun, small_dagger, wooden_staff, rapier, iron_hammer, short_sword, hand_axe, scimtar, 
    iron_nun, large_dagger, iron_staff, sabre, long_sword, great_axe, falchon, silver_dagger, 
    silver_sword, silver_hammer, silver_axe, flame_sword, ice_sword, dragon_sword, giant_sword, 
    sun_sword, coral_sword, were_sword, rune_sword, power_staff, light_axe, heal_staff, mage_staff,
    defense, vorpal, cat_claw, thor_hammer, bane_sword, katana, masmune
  ],
  [
    cloth, wooden_armor, chain_armor, iron_armor, silver_armor, flame_armor, ice_armor, copper_bracelet,
    silver_bracelet, gold_bracelet, opal_bracelet, wooden_shield, iron_shield, silver_shield, flame_shield,
    ice_shield, buckler, pro_cape, cap, wooden_helmet, iron_helmet, silver_helmet, heal_helmet, ribbon, 
    gloves, copper_gloves, iron_gloves, silver_gloves, zeus_gloves, power_gloves, pro_ring
  ],
  [
    lit, fire, lock, slep, dark, ice, slow, tmpr, hold, lit2, fir2, lok2, fast, ice2, conf, slow
  ])
master = CharClass(
  'master',
  [
    wooden_nun, wooden_staff, iron_nun, iron_staff, power_staff, masmune
  ],
  [
    cloth, wooden_armor, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, 
    cap, ribbon, gloves, pro_ring
  ],
  [])
red_wizard = CharClass(
  'red wizard',
  [
    small_dagger, wooden_staff, rapier, short_sword, scimtar, large_dagger, sabre, long_sword, 
    falchon, silver_dagger, silver_sword, flame_sword, ice_sword, dragon_sword, giant_sword,
    sun_sword, coral_sword, were_sword, rune_sword, defense, vorpal, cat_claw, bane_sword, masmune
  ],
  [
    cloth, wooden_armor, chain_armor, silver_armor, copper_bracelet, silver_bracelet, gold_bracelet, 
    opal_bracelet, buckler, pro_cape, cap, ribbon, gloves, silver_gloves, zeus_gloves, power_gloves, 
    pro_ring
  ],
  [
    lit, fire, lock, slep, dark, ice, slow, tmpr, hold, lit2, fir2, lok2, fast, ice2, conf, slp2, 
    fir3, bane, slo2, warp, lit3, ice3, ruse, cure, fog, invs, lamp, alit, mute, cur2, afir, pure,
    aice, amut, cur3, life, inv2, fog2, exit, arub
  ])
white_wizard = CharClass(
  'white wizard',
  [
    wooden_staff, iron_hammer, silver_hammer, power_staff, heal_staff, thor_hammer, masmune
  ],
  [
    cloth, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, white_robe, pro_cape, cap, 
    ribbon, gloves, pro_ring
  ],
  [
    ruse, cure, harm, fog, invs, lamp, alit, mute, cur2, hrm2, heal, afir, pure, fear, aice, amut, cur3,
    hrm3, hel2, life, inv2, fog2, soft, exit, cur4, hrm4, hel3, arub, xfer, fade, lif2, wall
  ])
black_wizard = CharClass(
  'black wizard',
  [
    small_dagger, wooden_staff, large_dagger, silver_dagger, power_staff, mage_staff, wizard_staff, 
    cat_claw, masmune
  ],
  [
    cloth, copper_bracelet, silver_bracelet, gold_bracelet, opal_bracelet, black_robe, pro_cape, cap,
    ribbon, gloves, pro_ring
  ],
  [
    lit, fire, lock, slep, dark, ice, slow, tmpr, hold, lit2, fir2, lok2, fast, ice2, conf, slow, fir3, 
    bane, slo2, warp, lit3, qake, rub, stun, blnd, brak, ice3, sabr, zap, xxxx, nuke, stop 
  ])

global castle_coneria
global coneria
global provaka
global castle_of_elf
global elf_land
global northwest_castle
global dwarf_cave
global melmond
global cresent_lake
global ryukahn_desert
global gaia
global lefein
global mirage_tower
global castle_of_ordeal
global onrac
global temple_of_friends

castle_coneria = Town('Castle Coneria', [], [], [], [])
coneria = Town(
  'Corneria', 
  [
    fire, lit, lock, slep, cure, fog, harm, ruse
  ],
  [
    wooden_nun, small_dagger, wooden_staff, rapier, iron_hammer
  ],
  [
    chain_armor, cloth, wooden_armor
  ],
  [
    heal_potion, pure_potion, tent
  ])
provaka = Town(
  'Provaka',
  [
    lamp, mute, alit, invs, ice, dark, tmpr, slow
  ],
  [
    iron_hammer, short_sword, hand_axe, scimtar
  ],
  [
    wooden_armor, chain_armor, iron_armor, wooden_shield, gloves
  ],
  [
    heal_potion, pure_potion, tent, cabin
  ]) 
castle_of_elf = Town('Castle of Elf', [], [], [], [])
elf_land = Town(
  'Elf Land',
  [
    fir2, hold, lit2, lok2, cur2, hrm2, afir, heal, slp2, fast, conf, ice2, pure, fear, aice, amut
  ],
  [
    iron_nun, large_dagger, iron_staff, sabre, silver_sword
  ],
  [
    iron_armor, copper_bracelet, iron_shield, cap, wooden_helmet
  ],
  [
    heal_potion, pure_potion, cabin, house, soft_potion
  ])
northwest_castle = Town( 'Northwest Castle', [], [], [], [])
dwarf_cave = Town( 'Dwarf Cave', [], [], [], [])
melmond = Town(
  'Melmond',
  [
    fir3, bane, warp, slo2, cur3, life, hrm3, hel2
  ],
  [
    iron_staff, sabre, long_sword, falchon
  ],
  [
    steel_armor, silver_bracelet, iron_helmet, copper_gloves, iron_gloves
  ],
  [])
crescent_lake = Town(
  'Crescent Lake',
  [
    lit3, rub, qake, stun, soft, exit, fog2, inv2
  ],
  [
    silver_dagger, silver_sword, silver_hammer, silver_axe,
  ],
  [
    silver_armor, silver_shield, buckler, silver_helmet, silver_gloves
  ],
  [
    heal_potion, pure_potion, cabin, house
  ])
ryukahn_desert = Town( 'Ryukahn_desert', [], [], [], [])
gaia = Town(
  'Gaia',
  [
    ice3, brak, cur4, hrm4, stop, zap, xxxx, fade, wall, xfer
  ],
  [
    cat_claw
  ],
  [
    gold_bracelet, pro_ring
  ],
  [
    cabin, house, heal_potion, pure_potion
  ])
lefein = Town('Lefein', [nuke, lif2], [], [], [])
mirage_tower = Town('Mirage Tower', [], [], [], [])
castle_of_ordeal = Town('Castle of Ordeal', [], [], [], [])
onrac = Town(
  'Onrac',
  [
    sabr, blnd, arub, hel3
  ], [], [],
  [
    cabin, house, heal_potion, pure_potion, soft_potion
  ])
caravan = Town('Caravan', [], [], [], [bottle])
temple_of_fiends = Town('Temple of Fiends',[], [], [], [])
