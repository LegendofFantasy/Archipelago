from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import APPF2eWorld

ITEM_NAME_TO_ID = {
    "Level Up" : 1,
    "Progressive Weapon Rune" : 2,
    "Progressive Armor Rune" : 3,
    "Apex Items Token" : 4,
    "Rest Token" : 5,
    "Ancestry Feat Token" : 6,
    "General Feat Token" : 7,
    "Skill Training Token" : 8,
    "Weapon Token" : 9,
    "Armor Token" : 10,
    "Shield Token" : 11,
    "Wand Token" : 12,
    "Staff Token" : 13,
    "Magic Item Token" : 14,
    "Consumable Token" : 15,
    "Apex Item Token" : 16,
    "Property Rune Token" : 17,
    "Material Token" : 18,
    "Healing Potion Token" : 19,
    "Elixir of Life Token" : 20,
    "Progressive Shield Rune" : 21,
    "Hero Point" : 22,
    "Avoid Notice Unlock" : 23,
    "Defend Unlock" : 24,
    "Detect Magic Unlock" : 25,
    "Repeat a Spell Unlock" : 26,
    "Scout Unlock" : 27,
    "Search Unlock" : 28,
    "Sustain an Effect Unlock" : 29,
    "Cover Tracks Unlock" : 30,
    "Hustle Unlock" : 31,
    "Investigate Unlock" : 32,
    "Track Unlock" : 33,
    "Red Key" : 101,
    "Blue Key" : 102,
    "Green Key" : 103,
    "Yellow Key" : 104,
    "Cyan Key" : 105,
    "Magenta Key" : 106,
    "White Key" : 107,
    "Black Key" : 108,
    "Gray Key" : 109,
    "Orange Key" : 110,
    "Azure Key" : 111,
    "Chartreuse Key" : 112,
    "Teal Key" : 113,
    "Violet Key" : 114,
    "Pink Key" : 115,
    "Amber Key" : 116,
    "Indigo Key" : 117,
    "Purple Key" : 118,
    "Crimson Key" : 119,
    "Vermilion Key" : 120
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Level Up" : ItemClassification.progression,
    "Progressive Weapon Rune" : ItemClassification.progression,
    "Progressive Armor Rune" : ItemClassification.progression,
    "Apex Items Token" : ItemClassification.progression,
    "Rest Token" : ItemClassification.filler,
    "Ancestry Feat Token" : ItemClassification.filler,
    "General Feat Token" : ItemClassification.filler,
    "Skill Training Token" : ItemClassification.filler,
    "Weapon Token" : ItemClassification.filler,
    "Armor Token" : ItemClassification.filler,
    "Shield Token" : ItemClassification.filler,
    "Wand Token" : ItemClassification.filler,
    "Staff Token" : ItemClassification.filler,
    "Magic Item Token" : ItemClassification.filler,
    "Consumable Token" : ItemClassification.filler,
    "Apex Item Token" : ItemClassification.filler,
    "Property Rune Token" : ItemClassification.filler,
    "Material Token" : ItemClassification.filler,
    "Healing Potion Token" : ItemClassification.filler,
    "Elixir of Life Token" : ItemClassification.filler,
    "Progressive Shield Rune" : ItemClassification.filler,
    "Hero Point" : ItemClassification.filler,
    "Avoid Notice Unlock" : ItemClassification.filler,
    "Defend Unlock" : ItemClassification.filler,
    "Detect Magic Unlock" : ItemClassification.filler,
    "Repeat a Spell Unlock" : ItemClassification.filler,
    "Scout Unlock" : ItemClassification.filler,
    "Search Unlock" : ItemClassification.filler,
    "Sustain an Effect Unlock" : ItemClassification.filler,
    "Cover Tracks Unlock" : ItemClassification.filler,
    "Hustle Unlock" : ItemClassification.filler,
    "Investigate Unlock" : ItemClassification.filler,
    "Track Unlock" : ItemClassification.filler,
    "Red Key" : ItemClassification.progression,
    "Blue Key" : ItemClassification.progression,
    "Green Key" : ItemClassification.progression,
    "Yellow Key" : ItemClassification.progression,
    "Cyan Key" : ItemClassification.progression,
    "Magenta Key" : ItemClassification.progression,
    "White Key" : ItemClassification.progression,
    "Black Key" : ItemClassification.progression,
    "Gray Key" : ItemClassification.progression,
    "Orange Key" : ItemClassification.progression,
    "Azure Key" : ItemClassification.progression,
    "Chartreuse Key" : ItemClassification.progression,
    "Teal Key" : ItemClassification.progression,
    "Violet Key" : ItemClassification.progression,
    "Pink Key" : ItemClassification.progression,
    "Amber Key" : ItemClassification.progression,
    "Indigo Key" : ItemClassification.progression,
    "Purple Key" : ItemClassification.progression,
    "Crimson Key" : ItemClassification.progression,
    "Vermilion Key" : ItemClassification.progression,
}


