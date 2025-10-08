import json
import pkgutil

def import_data(file_name="") -> dict:
    """Import json data from file_name in the data folder"""

    # with open(f"data/{file_name}") as json_file:
        # data = json.loads(json_file.readline())
        # json_file.close()

    # return data
    return json.loads(pkgutil.get_data(__name__, f"data/{file_name}"))

ANCESTRIES = {
    "Dwarf" : [
        "Ancient-Blooded Dwarf",
        "Anvil Dwarf",
        "Death Warden Dwarf",
        "Elemental Heart Dwarf",
        "Forge Dwarf",
        "Forge-Blessed Dwarf",
        "Oathkeeper Dwarf",
        "Rock Dwarf",
        "Strong-Blooded Dwarf",
        "VH Dwarf"
    ],
    "Elf" : [
        "Ancient Elf",
        "Arctic Elf",
        "Cavern Elf",
        "Desert Elf",
        "Seer Elf",
        "Whisper Elf",
        "Woodland Elf",
        "VH Elf"
    ],
    "Gnome" : [
        "Chameleon Gnome",
        "Fey-Touched Gnome",
        "Kijimuna Gnome",
        "Sensate Gnome",
        "Umbral Gnome",
        "Vivacious Gnome",
        "Wellspring Gnome",
        "VH Gnome"
    ],
    "Goblin" : [
        "Charhide Goblin",
        "Dokkaebi Goblin",
        "Irongut Goblin",
        "Razortooth Goblin",
        "Snow Goblin",
        "Tailed Goblin",
        "Treedweller Goblin",
        "Unbreakable Goblin",
        "VH Goblin"
    ],
    "Halfling" : [
        "Gutsy Halfling",
        "Hillock Halfling",
        "Jinxed Halfling",
        "Nomadic Halfling",
        "Observant Halfling",
        "Twilight Halfling",
        "Wildwood Halfling",
        "VH Halfling"
    ],
    "Human" : [
        "Skilled Human",
        "Versatile Human",
        "Wintertouched Human",
        "VH Human"
    ],
    "Leshy" : [
        "Cactus Leshy",
        "Chrysanthemum Leshy",
        "Fruit Leshy",
        "Fungus Leshy",
        "Gourd Leshy",
        "Leaf Leshy",
        "Lotus Leshy",
        "Peachchild Leshy",
        "Pine Leshy",
        "Root Leshy",
        "Seaweed Leshy",
        "Vine Leshy",
        "VH Leshy"
    ],
    "Orc" : [
        "Badlands Orc",
        "Battle-Ready Orc",
        "Deep Orc",
        "Grave Orc",
        "Hold-Scarred Orc",
        "Rainfall Orc",
        "Winter Orc",
        "VH Orc"
    ],
    "Athamaru" : [
        "Coral Athamaru",
        "Hopeful Athamaru",
        "Kaleidoscopic Athamaru",
        "Quilled Athamaru",
        "VH Athamaru"
    ],
    "Azarketi" : [
        "Ancient Scale Azarketi",
        "Benthic Azarketi",
        "Inured Azarketi",
        "Mistbreath Azarketi",
        "Murkeyed Azarketi",
        "River Azarketi",
        "Spined Azarketi",
        "Tactile Azarketi",
        "Thalassic Azarketi",
        "VH Azarketi"
    ],
    "Catfolk" : [
        "Clawed Catfolk",
        "Flexible Catfolk",
        "Hunting Catfolk",
        "Jungle Catfolk",
        "Liminal Catfolk",
        "Nine Lives Catfolk",
        "Sharp-Eared Catfolk",
        "Winter Catfolk",
        "VH Catfolk"
    ],
    "Centaur" : [
        "Budding Speaker Centaur",
        "Fleetwind Centaur",
        "Ironhoof Centaur",
        "Mottle-Coat Centaur",
        "Ponygait Centaur",
        "Stoutheart Centaur",
        "VH Centaur"
    ],
    "Fetchling" : [
        "Bright Fetchling",
        "Deep Fetchling",
        "Liminal Fetchling",
        "Resolute Fetchling",
        "Wisp Fetchling",
        "VH Fetchling"
    ],
    "Hobgoblin" : [
        "Elfbane Hobgoblin",
        "Runtboss Hobgoblin",
        "Shortshanks Hobgoblin",
        "Smokeworker Hobgoblin",
        "Steelskin Hobgoblin",
        "Warmarch Hobgoblin",
        "Warrenbred Hobgoblin",
        "VH Hobgoblin"
    ],
    "Kholo" : [
        "Ant Kholo",
        "Cave Kholo",
        "Dog Kholo",
        "Great Kholo",
        "Sweetbreath Kholo",
        "Winter Kholo",
        "Witched Kholo",
        "VH Kholo"
    ],
    "Kitsune" : [
        "Celestial Envoy Kitsune",
        "Dark Fields Kitsune",
        "Earthly Wilds Kitsune",
        "Empty Sky Kitsune",
        "Frozen Wind Kitsune",
        "Palace Echoes Kitsune",
        "VH Kitsune"
    ],
    "Kobold" : [
        "Caveclimber Kobold",
        "Cavernstalker Kobold",
        "Dragonscaled Kobold",
        "Elementheart Kobold",
        "Heavenscribe Kobold",
        "Mightyfall Kobold",
        "Spellhorn Kobold",
        "Strongjaw Kobold",
        "Tunnelflood Kobold",
        "Venomtail Kobold",
        "VH Kobold"
    ],
    "Lizardfolk" : [
        "Bakuwa Lizardfolk",
        "Cliffscale Lizardfolk",
        "Cloudleaper Lizardfolk",
        "Frilled Lizardfolk",
        "Makari Lizardfolk",
        "Sandstrider Lizardfolk",
        "Unseen Lizardfolk",
        "Wetlander Lizardfolk",
        "Woodstalker Lizardfolk",
        "VH Lizardfolk"
    ],
    "Merfolk" : [
        "Abyssal Merfolk",
        "Carcharodon Merfolk",
        "Pelagic Merfolk",
        "Reef Merfolk",
        "Sailfish Merfolk",
        "VH Merfolk"
    ],
    "Minotaur" : [
        "Ghost Bull Minotaur",
        "Glacier Cavern Minotaur",
        "Littlehorn Minotaur",
        "Roaming Minotaur",
        "Slabsoul Minotaur",
        "Stalker Minotaur",
        "VH Minotaur"
    ],
    "Nagaji" : [
        "Hooded Nagaji",
        "Sacred Nagaji",
        "Shimmertongue Nagaji",
        "Titan Nagaji",
        "Venomshield Nagaji",
        "Whipfang Nagaji",
        "VH Nagaji"
    ],
    "Ratfolk" : [
        "Deep Ratfolk",
        "Desert Ratfolk",
        "Longsnout Ratfolk",
        "Sewer Ratfolk",
        "Shadow Ratfolk",
        "Snow Ratfolk",
        "Tunnel Ratfolk",
        "VH Ratfolk"
    ],
    "Samsaran" : [
        "Healer Samsaran",
        "Mountaineer Samsaran",
        "Oracular Samsaran",
        "Sanctuary Samsaran",
        "Wilderness Samsaran",
        "VH Samsaran"
    ],
    "Tanuki" : [
        "Ascetic Tanuki",
        "Courageous Tanuki",
        "Even-Tempered Tanuki",
        "Steadfast Tanuki",
        "Virtuous Tanuki",
        "VH Tanuki"
    ],
    "Tengu" : [
        "Dogtooth Tengu",
        "Jinxed Tengu",
        "Mountainkeeper Tengu",
        "Skyborn Tengu",
        "Stormtossed Tengu",
        "Taloned Tengu",
        "Wavediver Tengu",
        "VH Tengu"
    ],
    "Tripkee" : [
        "Poisonhide Tripkee",
        "Riverside Tripkee",
        "Snaptongue Tripkee",
        "Stickytoe Tripkee",
        "Thickskin Tripkee",
        "Windweb Tripkee",
        "VH Tripkee"
    ],
    "Vanara" : [
        "Bandaagee Vanara",
        "Lahkgyan Vanara",
        "Ragdyan Vanara",
        "Wajaghand Vanara",
        "VH Vanara"
    ],
    "Wayang" : [
        "Shadow of the Courtier Wayang",
        "Shadow of the Hermit Wayang",
        "Shadow of the Sailor Wayang",
        "Shadow of the Smith Wayang",
        "Shadow of the Wanderer Wayang",
        "VH Wayang"
    ],
    "Anadi" : [
        "Adaptive Anadi",
        "Polychromatic Anadi",
        "Snaring Anadi",
        "Spindly Anadi",
        "Venomous Anadi",
        "VH Anadi"
    ],
    "Android" : [
        "Artisan Android",
        "Impersonator Android",
        "Laborer Android",
        "Polyglot Android",
        "Warrior Android",
        "VH Android"
    ],
    "Automaton" : [
        "Hunter Automaton",
        "Mage Automaton",
        "Sharpshooter Automaton",
        "Warrior Automaton",
        "VH Automaton"
    ],
    "Awakened Animal" : [
        "Climbing Awakened Animal",
        "Flying Awakened Animal",
        "Running Awakened Animal",
        "Swimming Awakened Animal",
        "VH Awakened Animal"
    ],
    "Conrasu" : [
        "Rite of Invocation Conrasu",
        "Rite of Knowing Conrasu",
        "Rite of Light Conrasu",
        "Rite of Passage Conrasu",
        "Rite of Reinforcement Conrasu",
        "VH Conrasu"
    ],
    "Fleshwarp" : [
        "Cataphract Fleshwarp",
        "Created Fleshwarp",
        "Discarded Fleshwarp",
        "Mutated Fleshwarp",
        "Shapewrought Fleshwarp",
        "Surgewise Fleshwarp",
        "Technological Fleshwarp",
        "VH Fleshwarp"
    ],
    "Ghoran" : [
        "Ancient Ash Ghoran",
        "Enchanting Lily Ghoran",
        "Strong Oak Ghoran",
        "Thorned Rose Ghoran",
        "VH Ghoran"
    ],
    "Goloma" : [
        "Farsight Goloma",
        "Frightful Goloma",
        "Insightful Goloma",
        "Vicious Goloma",
        "Vigilant Goloma",
        "VH Goloma"
    ],
    "Jotunborn" : [
        "Keeper Jotunborn",
        "Plane-Hopper Jotunborn",
        "Sage Jotunborn",
        "Warrior Jotunborn",
        "Weaver Jotunborn",
        "VH Jotunborn"
    ],
    "Kashrishi" : [
        "Athamasi Kashrishi",
        "Lethoci Kashrishi",
        "Nascent Kashrishi",
        "Trogloshi Kashrishi",
        "Xyloshi Kashrishi",
        "VH Kashrishi"
    ],
    "Poppet" : [
        "Ghost Poppet",
        "Stuffed Poppet",
        "Toy Poppet",
        "Tsukumogami Poppet",
        "Windup Poppet",
        "Wishborn Poppet",
        "VH Poppet"
    ],
    "Sarangay" : [
        "Full Moon Sarangay",
        "Half Moon Sarangay",
        "New Moon Sarangay",
        "Waning Moon Sarangay",
        "Waxing Moon Sarangay",
        "VH Sarangay"
    ],
    "Shisk" : [
        "Lorekeeper Shisk",
        "Quillcoat Shisk",
        "Spellkeeper Shisk",
        "Stonestep Shisk",
        "Stronggut Shisk",
        "VH Shisk"
    ],
    "Shoony" : [
        "Bloodhound Shoony",
        "Fishseeker Shoony",
        "Paddler Shoony",
        "Thickcoat Shoony",
        "VH Shoony"
    ],
    "Skeleton" : [
        "Compact Skeleton",
        "Fodder Skeleton",
        "Monstrous Skeleton",
        "Shifting Skeleton",
        "Sturdy Skeleton",
        "VH Skeleton"
    ],
    "Sprite" : [
        "Dijiang Sprite",
        "Draxie Sprite",
        "Gandharva Sprite",
        "Grig Sprite",
        "Kanchil Sprite",
        "Leungli Sprite",
        "Luminous Sprite",
        "Melixie Sprite",
        "Nyktera Sprite",
        "Pixie Sprite",
        "VH Sprite"
    ],
    "Strix" : [
        "Nightglider Strix",
        "Predator Strix",
        "Scavenger Strix",
        "Shoreline Strix",
        "Songbird Strix",
        "VH Strix"
    ],
    "Surki" : [
        "Breaker Surki",
        "Elytron Surki",
        "Hardshell Surki",
        "Lantern Surki",
        "VH Surki"
    ],
    "Vishkanya" : [
        "Elusive Vishkanya",
        "Keen-Venom Vishkanya",
        "Old-Blood Vishkanya",
        "Prismatic Vishkanya",
        "Scalekeeper Vishkanya",
        "Venom-Resistant Vishkanya",
        "VH Vishkanya"
    ],
    "Yaksha" : [
        "Deny Lady Nanbyo's Charity Yaksha",
        "Deny the Firstborn Pursuit Yaksha",
        "Deny the Traitor's Rebirth Yaksha",
        "Respite of a Thousand Roofs Yaksha",
        "Respite of Cloudless Paths Yaksha",
        "Respite of Loam and Leaf Yaksha"
    ],
    "Yaoguai" : [
        "Born of Animal Yaoguai",
        "Born of Celestial Yaoguai",
        "Born of Elements Yaoguai",
        "Born of Item Yaoguai",
        "Born of Vegetation Yaoguai",
        "VH Yaoguai"
    ]
}

