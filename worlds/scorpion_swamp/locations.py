from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import ScorpionSwampWorld

LOCATION_NAME_TO_ID = {
    "Fallen Fighter" : 1,
    "Slay the Parrot" : 2,
    "Eagle's Nest" : 3,
    "Slay the Dire Beast" : 4,
    "Slay Grimslade" : 5,
    "Gift from the Mistress of Birds" : 6,
    "Gift from the Master of Wolves" : 7,
    "Slay the Ranger" : 8,
    "Gift from Grimslade" : 9,
    "Slay the Unicorn" : 10,
    "Slay the Pool Beast" : 11,
    "Slay the Sword Trees" : 12,
    "Slay the Thief" : 13,
    "Game Over - A Feast for Rats" : 14,
    "Game Over - Crocodile Smile" : 15,
    "Game Over - A Hundred Pieces of Gold" : 16,
    "Game Over - Failing Selator's Quest" : 17,
    "Game Over - Itsy Bitsy Spider" : 18,
    "Game Over - Failing Poomchukker's Quest" : 19,
    "Game Over - Curse of the Birds" : 20,
    "Game Over - Magic Carpet Ride" : 21,
    "Game Over - Dragged Down Into the River" : 22,
    "Game Over - Grimslade's Trap" : 23,
    "Game Over - Out the Window and Into the Dungeons" : 24,
    "Game Over - A Feast for the Spiders" : 25,
    "Game Over - Slain by Poomchukker's Guards" : 26,
    "Game Over - Explosion of Hellfire" : 27,
    "Game Over - The Master of Spiders Has No Friends" : 28,
    "Game Over - Returning to Grimslade Empty-Handed": 99,
    "Halicar's Shop 1" : 29,
    "Halicar's Shop 2" : 30,
    "Halicar's Shop 3" : 31,
    "Halicar's Shop 4" : 32,
    "Halicar's Shop 5" : 33,
    "Halicar's Shop 6" : 34,
    "Selator's Spell Gem 1" : 35,
    "Selator's Spell Gem 2" : 36,
    "Selator's Spell Gem 3" : 37,
    "Selator's Spell Gem 4" : 38,
    "Selator's Spell Gem 5" : 39,
    "Selator's Spell Gem 6" : 40,
    "Selator's Spell Gem 7" : 41,
    "Selator's Spell Gem 8" : 42,
    "Selator's Spell Gem 9" : 43,
    "Poomchukker's Spell Gem 1" : 44,
    "Poomchukker's Spell Gem 2" : 45,
    "Poomchukker's Spell Gem 3" : 46,
    "Poomchukker's Spell Gem 4" : 47,
    "Poomchukker's Spell Gem 5" : 48,
    "Poomchukker's Spell Gem 6" : 49,
    "Grimslade's Spell Gem 1" : 50,
    "Grimslade's Spell Gem 2" : 51,
    "Grimslade's Spell Gem 3" : 52,
    "Grimslade's Spell Gem 4" : 53,
    "Grimslade's Spell Gem 5" : 54,
    "Grimslade's Spell Gem 6" : 55,
    "Grimslade's Spell Gem 7" : 56,
    "Grimslade's Spell Gem 8" : 57,
    "Grimslade's Spell Gem 9" : 58,
    "Gift from the Master of Gardens 1" : 59,
    "Gift from the Master of Gardens 2" : 60,
    "Gift from the Master of Gardens 3" : 61,
    "Unicorn Clearing Spell Gem 1" : 62,
    "Unicorn Clearing Spell Gem 2" : 63,
    "Gronar - Directions to Selator" : 64,
    "Gronar - Directions to Poomchukker" : 65,
    "Gronar - Directions to Grimslade" : 66,
    "Clearing 1 Entered" : 101,
    "Clearing 3 Entered" : 103,
    "Clearing 4 Entered" : 104,
    "Clearing 5 Entered" : 105,
    "Clearing 6 Entered" : 106,
    "Clearing 7 Entered" : 107,
    "Clearing 8 Entered" : 108,
    "Clearing 9 Entered" : 109,
    "Clearing 10 Entered" : 110,
    "Clearing 11 Entered" : 111,
    "Clearing 12 Entered" : 112,
    "Clearing 13 Entered" : 113,
    "Clearing 14 Entered" : 114,
    "Clearing 15 Entered" : 115,
    "Clearing 16 Entered" : 116,
    "Clearing 17 Entered" : 117,
    "Clearing 18 Entered" : 118,
    "Clearing 19 Entered" : 119,
    "Clearing 20 Entered" : 120,
    "Clearing 21 Entered" : 121,
    "Clearing 23 Entered" : 123,
    "Clearing 24 Entered" : 124,
    "Clearing 25 Entered" : 125,
    "Clearing 26 Entered" : 126,
    "Clearing 27 Entered" : 127,
    "Clearing 28 Entered" : 128,
    "Clearing 29 Entered" : 129,
    "Clearing 30 Entered" : 130,
    "Clearing 32 Entered" : 132,
    "Clearing 33 Entered" : 133,
    "Clearing 34 Entered" : 134,
    "Clearing 35 Entered" : 135,
}

