from __future__ import annotations

import collections
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .options import SimplifyNinja

if TYPE_CHECKING:
    from .world import DeathtrapDungeonWorld

ITEM_NAME_TO_ID = {
    "Pack of Provisions" : 1,
    "Potion of Skill" : 2,
    "Potion of Strength" : 3,
    "Potion of Fortune" : 4,
    "Progressive Skill" : 5,
    "Progressive Stamina" : 6,
    "Progressive Luck" : 7,
    "Iron Key" : 10,
    "Emerald" : 11,
    "Gold Piece" : 12,
    "Chainmail" : 13,
    "Sapphire" : 14,
    "Grappling Iron" : 15,
    "Brass Bell" : 16,
    "Hollow Wooden Tube" : 17,
    "Ring of Wishes" : 18,
    "Dagger" : 19,
    "Shield" : 20,
    "Goblet" : 21,
    "Doppelganger Potion" : 22,
    "Bone Monkey Charm" : 23,
    "Wooden Ball" : 24,
    "Pearl" : 25,
    "Bamboo Stilts" : 26,
    "Rope" : 27,
    "Leprechaun Tooth" : 28,
    "Old Bone" : 29,
    "Ninja's Weapons" : 30,
    "Winged Helmet" : 31,
    "Topaz" : 32,
    "Mirror" : 33,
    "Ruby" : 34,
    "Wooden Mallet" : 35,
    "Iron Spikes" : 36,
    "Garnet" : 37,
    "Diamond" : 38,
    "Necklace" : 39,
    "Jug of Acid" : 40,
    "Horath" : 51,
    "Torgrim" : 52,
    "Thomas" : 53,
    "Ivy" : 54,
    "Ian Livingstone" : 55,
    "Igbut" : 56,
    "Servant of the Trialmasters" : 57,
    "Elf" : 61,
    "Ninja" : 62,
    "Knight" : 63,
    "Throm" : 64,
    "Barbarian" : 65,
    "Brass Key" : 71,
    "Copper Key" : 72,
}

ITEM_NAME_GROUPS = {
    "Progressive Statistic" : {"Progressive Skill", "Progressive Stamina", "Progressive Luck"},
    "Progressive Stat" : {"Progressive Skill", "Progressive Stamina", "Progressive Luck"},
    "Trialmaster" : {name for name in ITEM_NAME_TO_ID.keys() if 60 > ITEM_NAME_TO_ID[name] > 50},
    "Champion" : {name for name in ITEM_NAME_TO_ID.keys() if 70 > ITEM_NAME_TO_ID[name] > 60},
    "Key" : {"Iron Key", "Brass Key", "Copper Key"}
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Pack of Provisions" : ItemClassification.filler,
    "Potion of Skill" : ItemClassification.filler,
    "Potion of Strength" : ItemClassification.filler,
    "Potion of Fortune" : ItemClassification.filler,
    "Progressive Skill" : ItemClassification.useful,
    "Progressive Stamina" : ItemClassification.useful,
    "Progressive Luck" : ItemClassification.useful,
    "Iron Key" : ItemClassification.progression,
    "Emerald" : ItemClassification.progression_skip_balancing,
    "Gold Piece" : ItemClassification.progression_deprioritized,
    "Chainmail" : ItemClassification.filler,
    "Sapphire" : ItemClassification.progression_skip_balancing,
    "Grappling Iron" : ItemClassification.useful,
    "Brass Bell" : ItemClassification.filler,
    "Hollow Wooden Tube" : ItemClassification.useful,
    "Ring of Wishes" : ItemClassification.useful,
    "Dagger" : ItemClassification.useful,
    "Shield" : ItemClassification.useful,
    "Goblet" : ItemClassification.filler,
    "Doppelganger Potion" : ItemClassification.useful,
    "Bone Monkey Charm" : ItemClassification.useful,
    "Wooden Ball" : ItemClassification.filler,
    "Pearl" : ItemClassification.filler,
    "Bamboo Stilts" : ItemClassification.useful,
    "Rope" : ItemClassification.useful,
    "Leprechaun Tooth" : ItemClassification.filler,
    "Old Bone" : ItemClassification.useful,
    "Ninja's Weapons" : ItemClassification.filler,
    "Winged Helmet" : ItemClassification.filler,
    "Topaz" : ItemClassification.filler,
    "Mirror" : ItemClassification.filler,
    "Ruby" : ItemClassification.filler,
    "Wooden Mallet" : ItemClassification.filler,
    "Iron Spikes" : ItemClassification.filler,
    "Garnet" : ItemClassification.filler,
    "Diamond" : ItemClassification.progression_skip_balancing,
    "Necklace" : ItemClassification.filler,
    "Jug of Acid" : ItemClassification.useful,
    "Horath" : ItemClassification.progression,
    "Torgrim" : ItemClassification.progression,
    "Thomas" : ItemClassification.progression,
    "Ivy" : ItemClassification.progression,
    "Ian Livingstone" : ItemClassification.progression,
    "Igbut" : ItemClassification.progression,
    "Servant of the Trialmasters" : ItemClassification.progression,
    "Elf" : ItemClassification.progression,
    "Ninja" : ItemClassification.progression,
    "Knight" : ItemClassification.progression,
    "Throm" : ItemClassification.progression,
    "Barbarian" : ItemClassification.progression,
    "Brass Key" : ItemClassification.progression,
    "Copper Key" : ItemClassification.progression,
}


