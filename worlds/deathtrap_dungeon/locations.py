from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items
from .options import SimplifyNinja

if TYPE_CHECKING:
    from .world import DeathtrapDungeonWorld

LOCATION_NAME_TO_ID = {
    "Starting Potion" : 1,
    "Idol's Left Eye" : 2,
    "Abandoned Backpack" : 3,
    "Slay the Dwarf" : 4,
    "Iron Grille - Loose" : 5,
    "Iron Grille - Leather Pouch" : 6,
    "Pit of Worms" : 7,
    "Trapdoor in the Sand" : 8,
    "Goblet of Red Liquid" : 9,
    "Demon Chair's Secret Panel" : 10,
    "Wooden Ball 1" : 11,
    "Wooden Ball 2" : 12,
    "Wooden Casket" : 13,
    "Wooden Box in the Iron Pipe 1" : 14,
    "Wooden Box in the Iron Pipe 2" : 15,
    "Shop in the Tunnel" : 16,
    "Hanging from an Iron Hook" : 17,
    "Slay Both Guard Dogs" : 18,
    "Ivy's Cupboard" : 19,
    "Taking the Ninja's Weapons" : 20,
    "Pole Across the Chasm" : 21,
    "Gift from the Booming Voice" : 22,
    "Slay the Orcs 1" : 23,
    "Slay the Orcs 2" : 24,
    "Gift from Sukumvit 1" : 25,
    "Gift from Sukumvit 2" : 26,
    "Skull's Left Eye" : 27,
    "Skull's Right Eye" : 28,
    "Gift from the Elf 1" : 29,
    "Gift from the Elf 2" : 30,
    "Gift from the Elf 3" : 31,
    "Gift from the Elf 4" : 32,
    "Bottom of the Pit" : 33,
    "Goblins' Cupboard 1" : 34,
    "Goblins' Cupboard 2" : 35,
    "Slay the Medusa" : 36,
    "Slay the Ninja" : 37,
    "Orc's Necklace" : 38,
    "Slay the Hobgoblins" : 39,
    "Starting Shield" : 40,
    "Meeting Horath" : 51,
    "Meeting Torgrim" : 52,
    "Meeting Thomas" : 53,
    "Meeting Ivy" : 54,
    "Meeting Ian Livingstone" : 55,
    "Meeting Igbut" : 56,
    "Meeting the Servant" : 57,
    "Meeting the Elf" : 61,
    "Meeting the Ninja" : 62,
    "Meeting the Knight" : 63,
    "Meeting Throm" : 64,
    "Meeting the Barbarian" : 65,
    "Using the Copper Key" : 71,
    "Using the Brass Key" : 72,
    "Game Over - Dying in the Arena of Death" : 101,
    "Game Over - Lacking a Jewel" : 102,
    "Game Over - Fifty-Metre Freefall" : 103,
    "Game Over - Crushing Defeat" : 104,
    "Game Over - Man in the Mirror" : 105,
    "Game Over - Hail Sukumvit" : 106,
    "Game Over - Stony Gaze" : 107,
    "Game Over - Poisoned Emerald" : 108,
    "Game Over - Another Stone for the Garden" : 109,
    "Game Over - The Bell Tolls for Thee" : 110,
    "Game Over - Chamber of the Dead" : 111,
    "Game Over - Between Troglodytes and the River" : 112,
    "Game Over - Food for the Bloodbeast" : 113,
    "Game Over - Drinking Acid" : 114,
    "Game Over - Eating the Mushrooms" : 115,
    "Game Over - Slain by the Rock Grub's Mate" : 116,
    "Game Over - Mirrored Headache" : 117,
    "Game Over - Knock-Knock" : 118,
    "Game Over - All Brawn and No Brain" : 119,
    "Game Over - Falling off the Tightrope" : 120,
    "Game Over - Too Hot to Handle" : 121,
    "Game Over - Crushed by the Boulder" : 122,
}

LOCATION_NAME_GROUPS = {
    "Game Over" : {name for name in LOCATION_NAME_TO_ID.keys() if LOCATION_NAME_TO_ID[name] > 100},
    "Trialmaster" : {name for name in LOCATION_NAME_TO_ID.keys() if 60 > LOCATION_NAME_TO_ID[name] > 50},
    "Champion" : {name for name in LOCATION_NAME_TO_ID.keys() if 70 > LOCATION_NAME_TO_ID[name] > 60},
}


