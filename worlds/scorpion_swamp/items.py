from __future__ import annotations

import collections
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ScorpionSwampWorld

ITEM_NAME_TO_ID = {
    "Skill Spell Gem" : 1,
    "Stamina Spell Gem" : 2,
    "Luck Spell Gem" : 3,
    "Fire Spell Gem" : 4,
    "Ice Spell Gem" : 5,
    "Illusion Spell Gem" : 6,
    "Friendship Spell Gem" : 7,
    "Growth Spell Gem" : 8,
    "Bless Spell Gem" : 9,
    "Fear Spell Gem" : 10,
    "Withering Spell Gem" : 11,
    "Curse Spell Gem" : 12,
    "Golden Magnet" : 13,
    "Violet Jewel" : 14,
    "Secret Word" : 15,
    "Gold Chain" : 16,
    "Magic Sword" : 17,
    "Horn of a Unicorn" : 18,
    "Magic Potion" : 19,
    "Ranger's Helmet" : 20,
    "Sword Tree Seeds" : 21,
    "Red Cloak" : 22,
    "Great Magic Sword" : 23,
    "Parrot Feathers" : 24,
    "Dire Beast Claws" : 25,
    "Progressive Skill" : 26,
    "Progressive Stamina" : 27,
    "Progressive Luck" : 28,
    "Clearing 3" : 103,
    "Clearing 4" : 104,
    "Clearing 5" : 105,
    "Clearing 6" : 106,
    "Clearing 7" : 107,
    "Clearing 8" : 108,
    "Clearing 9" : 109,
    "Clearing 10" : 110,
    "Clearing 11" : 111,
    "Clearing 12" : 112,
    "Clearing 13" : 113,
    "Clearing 14" : 114,
    "Clearing 15" : 115,
    "Clearing 16" : 116,
    "Clearing 17" : 117,
    "Clearing 18" : 118,
    "Clearing 19" : 119,
    "Clearing 20" : 120,
    "Clearing 21" : 121,
    "Clearing 23" : 123,
    "Clearing 24" : 124,
    "Clearing 25" : 125,
    "Clearing 26" : 126,
    "Clearing 27" : 127,
    "Clearing 28" : 128,
    "Clearing 29" : 129,
    "Clearing 30" : 130,
    "Clearing 32" : 132,
    "Clearing 33" : 133,
    "Clearing 34" : 134,
    "Clearing 35" : 135,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Skill Spell Gem" : ItemClassification.filler,
    "Stamina Spell Gem" : ItemClassification.filler,
    "Luck Spell Gem" : ItemClassification.filler,
    "Fire Spell Gem" : ItemClassification.useful,
    "Ice Spell Gem" : ItemClassification.useful,
    "Illusion Spell Gem" : ItemClassification.progression,
    "Friendship Spell Gem" : ItemClassification.progression,
    "Growth Spell Gem" : ItemClassification.useful,
    "Bless Spell Gem" : ItemClassification.useful,
    "Fear Spell Gem" : ItemClassification.useful,
    "Withering Spell Gem" : ItemClassification.useful,
    "Curse Spell Gem" : ItemClassification.useful,
    "Golden Magnet" : ItemClassification.trap | ItemClassification.useful,
    "Violet Jewel" : ItemClassification.useful,
    "Secret Word" : ItemClassification.useful,
    "Gold Chain" : ItemClassification.useful,
    "Magic Sword" : ItemClassification.useful,
    "Horn of a Unicorn" : ItemClassification.useful,
    "Magic Potion" : ItemClassification.useful,
    "Ranger's Helmet" : ItemClassification.useful,
    "Sword Tree Seeds" : ItemClassification.useful,
    "Red Cloak" : ItemClassification.useful,
    "Great Magic Sword" : ItemClassification.useful,
    "Parrot Feathers" : ItemClassification.trap,
    "Dire Beast Claws" : ItemClassification.filler,
    "Progressive Skill" : ItemClassification.useful,
    "Progressive Stamina" : ItemClassification.useful,
    "Progressive Luck" : ItemClassification.useful,
    "Clearing 3" : ItemClassification.progression,
    "Clearing 4" : ItemClassification.progression,
    "Clearing 5" : ItemClassification.progression,
    "Clearing 6" : ItemClassification.progression,
    "Clearing 7" : ItemClassification.progression,
    "Clearing 8" : ItemClassification.progression,
    "Clearing 9" : ItemClassification.progression,
    "Clearing 10" : ItemClassification.progression,
    "Clearing 11" : ItemClassification.progression,
    "Clearing 12" : ItemClassification.progression,
    "Clearing 13" : ItemClassification.progression,
    "Clearing 14" : ItemClassification.progression,
    "Clearing 15" : ItemClassification.progression,
    "Clearing 16" : ItemClassification.progression,
    "Clearing 17" : ItemClassification.progression,
    "Clearing 18" : ItemClassification.progression,
    "Clearing 19" : ItemClassification.progression,
    "Clearing 20" : ItemClassification.progression,
    "Clearing 21" : ItemClassification.progression,
    "Clearing 23" : ItemClassification.progression,
    "Clearing 24" : ItemClassification.progression,
    "Clearing 25" : ItemClassification.progression,
    "Clearing 26" : ItemClassification.progression,
    "Clearing 27" : ItemClassification.progression,
    "Clearing 28" : ItemClassification.progression,
    "Clearing 29" : ItemClassification.progression,
    "Clearing 30" : ItemClassification.progression,
    "Clearing 32" : ItemClassification.progression,
    "Clearing 33" : ItemClassification.progression,
    "Clearing 34" : ItemClassification.progression,
    "Clearing 35" : ItemClassification.progression,
}


