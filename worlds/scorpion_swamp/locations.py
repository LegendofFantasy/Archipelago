from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

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


class ScorpionSwampLocation(Location):
    game = "Scorpion Swamp"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ScorpionSwampWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ScorpionSwampWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    overworld = world.get_region("Overworld")
    top_left_room = world.get_region("Top Left Room")
    bottom_right_room = world.get_region("Bottom Right Room")
    right_room = world.get_region("Right Room")

    # One way to create locations is by just creating them directly via their constructor.
    bottom_left_chest = ScorpionSwampLocation(
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
    bottom_right_room.add_locations(bottom_right_room_locations, ScorpionSwampLocation)

    top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    top_left_room.add_locations(top_left_room_locations, ScorpionSwampLocation)

    right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    right_room.add_locations(right_room_locations, ScorpionSwampLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, ScorpionSwampLocation)
    else:
        overworld.add_locations(top_middle_room_locations, ScorpionSwampLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        overworld.add_locations(bottom_left_extra_chest, ScorpionSwampLocation)


def create_events(world: ScorpionSwampWorld) -> None:
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
    button_in_top_left_room = ScorpionSwampLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.ScorpionSwampItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=ScorpionSwampLocation, item_type=items.ScorpionSwampItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