class DeathtrapDungeonItem(Item):
    game = "Deathtrap Dungeon"


def get_random_filler_item_name(world: DeathtrapDungeonWorld) -> str:

    filler_names = sorted(collections.Counter(world.options.filler_weights.value).elements())
    if filler_names:
        return world.random.choice(filler_names)
    return "Pack of Provisions"


def create_item_with_correct_classification(world: DeathtrapDungeonWorld, name: str) -> DeathtrapDungeonItem:

    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if name == "Pack of Provisions" and world.options.pack_size.value < 0:
        classification = ItemClassification.trap

    if name in {"Pearl", "Topaz", "Ruby", "Garnet"} and world.options.gem_hunt:
        classification = ItemClassification.progression_deprioritized_skip_balancing

    if name == "Ninja's Weapons" and world.options.simplify_ninja.value == SimplifyNinja.option_item:
        classification = ItemClassification.progression

    return DeathtrapDungeonItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: DeathtrapDungeonWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Emerald"), # Idol's Left Eye
        world.create_item("Gold Piece"), # Abandoned Backpack
        world.create_item("Chainmail"), # Slay the Dwarf
        world.create_item("Grappling Iron"), # Iron Grille - Loose
        world.create_item("Brass Bell"), # Iron Grille - Leather Pouch
        world.create_item("Dagger"), # Pit of Worms
        world.create_item("Shield"), # Trapdoor in the Sand
        world.create_item("Goblet"), # Goblet of Red Liquid
        world.create_item("Doppelganger Potion"), # Demon Chair's Secret Panel
        world.create_item("Wooden Ball"), # Wooden Ball 1
        world.create_item("Wooden Ball"), # Wooden Ball 2
        world.create_item("Pearl"), # Wooden Casket
        world.create_item("Iron Key"), # Wooden Box in the Iron Pipe 1
        world.create_item("Sapphire"), # Wooden Box in the Iron Pipe 2
        world.create_item("Bamboo Stilts"), # Shop in the Tunnel
        world.create_item("Rope"), # Hanging from an Iron Hook
        world.create_item("Leprechaun Tooth"), # Slay Both Guard Dogs
        world.create_item("Old Bone"), # Ivy's Cupboard
        world.create_item("Ninja's Weapons"), # Taking the Ninja's Weapons
        world.create_item("Winged Helmet"), # Pole Across the Chasm
        world.create_item("Ring of Wishes"), # Gift from the Booming Voice
        world.create_item("Hollow Wooden Tube"), # Slay the Orcs 1
        world.create_item("Gold Piece"), # Slay the Orcs 2
        world.create_item("Gold Piece"), # Gift from Sukumvit 1
        world.create_item("Gold Piece"), # Gift from Sukumvit 2
        world.create_item("Topaz"), # Skull's Left Eye
        world.create_item("Topaz"), # Skull's Right Eye
        world.create_item("Bone Monkey Charm"), # Gift from the Elf 1
        world.create_item("Mirror"), # Gift from the Elf 2
        world.create_item("Dagger"), # Gift from the Elf 3
        world.create_item("Dagger"), # Gift from the Elf 4
        world.create_item("Ruby"), # Bottom of the Pit
        world.create_item("Wooden Mallet"), # Goblins' Cupboard 1
        world.create_item("Iron Spikes"), # Goblins' Cupboard 2
        world.create_item("Garnet"), # Slay the Medusa
        world.create_item("Diamond"), # Slay the Ninja
        world.create_item("Necklace"), # Orc's Necklace
        world.create_item("Jug of Acid") # Slay the Hobgoblins
    ]

    if world.options.progressive_stats:
        itempool.extend([
            world.create_item("Progressive Skill"),
            world.create_item("Progressive Skill"),
            world.create_item("Progressive Skill"),
            world.create_item("Progressive Skill"),
            world.create_item("Progressive Skill"),
            world.create_item("Progressive Stamina"),
            world.create_item("Progressive Stamina"),
            world.create_item("Progressive Stamina"),
            world.create_item("Progressive Stamina"),
            world.create_item("Progressive Stamina"),
            world.create_item("Progressive Luck"),
            world.create_item("Progressive Luck"),
            world.create_item("Progressive Luck"),
            world.create_item("Progressive Luck"),
            world.create_item("Progressive Luck")
        ])

    if world.options.shuffle_shield:
        itempool.extend([world.create_item("Shield")]) # Starting Shield

    if world.options.shuffle_potion:
        itempool.extend([ # Starting Potion
            world.create_item(world.random.choice(["Potion of Skill", "Potion of Strength", "Potion of Fortune"]))
        ])

    if world.options.trialmastersanity:
        itempool.extend([
            world.create_item("Horath"),
            world.create_item("Torgrim"),
            world.create_item("Thomas"),
            world.create_item("Ivy"),
            world.create_item("Ian Livingstone"),
            world.create_item("Igbut"),
            world.create_item("Servant of the Trialmasters")
        ])

    if world.options.championsanity:
        itempool.extend([
            world.create_item("Elf"),
            world.create_item("Ninja"),
            world.create_item("Knight"),
            world.create_item("Throm"),
            world.create_item("Barbarian")
        ])

    if world.options.extra_locks:
        itempool.extend([
            world.create_item("Brass Key"),
            world.create_item("Copper Key")
        ])

    filler_count = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)

    itempool += [world.create_filler() for _ in range(filler_count)]

    world.multiworld.itempool += itempool