COMMON_ANCESTRIES = [
    "Dwarf",
    "Elf",
    "Gnome",
    "Goblin",
    "Halfling",
    "Human",
    "Leshy",
    "Orc"
]

UNCOMMON_ANCESTRIES = [
    "Athamaru",
    "Azarketi",
    "Catfolk",
    "Centaur",
    "Fetchling",
    "Hobgoblin",
    "Kholo",
    "Kitsune",
    "Kobold",
    "Lizardfolk",
    "Merfolk",
    "Minotaur",
    "Nagaji",
    "Ratfolk",
    "Samsaran",
    "Tanuki",
    "Tengu",
    "Tripkee",
    "Wayang"
]

RARE_ANCESTRIES = [
    "Anadi",
    "Android",
    "Automaton",
    "Awakened Animal",
    "Conrasu",
    "Fleshwarp",
    "Ghoran",
    "Goloma",
    "Jotunborn",
    "Kashrishi",
    "Poppet",
    "Sarangay",
    "Shisk",
    "Shoony",
    "Skeleton",
    "Sprite",
    "Strix",
    "Surki",
    "Vishkanya",
    "Yaksha",
    "Yaoguai"
]

ARMORS = import_data("armors.json")

BACKGROUNDS = import_data("backgrounds.json")

CLASSES = {
    "Alchemist" : [
        "Bomber Alchemist",
        "Chiurgeon Alchemist",
        "Mutagenist Alchemist",
        "Toxicologist Alchemist"
    ],
    "Animist" : [
        "Liturgist Animist",
        "Medium Animist",
        "Seer Animist",
        "Shaman Animist"
    ],
    "Barbarian" : [
        "Animal Instinct Barbarian",
        "Bloodrager Instinct Barbarian",
        "Decay Instinct Barbarian",
        "Dragon Instinct Barbarian",
        "Elemental Instinct Barbarian",
        "Fury Instinct Barbarian",
        "Giant Instinct Barbarian",
        "Ligneous Instinct Barbarian",
        "Spirit Instinct Barbarian",
        "Superstition Instinct Barbarian"
    ],
    "Bard" : [
        "Enigma Bard",
        "Maestro Bard",
        "Polymath Bard",
        "Warrior Bard",
        "Zoophonia Bard"
    ],
    "Champion" : [
        "Desecration Champion",
        "Grandeur Champion",
        "Iniquity Champion",
        "Justice Champion",
        "Liberation Champion",
        "Obedience Champion",
        "Redemption Champion"
    ],
    "Cleric" : [
        "Battle Creed Cleric",
        "Cloistered Cleric",
        "Warpriest Cleric"
    ],
    "Commander" : [
        "Commander"
    ],
    "Druid" : [
        "Animal Druid",
        "Cultivation Druid",
        "Flame Druid",
        "Leaf Druid",
        "Spore Druid",
        "Stone Druid",
        "Storm Druid",
        "Untamed Druid",
        "Wave Druid"
    ],
    "Exemplar" : [
        "Exemplar"
    ],
    "Fighter" : [
        "Fighter"
    ],
    "Guardian" : [
        "Guardian"
    ],
    "Investigator" : [
        "Alchemical Sciences Investigator",
        "Empiricism Investigator",
        "Esoterica Investigator",
        "Forensic Medicine Investigator",
        "Interrogation Investigator"
    ],
    "Kineticist" : [
        "Air Kineticist",
        "Earth Kineticist",
        "Fire Kineticist",
        "Metal Kineticist",
        "Water Kineticist",
        "Wood Kineticist",
        "Air and Earth Kineticist",
        "Air and Fire Kineticist",
        "Air and Metal Kineticist",
        "Air and Water Kineticist",
        "Air and Wood Kineticist",
        "Earth and Fire Kineticist",
        "Earth and Metal Kineticist",
        "Earth and Water Kineticist",
        "Earth and Wood Kineticist",
        "Fire and Metal Kineticist",
        "Fire and Water Kineticist",
        "Fire and Wood Kineticist",
        "Metal and Water Kineticist",
        "Metal and Wood Kineticist",
        "Water and Wood Kineticist"
    ],
    "Magus" : [
        "Aloof Firmament Magus",
        "Inexorable Iron Magus",
        "Laughing Shadow Magus",
        "Resurgent Maelstrom Magus",
        "Sparkling Targe Magus",
        "Starlit Span Magus",
        "Twisting Tree Magus",
        "Unfurling Brocade Magus"
    ],
    "Monk" : [
        "Monk"
    ],
    "Oracle" : [
        "Ancestors Oracle",
        "Ash Oracle",
        "Battle Oracle",
        "Blight Oracle",
        "Bones Oracle",
        "Cosmos Oracle",
        "Flames Oracle",
        "Life Oracle",
        "Lore Oracle",
        "Tempest Oracle",
        "Time Oracle"
    ],
    "Psychic" : [
        "The Distant Grasp Emotional Acceptance Psychic",
        "The Distant Grasp Gathered Lore Psychic",
        "The Distant Grasp Precise Discipline Psychic",
        "The Distant Grasp Wandering Reverie Psychic",
        "The Infinite Eye Emotional Acceptance Psychic",
        "The Infinite Eye Gathered Lore Psychic",
        "The Infinite Eye Precise Discipline Psychic",
        "The Infinite Eye Wandering Reverie Psychic",
        "The Oscillating Wave Emotional Acceptance Psychic",
        "The Oscillating Wave Gathered Lore Psychic",
        "The Oscillating Wave Precise Discipline Psychic",
        "The Oscillating Wave Wandering Reverie Psychic",
        "The Silent Whisper Emotional Acceptance Psychic",
        "The Silent Whisper Gathered Lore Psychic",
        "The Silent Whisper Precise Discipline Psychic",
        "The Silent Whisper Wandering Reverie Psychic",
        "The Tangible Dream Emotional Acceptance Psychic",
        "The Tangible Dream Gathered Lore Psychic",
        "The Tangible Dream Precise Discipline Psychic",
        "The Tangible Dream Wandering Reverie Psychic",
        "The Unbound Step Emotional Acceptance Psychic",
        "The Unbound Step Gathered Lore Psychic",
        "The Unbound Step Precise Discipline Psychic",
        "The Unbound Step Wandering Reverie Psychic"
    ],
    "Ranger" : [
        "Flurry Ranger",
        "Outwit Ranger",
        "Precision Ranger",
        "Vindication Ranger"
    ],
    "Rogue" : [
        "Avenger Rogue",
        "Eldritch Trickster Rogue",
        "Mastermind Rogue",
        "Ruffian Rogue",
        "Scoundrel Rogue",
        "Thief Rogue"
    ],
    "Sorcerer" : [
        "Aberrant Sorcerer",
        "Aesir Sorcerer",
        "Angelic Sorcerer",
        "Demonic Sorcerer",
        "Diabolic Sorcerer",
        "Draconic Sorcerer",
        "Elemental Sorcerer",
        "Fey Sorcerer",
        "Genie Sorcerer",
        "Hag Sorcerer",
        "Harrow Sorcerer",
        "Imperial Sorcerer",
        "Nymph Sorcerer",
        "Phoenix Sorcerer",
        "Psychopomp Sorcerer",
        "Shadow Sorcerer",
        "Undead Sorcerer",
        "Wyrmblessed Sorcerer"
    ],
    "Summoner" : [
        "Angel Eidolon Summoner",
        "Anger Phantom Eidolon Summoner",
        "Beast Eidolon Summoner",
        "Construct Eidolon Summoner",
        "Demon Eidolon Summoner",
        "Devotion Phantom Eidolon Summoner",
        "Dragon Eidolon Summoner",
        "Elemental Eidolon Summoner",
        "Fey Eidolon Summoner",
        "Plant Eidolon Summoner",
        "Psychopomp Eidolon Summoner",
        "Swarm Eidolon Summoner",
        "Undead Eidolon Summoner"
    ],
    "Swashbuckler" : [
        "Battledancer Swashbuckler",
        "Braggart Swashbuckler",
        "Fencer Swashbuckler",
        "Gymnast Swashbuckler",
        "Rascal Swashbuckler",
        "Wit Swashbuckler"
    ],
    "Thaumaturge" : [
        "Amulet Thaumaturge",
        "Bell Thaumaturge",
        "Chalice Thaumaturge",
        "Lantern Thaumaturge",
        "Mirror Thaumaturge",
        "Regalia Thaumaturge",
        "Shield Thaumaturge",
        "Tome Thaumaturge",
        "Wand Thaumaturge",
        "Weapon Thaumaturge"
    ],
    "Witch" : [
        "Baba Yaga Witch",
        "Choir Politic Witch",
        "Cobyslarni Witch",
        "Devourer of Decay Witch",
        "Faith's Flamekeeper Witch",
        "Mosquito Witch Witch",
        "Paradox of Opposites Witch",
        "Ripple in the Deep Witch",
        "Silence in Snow Witch",
        "Spinner of Threads Witch",
        "Starless Shadow Witch",
        "The Inscribed One Witch",
        "The Resentment Witch",
        "The Unseen Broker Witch",
        "Whisper of Wings Witch",
        "Wilding Steward Witch"
    ],
    "Wizard" : [
        "Experimental Spellshaping Wizard",
        "Improved Familiar Attunement Wizard",
        "Spell Blending Wizard",
        "Spell Substitution Wizard",
        "Staff Nexus Wizard"
    ],
    "Gunslinger" : [
        "Way of the Drifter Gunslinger",
        "Way of the Pistolero Gunslinger",
        "Way of the Sniper Gunslinger",
        "Way of the Spellshot Gunslinger",
        "Way of the Triggerbrand Gunslinger",
        "Way of the Vanguard Gunslinger"
    ],
    "Inventor" : [
        "Armor Innovation Inventor",
        "Construct Innovation Inventor",
        "Light Mortar Innovation Inventor",
        "Weapon Innovation Inventor"
    ]
}

