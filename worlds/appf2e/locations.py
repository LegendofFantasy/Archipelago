from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import APPF2eWorld

LOCATION_NAME_TO_ID = {
    "Room 1 A" : 11,
    "Room 1 B" : 12,
    "Room 1 C" : 13,
    "Room 1 D" : 14,
    "Room 1 E" : 15,
    "Room 2 A" : 21,
    "Room 2 B" : 22,
    "Room 2 C" : 23,
    "Room 2 D" : 24,
    "Room 2 E" : 25,
    "Room 3 A" : 31,
    "Room 3 B" : 32,
    "Room 3 C" : 33,
    "Room 3 D" : 34,
    "Room 3 E" : 35,
    "Room 4 A" : 41,
    "Room 4 B" : 42,
    "Room 4 C" : 43,
    "Room 4 D" : 44,
    "Room 4 E" : 45,
    "Room 5 A" : 51,
    "Room 5 B" : 52,
    "Room 5 C" : 53,
    "Room 5 D" : 54,
    "Room 5 E" : 55,
    "Room 6 A" : 61,
    "Room 6 B" : 62,
    "Room 6 C" : 63,
    "Room 6 D" : 64,
    "Room 6 E" : 65,
    "Room 7 A" : 71,
    "Room 7 B" : 72,
    "Room 7 C" : 73,
    "Room 7 D" : 74,
    "Room 7 E" : 75,
    "Room 8 A" : 81,
    "Room 8 B" : 82,
    "Room 8 C" : 83,
    "Room 8 D" : 84,
    "Room 8 E" : 85,
    "Room 9 A" : 91,
    "Room 9 B" : 92,
    "Room 9 C" : 93,
    "Room 9 D" : 94,
    "Room 9 E" : 95,
    "Room 10 A" : 101,
    "Room 10 B" : 102,
    "Room 10 C" : 103,
    "Room 10 D" : 104,
    "Room 10 E" : 105,
    "Room 11 A" : 111,
    "Room 11 B" : 112,
    "Room 11 C" : 113,
    "Room 11 D" : 114,
    "Room 11 E" : 115,
    "Room 12 A" : 121,
    "Room 12 B" : 122,
    "Room 12 C" : 123,
    "Room 12 D" : 124,
    "Room 12 E" : 125,
    "Room 13 A" : 131,
    "Room 13 B" : 132,
    "Room 13 C" : 133,
    "Room 13 D" : 134,
    "Room 13 E" : 135,
    "Room 14 A" : 141,
    "Room 14 B" : 142,
    "Room 14 C" : 143,
    "Room 14 D" : 144,
    "Room 14 E" : 145,
    "Room 15 A" : 151,
    "Room 15 B" : 152,
    "Room 15 C" : 153,
    "Room 15 D" : 154,
    "Room 15 E" : 155,
    "Room 16 A" : 161,
    "Room 16 B" : 162,
    "Room 16 C" : 163,
    "Room 16 D" : 164,
    "Room 16 E" : 165,
    "Room 17 A" : 171,
    "Room 17 B" : 172,
    "Room 17 C" : 173,
    "Room 17 D" : 174,
    "Room 17 E" : 175,
    "Room 18 A" : 181,
    "Room 18 B" : 182,
    "Room 18 C" : 183,
    "Room 18 D" : 184,
    "Room 18 E" : 185,
    "Room 19 A" : 191,
    "Room 19 B" : 192,
    "Room 19 C" : 193,
    "Room 19 D" : 194,
    "Room 19 E" : 195,
    "Room 20 A" : 201,
    "Room 20 B" : 202,
    "Room 20 C" : 203,
    "Room 20 D" : 204,
    "Room 20 E" : 205,
    "Boss Room A" : 10001,
    "Boss Room B" : 10002,
    "Boss Room C" : 10003,
    "Boss Room D" : 10004,
    "Boss Room E" : 10005,
    "Boss Room F" : 10006,
    "Boss Room G" : 10007,
    "Boss Room H" : 10008,
    "Boss Room I" : 10009,
    "Boss Room J" : 10010,
    "Boss Room K" : 10011,
    "Boss Room L" : 10012,
    "Boss Room M" : 10013,
    "Boss Room N" : 10014,
    "Boss Room O" : 10015,
    "Boss Room P" : 10016,
    "Boss Room Q" : 10017,
    "Boss Room R" : 10018,
    "Boss Room S" : 10019,
    "Boss Room T" : 10020,
    "Boss Room U" : 10021,
    "Boss Room V" : 10022,
    "Boss Room W" : 10023,
    "Boss Room X" : 10024,
    "Boss Room Y" : 10025,
    "Boss Room Z" : 10026,
    "Boss Room a" : 10027,
    "Boss Room b" : 10028,
}


class APPF2eLocation(Location):
    game = "AP Pathfinder 2e"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: APPF2eWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: APPF2eWorld) -> None:

    for room in world.rooms:
        if not room == "Boss Room":
            world.get_region(room).add_locations(get_location_names_with_ids([
                f"{room} {letter}" for letter in "ABCDE"
            ]), APPF2eLocation)
        else:
            locations_needed = world.rooms[room]["Locations Needed"]
            world.get_region(room).add_locations(get_location_names_with_ids([
                f"{room} {letter}" for letter in locations_needed
            ]), APPF2eLocation)



def create_events(world: APPF2eWorld) -> None:

    world.get_region("Boss Room").add_event(
        "Final Boss Defeated", "Victory", location_type=APPF2eLocation, item_type=items.APPF2eItem
    )