LOCATION_NAME_GROUPS = {
    "Clearing" : {name for name in LOCATION_NAME_TO_ID.keys() if LOCATION_NAME_TO_ID[name] > 100},
    "Selator" : {
        "Gronar - Directions to Selator",
        "Selator's Spell Gem 1",
        "Selator's Spell Gem 2",
        "Selator's Spell Gem 3",
        "Selator's Spell Gem 4",
        "Selator's Spell Gem 5",
        "Selator's Spell Gem 6",
        "Selator's Spell Gem 7",
        "Selator's Spell Gem 8",
        "Selator's Spell Gem 9",
        "Gift from the Mistress of Birds",
        "Gift from the Master of Gardens 1",
        "Gift from the Master of Gardens 2",
        "Gift from the Master of Gardens 3",
        "Game Over - Failing Selator's Quest"
    },
    "Poomchukker" : {
        "Gronar - Directions to Poomchukker",
        "Poomchukker's Spell Gem 1",
        "Poomchukker's Spell Gem 2",
        "Poomchukker's Spell Gem 3",
        "Poomchukker's Spell Gem 4",
        "Poomchukker's Spell Gem 5",
        "Poomchukker's Spell Gem 6",
        "Game Over - A Hundred Pieces of Gold",
        "Game Over - Failing Poomchukker's Quest",
        "Game Over - Out the Window and Into the Dungeons",
        "Game Over - Slain by Poomchukker's Guards"
    },
    "Grimslade" : {
        "Gronar - Directions to Grimslade",
        "Grimslade's Spell Gem 1",
        "Grimslade's Spell Gem 2",
        "Grimslade's Spell Gem 3",
        "Grimslade's Spell Gem 4",
        "Grimslade's Spell Gem 5",
        "Grimslade's Spell Gem 6",
        "Grimslade's Spell Gem 7",
        "Grimslade's Spell Gem 8",
        "Grimslade's Spell Gem 9",
        "Slay Grimslade",
        "Gift from Grimslade",
        "Slay the Ranger",
        "Game Over - Itsy Bitsy Spider",
        "Game Over - Magic Carpet Ride",
        "Game Over - Grimslade's Trap",
        "Game Over - Explosion of Hellfire",
        "Game Over - Returning to Grimslade Empty-Handed"
    }
}


