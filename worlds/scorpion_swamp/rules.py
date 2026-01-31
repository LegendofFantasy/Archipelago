from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule
from .options import Goal

if TYPE_CHECKING:
    from .world import ScorpionSwampWorld


def set_all_rules(world: ScorpionSwampWorld) -> None:

    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: ScorpionSwampWorld) -> None:

    # No additional rules are needed for common locations

    # Set rules for clearingsanity; these rules ensure that these locations can be accessed on Grimslade's quest
    # since they are only obtainable on that quest. On the others, 14 connects to 16
    if world.options.clearingsanity:
        set_rule(world.get_location("Slay the Ranger"),
                 lambda state: state.has_all(("Clearing 35", "Clearing 13"), world.player) and
                               (state.has_all(("Clearing 29", "Clearing 18", "Clearing 34", "Clearing 4"),
                                              world.player) and (
                                state.has_all(("Clearing 9", "Clearing 20", "Clearing 33"), world.player) or
                                state.has_all(("Clearing 9", "Clearing 5"), world.player) or
                                state.has_all(("Clearing 3", "Clearing 26", "Clearing 24", "Clearing 5"), world.player)
                               )) or
                               (state.has_all(("Clearing 24", "Clearing 17", "Clearing 12"), world.player) and (
                                 state.has_all(("Clearing 5", "Clearing 9"), world.player) or
                                 state.has_all(("Clearing 26", "Clearing 3"), world.player)
                               ))
                 )
        set_rule(world.get_location("Slay the Master of Gardens"),
                 lambda state: state.has_all(("Clearing 35", "Clearing 13"), world.player) and
                               (state.has_all(("Clearing 29", "Clearing 18", "Clearing 34", "Clearing 4"),
                                              world.player) and (
                                        state.has_all(("Clearing 9", "Clearing 20", "Clearing 33"), world.player) or
                                        state.has_all(("Clearing 9", "Clearing 5"), world.player) or
                                        state.has_all(("Clearing 3", "Clearing 26", "Clearing 24", "Clearing 5"),
                                                      world.player)
                                )) or
                               (state.has_all(("Clearing 24", "Clearing 17", "Clearing 12"), world.player) and (
                                       state.has_all(("Clearing 5", "Clearing 9"), world.player) or
                                       state.has_all(("Clearing 26", "Clearing 3"), world.player)
                               ))
                 )
        if world.options.spellsanity:
            set_rule(world.get_location("Rob the Master of Frogs"),
                     lambda state: state.has_all(("Clearing 26", "Illusion Spell Gem"), world.player) and
                                   (state.has("Clearing 24", world.player) and (
                                       state.has_all(("Clearing 5", "Clearing 29", "Clearing 18", "Clearing 34",
                                                      "Clearing 4"), world.player) or
                                       state.has_all(("Clearing 17", "Clearing 12"), world.player)
                                   )) or
                                   (state.has_all(("Clearing 3", "Clearing 13", "Clearing 9", "Clearing 29",
                                                   "Clearing 18", "Clearing 34", "Clearing 4"), world.player) and (
                                       state.has_all(("Clearing 20", "Clearing 33"), world.player) or
                                       state.has("Clearing 5", world.player)
                                   ))
                     )
        else:
            set_rule(world.get_location("Rob the Master of Frogs"),
                     lambda state: state.has("Clearing 26", world.player) and
                                   (state.has("Clearing 24", world.player) and (
                                           state.has_all(("Clearing 5", "Clearing 29", "Clearing 18", "Clearing 34",
                                                          "Clearing 4"), world.player) or
                                           state.has_all(("Clearing 17", "Clearing 12"), world.player)
                                   )) or
                                   (state.has_all(("Clearing 3", "Clearing 13", "Clearing 9", "Clearing 29",
                                                   "Clearing 18", "Clearing 34", "Clearing 4"), world.player) and (
                                            state.has_all(("Clearing 20", "Clearing 33"), world.player) or
                                            state.has("Clearing 5", world.player)
                                   ))
                     )

    # Set rules for extra locations, all of which need spellsanity for rules
    # Otherwise the player can get the spells from a vanilla location
    if world.options.extra_locations and world.options.spellsanity:
        set_rule(world.get_location("Game Over - Curse of the Birds"),
                 lambda state: state.has("Curse Spell Gem" , world.player))
        set_rule(world.get_location("Game Over - Dragged Down Into the River"),
                 lambda state: state.has("Ice Spell Gem" , world.player))
        set_rule(world.get_location("Game Over - The Master of Spiders Has No Friends"),
                 lambda state: state.has("Friendship Spell Gem" , world.player))

    # Set rules for spellsanity locations
    if world.options.spellsanity:

        trade_items = [
            "Wolf Amulet",
            "Spider Amulet",
            "Golden Magnet",
            "Violet Jewel",
            "Gold Chain"
        ]

        # These amulets all require you to be on Grimslade's quest which prevents you from using the
        # Eagle to go from 14 to 16, so logic gets messy. Easiest to only consider them outside clearingsanity
        # and just let them be used out of logic if the way is open
        if not world.options.clearingsanity:
            trade_items.extend([
            "Flower Amulet",
            "Bird Amulet",
            "Frog Amulet"
            ])

        for i in range(1, 7):
            # Require 2 items for logic for Halicar's shop since it's a long trip to get one at a time
            set_rule(world.get_location(f"Halicar's Shop {i}"),
                     lambda state: state.has_from_list_unique(trade_items, world.player, 2))

        # Similar to the extra_locations, the player just gets the vanilla Spell Gem outside spellsanity
        set_rule(world.get_location("Gift from the Master of Wolves"),
                 lambda state: state.has("Friendship Spell Gem", world.player))
        if not world.options.clearingsanity:
            set_rule(world.get_location("Rob the Master of Frogs"),
                    lambda state: state.has("Illusion Spell Gem", world.player))



    # Set rules for victory event locations
    set_rule(world.get_location("Give Antherica to Selator"), lambda state: state.has("Antherica Berry", world.player))
    set_rule(world.get_location("Give Map to Poomchukker"), lambda state: state.has("Map to Willowbend", world.player))
    if world.options.required_amulets.value > -1:
        set_rule(world.get_location("Give Amulets to Grimslade"), lambda state: state.has_from_list_unique((
            "Wolf Amulet",
            "Frog Amulet",
            "Bird Amulet",
            "Spider Amulet",
            "Flower Amulet"
        ), world.player, world.options.required_amulets.value))
    else:
        set_rule(world.get_location("Give Amulets to Grimslade"), lambda state: state.has_any((
            "Wolf Amulet",
            "Frog Amulet",
            "Bird Amulet",
            "Spider Amulet",
            "Flower Amulet"
        ), world.player))


def set_completion_condition(world: ScorpionSwampWorld) -> None:
    if world.options.goal == Goal.option_selator:
        world.multiworld.completion_condition[world.player] = lambda state: state.has(
            "Selator Victory", world.player
        )
    elif world.options.goal == Goal.option_poomchukker:
        world.multiworld.completion_condition[world.player] = lambda state: state.has(
            "Poomchukker Victory", world.player
        )
    elif world.options.goal == Goal.option_grimslade:
        world.multiworld.completion_condition[world.player] = lambda state: state.has(
            "Grimslade Victory", world.player
        )
    elif world.options.goal == Goal.option_any:
        world.multiworld.completion_condition[world.player] = lambda state: state.has_any((
            "Selator Victory",
            "Grimslade Victory",
            "Poomchukker Victory"
        ), world.player)
    elif world.options.goal == Goal.option_all:
        world.multiworld.completion_condition[world.player] = lambda state: state.has_all((
            "Selator Victory",
            "Grimslade Victory",
            "Poomchukker Victory"
        ), world.player)