class APPF2eItem(Item):
    game = "AP Pathfinder 2e"


def get_random_filler_item_name(world: APPF2eWorld) -> str:

    filler_list = [
        "Rest Token",
        "Weapon Token",
        "Armor Token",
        "Shield Token",
        "Wand Token",
        "Staff Token",
        "Magic Item Token",
        "Consumable Token",
        "Healing Potion Token",
        "Elixir of Life Token"
    ]

    if world.options.include_ancestry_feat_tokens:
        filler_list += ["Ancestry Feat Token"]
    if world.options.include_general_feat_tokens:
        filler_list += ["General Feat Token"]
    if world.options.include_skill_training_tokens:
        filler_list += ["Skill Training Token"]
    if world.options.include_hero_points:
        filler_list += ["Hero Point"]
    if world.options.maximum_level >= 2:
        filler_list += ["Property Rune Token", "Material Token"]
    if world.options.maximum_level >= 17 and not world.options.use_abp:
        filler_list += ["Apex Item Token"]

    return world.random.choice(filler_list)


def create_item_with_correct_classification(world: APPF2eWorld, name: str) -> APPF2eItem:

    return APPF2eItem(name, DEFAULT_ITEM_CLASSIFICATIONS[name], ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: APPF2eWorld) -> None:

    itempool: list[Item] = []

    # Add all the required items
    if world.options.maximum_level.value > world.options.starting_level.value:
        for _ in range(world.options.maximum_level.value - world.options.starting_level.value):
            itempool.append(world.create_item("Level Up"))

    if not world.options.use_abp:
        if world.options.maximum_level >= 2 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Weapon Rune"))
        if world.options.maximum_level >= 4 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Weapon Rune"))
        if world.options.maximum_level >= 5 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Armor Rune"))
        if world.options.maximum_level >= 8 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Armor Rune"))
        if world.options.maximum_level >= 10 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Weapon Rune"))
        if world.options.maximum_level >= 11 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Armor Rune"))
        if world.options.maximum_level >= 12 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Weapon Rune"))
        if world.options.maximum_level >= 14 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Armor Rune"))
        if world.options.maximum_level >= 16 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Weapon Rune"))
        if world.options.maximum_level >= 17 > world.options.starting_level:
            itempool.append(world.create_item("Apex Items Token"))
        if world.options.maximum_level >= 18 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Armor Rune"))
        if world.options.maximum_level >= 19 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Weapon Rune"))
        if world.options.maximum_level >= 20 > world.options.starting_level:
            itempool.append(world.create_item("Progressive Armor Rune"))

    for key in world.keys_used:
        itempool.append(world.create_item(key))

    # In the worst case scenario the above are all the items we can add, so we need to start checking for space.
    locations_left = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)

    # Add the useful exploration activities if there's room
    if locations_left >= 7 and world.options.include_exploration_activities:
        itempool.extend([
            world.create_item("Avoid Notice Unlock"),
            world.create_item("Defend Unlock"),
            world.create_item("Detect Magic Unlock"),
            world.create_item("Repeat a Spell Unlock"),
            world.create_item("Scout Unlock"),
            world.create_item("Search Unlock"),
            world.create_item("Sustain an Effect Unlock")
        ])
        locations_left -= 7

    # Add the rest of the exploration activities if there's room
    if locations_left >= 4 and world.options.include_exploration_activities:
        itempool.extend([
            world.create_item("Cover Tracks Unlock"),
            world.create_item("Hustle Unlock"),
            world.create_item("Investigate Unlock"),
            world.create_item("Track Unlock")
        ])
        locations_left -= 4

    # Add in Progressive Shield Runes if there's room for them and they are appropriate for the level range
    if locations_left >= 1 and world.options.maximum_level >= 4:
        itempool.append(world.create_item("Progressive Shield Rune"))
        locations_left -= 1
    if locations_left >= 1 and world.options.maximum_level >= 7:
        itempool.append(world.create_item("Progressive Shield Rune"))
        locations_left -= 1
    if locations_left >= 1 and world.options.maximum_level >= 10:
        itempool.append(world.create_item("Progressive Shield Rune"))
        locations_left -= 1
    if locations_left >= 1 and world.options.maximum_level >= 13:
        itempool.append(world.create_item("Progressive Shield Rune"))
        locations_left -= 1
    if locations_left >= 1 and world.options.maximum_level >= 16:
        itempool.append(world.create_item("Progressive Shield Rune"))
        locations_left -= 1
    if locations_left >= 1 and world.options.maximum_level >= 19:
        itempool.append(world.create_item("Progressive Shield Rune"))
        locations_left -= 1

    # Add in some Rest Tokens if there's room since they're very useful, especially with low level ranges
    guaranteed_rest_tokens = (world.options.number_of_rooms.value //
                              max(3, world.options.maximum_level.value - world.options.starting_level.value))
    if locations_left >= guaranteed_rest_tokens:
        for _ in range(0, guaranteed_rest_tokens):
            itempool.append(world.create_item("Rest Token"))
        locations_left -= guaranteed_rest_tokens

    # Fill the rest of the itempool with filler
    itempool += [world.create_filler() for _ in range(locations_left)]

    # Add the itempool to the multiworld
    world.multiworld.itempool += itempool

    # Send the appropriate precollected items based on starting level
    if world.options.starting_level >= 2:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Weapon Rune"))
    if world.options.starting_level >= 3:
        world.push_precollected(world.create_item("Level Up"))
    if world.options.starting_level >= 4:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Weapon Rune"))
    if world.options.starting_level >= 5:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Armor Rune"))
    if world.options.starting_level >= 6:
        world.push_precollected(world.create_item("Level Up"))
    if world.options.starting_level >= 7:
        world.push_precollected(world.create_item("Level Up"))
    if world.options.starting_level >= 8:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Armor Rune"))
    if world.options.starting_level >= 9:
        world.push_precollected(world.create_item("Level Up"))
    if world.options.starting_level >= 10:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Weapon Rune"))
    if world.options.starting_level >= 11:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Armor Rune"))
    if world.options.starting_level >= 12:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Weapon Rune"))
    if world.options.starting_level >= 13:
        world.push_precollected(world.create_item("Level Up"))
    if world.options.starting_level >= 14:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Armor Rune"))
    if world.options.starting_level >= 15:
        world.push_precollected(world.create_item("Level Up"))
    if world.options.starting_level >= 16:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Weapon Rune"))
    if world.options.starting_level >= 17:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Apex Items Token"))
    if world.options.starting_level >= 18:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Armor Rune"))
    if world.options.starting_level >= 19:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Weapon Rune"))
    if world.options.starting_level >= 20:
        world.push_precollected(world.create_item("Level Up"))
        if not world.options.use_abp: world.push_precollected(world.create_item("Progressive Armor Rune"))