class ScorpionSwampLocation(Location):
    game = "Scorpion Swamp"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ScorpionSwampWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ScorpionSwampWorld) -> None:

    # Start with the always included locations
    add_locations_to_region(world, "Fenmarge", ["Slay Grimslade", "Gift from Grimslade"])
    add_locations_to_region(world, "Clearing 4", ["Gift from the Master of Wolves"])
    add_locations_to_region(world, "Clearing 5", ["Fallen Fighter"])
    add_locations_to_region(world, "Clearing 6", ["Slay the Dire Beast"])
    add_locations_to_region(world, "Clearing 9", ["Slay the Thief"])
    add_locations_to_region(world, "Clearing 14", ["Slay the Parrot", "Gift from the Mistress of Birds"])
    add_locations_to_region(world, "Clearing 16", ["Eagle's Nest"])
    add_locations_to_region(world, "Clearing 18", ["Slay the Sword Trees"])
    add_locations_to_region(world, "Clearing 19", ["Slay the Ranger"])
    add_locations_to_region(world, "Clearing 25", ["Slay the Pool Beast"])
    add_locations_to_region(world, "Clearing 29", ["Slay the Unicorn"])

    # Add the locations for the extra_locations option
    if world.options.extra_locations:
        add_locations_to_region(world, "Fenmarge", [
            "Game Over - A Hundred Pieces of Gold",
            "Game Over - Failing Selator's Quest",
            "Game Over - Itsy Bitsy Spider",
            "Game Over - Failing Poomchukker's Quest",
            "Game Over - Magic Carpet Ride",
            "Game Over - Grimslade's Trap",
            "Game Over - Out the Window and Into the Dungeons",
            "Game Over - Slain by Poomchukker's Guards",
            "Game Over - Explosion of Hellfire",
            "Game Over - Returning to Grimslade Empty-Handed"
        ])
        add_locations_to_region(world, "Clearing 1", ["Game Over - A Feast for Rats"])
        add_locations_to_region(world, "Clearing 14", ["Game Over - Curse of the Birds"])
        add_locations_to_region(world, "Clearing 17", [
            "Game Over - A Feast for the Spiders",
            "Game Over - The Master of Spiders Has No Friends"
        ])
        add_locations_to_region(world, "Clearing 20", ["Game Over - Crocodile Smile"])
        add_locations_to_region(world, "Clearing 33", ["Game Over - Dragged Down Into the River"])

    # Add the locations for the spellsanity option
    if world.options.spellsanity:
        add_locations_to_region(world, "Fenmarge", [
            "Selator's Spell Gem 1",
            "Selator's Spell Gem 2",
            "Selator's Spell Gem 3",
            "Selator's Spell Gem 4",
            "Selator's Spell Gem 5",
            "Selator's Spell Gem 6",
            "Selator's Spell Gem 7",
            "Selator's Spell Gem 8",
            "Selator's Spell Gem 9",
            "Poomchukker's Spell Gem 1",
            "Poomchukker's Spell Gem 2",
            "Poomchukker's Spell Gem 3",
            "Poomchukker's Spell Gem 4",
            "Poomchukker's Spell Gem 5",
            "Poomchukker's Spell Gem 6",
            "Grimslade's Spell Gem 1",
            "Grimslade's Spell Gem 2",
            "Grimslade's Spell Gem 3",
            "Grimslade's Spell Gem 4",
            "Grimslade's Spell Gem 5",
            "Grimslade's Spell Gem 6",
            "Grimslade's Spell Gem 7",
            "Grimslade's Spell Gem 8",
            "Grimslade's Spell Gem 9"
        ])
        add_locations_to_region(world, "Willowbend", [
            "Halicar's Shop 1",
            "Halicar's Shop 2",
            "Halicar's Shop 3",
            "Halicar's Shop 4",
            "Halicar's Shop 5",
            "Halicar's Shop 6"
        ])
        add_locations_to_region(world, "Clearing 27", [
            "Gift from the Master of Gardens 1",
            "Gift from the Master of Gardens 2",
            "Gift from the Master of Gardens 3"
        ])
        add_locations_to_region(world, "Clearing 29", [
            "Unicorn Clearing Spell Gem 1",
            "Unicorn Clearing Spell Gem 2"
        ])

    # add the locations for the clearingsanity option
    if world.options.clearingsanity:
        for i in range(1, 36):
            if i not in {2, 22, 31}:
                add_locations_to_region(world, f"Clearing {i}", [f"Clearing {i} Entered"])

    # add the locations for the wizardsanity option
    if world.options.wizardsanity:
        add_locations_to_region(world, "Fenmarge", [
            "Gronar - Directions to Selator",
            "Gronar - Directions to Poomchukker",
            "Gronar - Directions to Grimslade"
        ])



def add_locations_to_region(world: ScorpionSwampWorld, region: str, locations: list[str]) -> None:
    world.get_region(region).add_locations(get_location_names_with_ids(locations), ScorpionSwampLocation)


def create_events(world: ScorpionSwampWorld) -> None:

    add_events_to_region(world, "Fenmarge", {
        "Give Antherica to Selator" : "Selator Victory",
        "Give Map to Poomchukker" : "Poomchukker Victory",
        "Give Amulets to Grimslade" : "Grimslade Victory"
    })
    add_events_to_region(world, "Willowbend", {"Reach Willowbend" : "Map to Willowbend"})
    add_events_to_region(world, "Clearing 4", {"Slay the Master of Wolves" : "Wolf Amulet"})
    add_events_to_region(world, "Clearing 8", {"Rob the Master of Frogs" : "Frog Amulet"})
    add_events_to_region(world, "Clearing 11", {"Antherica Bush" : "Antherica Berry"})
    add_events_to_region(world, "Clearing 14", {"Negotiate with the Mistress of Birds" : "Bird Amulet"})
    add_events_to_region(world, "Clearing 17", {"Slay the Master of Spiders" : "Spider Amulet"})
    add_events_to_region(world, "Clearing 27", {"Slay the Master of Gardens" : "Flower Amulet"})


def add_events_to_region(world: ScorpionSwampWorld, region: str, events: dict[str,str]) -> None:
    for event in events:
        world.get_region(region).add_event(
            event, events[event], location_type=ScorpionSwampLocation, item_type=items.ScorpionSwampItem
        )