class ScorpionSwampItem(Item):
    game = "Scorpion Swamp"


def get_random_filler_item_name(world: ScorpionSwampWorld) -> str:

    filler_names = sorted(collections.Counter(world.options.filler_weights.value).elements())
    if filler_names:
        return world.random.choice(filler_names)
    return "Stamina Spell Gem"


def create_item_with_correct_classification(world: ScorpionSwampWorld, name: str) -> ScorpionSwampItem:

    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if name in {"Golden Magnet", "Violet Jewel", "Gold Chain"} and world.options.spellsanity:
        classification |= ItemClassification.progression

    if name in {"Curse Spell Gem", "Ice Spell Gem"} and world.options.extra_locations:
        classification |= ItemClassification.progression

    return ScorpionSwampItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: ScorpionSwampWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Golden Magnet"),
        world.create_item("Violet Jewel"),
        world.create_item("Secret Word"),
        world.create_item("Gold Chain"),
        world.create_item("Magic Sword"),
        world.create_item("Horn of a Unicorn"),
        world.create_item("Magic Potion"),
        world.create_item("Ranger's Helmet"),
        world.create_item("Sword Tree Seeds"),
        world.create_item("Red Cloak"),
        world.create_item("Great Magic Sword"),
        world.create_item("Parrot Feathers"),
        world.create_item("Dire Beast Claws"),
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
            world.create_item("Progressive Luck"),
        ])

    if world.options.spellsanity:
        itempool.extend([
            world.create_item("Skill Spell Gem"),
            world.create_item("Skill Spell Gem"),
            world.create_item("Skill Spell Gem"),
            world.create_item("Stamina Spell Gem"),
            world.create_item("Stamina Spell Gem"),
            world.create_item("Stamina Spell Gem"),
            world.create_item("Luck Spell Gem"),
            world.create_item("Luck Spell Gem"),
            world.create_item("Luck Spell Gem"),
            world.create_item("Luck Spell Gem"), # extra from Unicorn clearing
            world.create_item("Fire Spell Gem"),
            world.create_item("Fire Spell Gem"),
            world.create_item("Fire Spell Gem"),
            world.create_item("Ice Spell Gem"),
            world.create_item("Ice Spell Gem"),
            world.create_item("Ice Spell Gem"),
            world.create_item("Illusion Spell Gem"),
            world.create_item("Illusion Spell Gem"),
            world.create_item("Illusion Spell Gem"),
            world.create_item("Friendship Spell Gem"),
            world.create_item("Friendship Spell Gem"),
            world.create_item("Friendship Spell Gem"),
            world.create_item("Friendship Spell Gem"), # extra from Unicorn clearing
            world.create_item("Growth Spell Gem"),
            world.create_item("Growth Spell Gem"),
            world.create_item("Growth Spell Gem"),
            world.create_item("Bless Spell Gem"),
            world.create_item("Bless Spell Gem"),
            world.create_item("Bless Spell Gem"),
            world.create_item("Fear Spell Gem"),
            world.create_item("Fear Spell Gem"),
            world.create_item("Withering Spell Gem"),
            world.create_item("Withering Spell Gem"),
            world.create_item("Curse Spell Gem"),
            world.create_item("Curse Spell Gem"),
        ])

    if world.options.clearingsanity:
        itempool.extend([
            world.create_item("Clearing 3"),
            world.create_item("Clearing 4"),
            world.create_item("Clearing 5"),
            world.create_item("Clearing 6"),
            world.create_item("Clearing 7"),
            world.create_item("Clearing 8"),
            world.create_item("Clearing 9"),
            world.create_item("Clearing 10"),
            world.create_item("Clearing 11"),
            world.create_item("Clearing 12"),
            world.create_item("Clearing 13"),
            world.create_item("Clearing 14"),
            world.create_item("Clearing 15"),
            world.create_item("Clearing 16"),
            world.create_item("Clearing 17"),
            world.create_item("Clearing 18"),
            world.create_item("Clearing 19"),
            world.create_item("Clearing 20"),
            world.create_item("Clearing 21"),
            world.create_item("Clearing 23"),
            world.create_item("Clearing 24"),
            world.create_item("Clearing 25"),
            world.create_item("Clearing 26"),
            world.create_item("Clearing 27"),
            world.create_item("Clearing 28"),
            world.create_item("Clearing 29"),
            world.create_item("Clearing 30"),
            world.create_item("Clearing 32"),
            world.create_item("Clearing 33"),
            world.create_item("Clearing 34"),
            world.create_item("Clearing 35"),
        ])

    filler_count = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)

    itempool += [world.create_filler() for _ in range(filler_count)]

    world.multiworld.itempool += itempool
