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
    "Boss Room AA" : 10027,
    "Boss Room AB" : 10028,
}


class APPF2eLocation(Location):
    game = "AP Pathfinder 2e"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: APPF2eWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: APPF2eWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    overworld = world.get_region("Overworld")
    top_left_room = world.get_region("Top Left Room")
    bottom_right_room = world.get_region("Bottom Right Room")
    right_room = world.get_region("Right Room")

    # One way to create locations is by just creating them directly via their constructor.
    bottom_left_chest = APPF2eLocation(
        world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    )

    # You can then add them to the region.
    overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    bottom_right_room_locations = get_location_names_with_ids(
        ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    )
    bottom_right_room.add_locations(bottom_right_room_locations, APPF2eLocation)

    top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    top_left_room.add_locations(top_left_room_locations, APPF2eLocation)

    right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    right_room.add_locations(right_room_locations, APPF2eLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, APPF2eLocation)
    else:
        overworld.add_locations(top_middle_room_locations, APPF2eLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        overworld.add_locations(bottom_left_extra_chest, APPF2eLocation)


def create_events(world: APPF2eWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = Location(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.APPF2eItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=APPF2eLocation, item_type=items.APPF2eItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