CREATURES = import_data("creatures.json")

KEY_NAMES = {
    "Red Key",
    "Blue Key",
    "Green Key",
    "Yellow Key",
    "Cyan Key",
    "Magenta Key",
    "White Key",
    "Black Key",
    "Gray Key",
    "Orange Key",
    "Azure Key",
    "Chartreuse Key",
    "Teal Key",
    "Violet Key",
    "Pink Key",
    "Amber Key",
    "Indigo Key",
    "Purple Key",
    "Crimson Key"
}

SHIELDS = import_data("shields.json")

VERSATILE_HERITAGES = [
    "Aiuvarin",
    "Dromaar",
    "Ardande",
    "Changeling",
    "Dhampir",
    "Dragonblood",
    "Duskwalker",
    "Hungerseed",
    "Ifrit",
    "Nephilim",
    "Oread",
    "Suli",
    "Sylph",
    "Talos",
    "Undine",
    "Beastkin",
    "Reflection"
]

WEAPONS = import_data("weapons.json")

TRAITS = set()

for creature in CREATURES:
    traits = creature["trait"].split(", ")
    for trait in traits:
        if trait not in TRAITS:
            TRAITS.add(trait)

DIFFICULTIES = {
    "Trivial" : 40,
    "Low" : 60,
    "Moderate" : 80,
    "Severe" : 120,
    "Extreme" : 160
}

XP_VALUES = {
    -4 : 10,
    -3 : 15,
    -2 : 20,
    -1 : 30,
    0 : 40,
    1 : 60,
    2 : 80,
    3 : 120,
    4 : 160
}