class DeathtrapDungeonLocation(Location):
    game = "Deathtrap Dungeon"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: DeathtrapDungeonWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: DeathtrapDungeonWorld) -> None:

    # Start with the always included locations
    add_locations_to_region(world, "Entrance Area", [
        "Idol's Left Eye",
        "Abandoned Backpack",
        "Pit of Worms",
        "Hanging from an Iron Hook",
        "Gift from the Booming Voice",
        "Slay the Orcs 1",
        "Slay the Orcs 2",
        "Gift from Sukumvit 1",
        "Gift from Sukumvit 2",
        "Slay the Hobgoblins"
    ])
    add_locations_to_region(world, "Barbarian's Room", [
        "Goblet of Red Liquid"
    ])
    add_locations_to_region(world, "Pre-Throm Area", [
        "Wooden Ball 1",
        "Wooden Ball 2",
        "Wooden Box in the Iron Pipe 1",
        "Wooden Box in the Iron Pipe 2",
        "Skull's Left Eye",
        "Skull's Right Eye",
        "Bottom of the Pit",
        "Goblins' Cupboard 1",
        "Goblins' Cupboard 2",
        "Orc's Necklace"
    ])
    add_locations_to_region(world, "Torgrim's Trial and the Troglodytes", [
        "Slay the Dwarf",
        "Iron Grille - Loose",
        "Iron Grille - Leather Pouch",
        "Demon Chair's Secret Panel"
    ])
    add_locations_to_region(world, "Elf's Room", [
        "Gift from the Elf 1",
        "Gift from the Elf 2",
        "Gift from the Elf 3",
        "Gift from the Elf 4"
    ])
    add_locations_to_region(world, "North Past Torgrim", [
        "Wooden Casket",
        "Shop in the Tunnel"
    ])
    add_locations_to_region(world, "Far West Past Torgrim", [
        "Pole Across the Chasm",
        "Slay the Medusa"
    ])
    add_locations_to_region(world, "Ivy through Pre-Ninja Encounter", [
        "Trapdoor in the Sand",
        "Slay Both Guard Dogs",
        "Ivy's Cupboard"
    ])
    add_locations_to_region(world, "Ninja's Encounter", [
        "Taking the Ninja's Weapons",
        "Slay the Ninja"
    ])

    # Add the locations for shuffle_potion
    if world.options.shuffle_potion:
        add_locations_to_region(world, "Fang", ["Starting Potion"])

    # Add the locations for shuffle_shield
    if world.options.shuffle_shield:
        add_locations_to_region(world, "Fang", ["Starting Shield"])

    # Add the locations for trialmastersanity
    if world.options.trialmastersanity:
        add_locations_to_region(world, "Horath's Room", ["Meeting Horath"])
        add_locations_to_region(world, "Torgrim's Trial and the Troglodytes", ["Meeting Torgrim"])
        add_locations_to_region(world, "Thomas's Encounter", ["Meeting Thomas"])
        add_locations_to_region(world, "Ivy through Pre-Ninja Encounter", ["Meeting Ivy"])
        add_locations_to_region(world, "Ian's Room", ["Meeting Ian Livingstone"])
        add_locations_to_region(world, "Igbut's Encounter", ["Meeting Igbut"])
        add_locations_to_region(world, "Servant's Encounter", ["Meeting the Servant"])

    # Add the locations for championsanity
    if world.options.championsanity:
        add_locations_to_region(world, "Elf's Room", ["Meeting the Elf"])
        add_locations_to_region(world, "Ninja's Encounter", ["Meeting the Ninja"])
        add_locations_to_region(world, "Horath's Room", ["Meeting the Knight"])
        add_locations_to_region(world, "Throm's Area", ["Meeting Throm"])
        add_locations_to_region(world, "Barbarian's Room", ["Meeting the Barbarian"])

    # Add the locations for extra_locks
    if world.options.extra_locks:
        add_locations_to_region(world, "Pre-Throm Area", ["Using the Copper Key"])
        add_locations_to_region(world, "Past the Brass Key Door", ["Using the Brass Key"])

    # Add the locations for extra_locations
    if world.options.extra_locations:
        add_locations_to_region(world, "Entrance Area", [
            "Game Over - Hail Sukumvit",
            "Game Over - Poisoned Emerald",
            "Game Over - The Bell Tolls for Thee",
            "Game Over - Drinking Acid",
            "Game Over - Too Hot to Handle"
        ])
        add_locations_to_region(world, "Pre-Throm Area", [
            "Game Over - Fifty-Metre Freefall",
            "Game Over - Man in the Mirror",
            "Game Over - Eating the Mushrooms",
            "Game Over - Slain by the Rock Grub's Mate",
            "Game Over - Mirrored Headache",
            "Game Over - Knock-Knock",
            "Game Over - Crushed by the Boulder"
        ])
        add_locations_to_region(world, "Horath's Room", [
            "Game Over - Another Stone for the Garden"
        ])
        add_locations_to_region(world, "Throm's Area", [
            "Game Over - Chamber of the Dead"
        ])
        add_locations_to_region(world, "Torgrim's Trial and the Troglodytes", [
            "Game Over - Dying in the Arena of Death",
            "Game Over - Between Troglodytes and the River",
            "Game Over - All Brawn and No Brain"
        ])
        add_locations_to_region(world, "North Routes' Convergence", [
            "Game Over - Crushing Defeat"
        ])
        add_locations_to_region(world, "Far West Past Torgrim", [
            "Game Over - Stony Gaze",
            "Game Over - Falling off the Tightrope"
        ])
        add_locations_to_region(world, "Bloodbeast and Manticore Encounters", [
            "Game Over - Food for the Bloodbeast"
        ])
        add_locations_to_region(world, "Igbut's Encounter", [
            "Game Over - Lacking a Jewel"
        ])


def add_locations_to_region(world: DeathtrapDungeonWorld, region: str, locations: list[str]) -> None:
    world.get_region(region).add_locations(get_location_names_with_ids(locations), DeathtrapDungeonLocation)


def create_events(world: DeathtrapDungeonWorld) -> None:

    add_events_to_region(world, "Return to Fang", {"Beat Deathtrap Dungeon" : "Victory"})


def add_events_to_region(world: DeathtrapDungeonWorld, region: str, events: dict[str,str]) -> None:
    for event in events:
        world.get_region(region).add_event(
            event, events[event], location_type=DeathtrapDungeonLocation, item_type=items.DeathtrapDungeonItem
        )
