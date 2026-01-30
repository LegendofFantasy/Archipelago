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

    # No additional rules are needed for common or clearingsanity locations

    # Set rules for extra locations
    if world.options.extra_locations:
        set_rule(world.get_location("Game Over - Curse of the Birds"),
                 lambda state: state.has("Curse Spell Gem" , world.player))
        set_rule(world.get_location("Game Over - Dragged Down Into the River"),
                 lambda state: state.has("Ice Spell Gem" , world.player))
        set_rule(world.get_location("Game Over - The Master of Spiders Has No Friends"),
                 lambda state: state.has("Friendship Spell Gem" , world.player))

    # Set rules for spellsanity locations
    if world.options.spellsanity:
        for i in range(1, 7):
            set_rule(world.get_location(f"Halicar's Shop {i}"),
                     lambda state: state.has_from_list_unique((
                         "Wolf Amulet",
                         "Frog Amulet",
                         "Bird Amulet",
                         "Spider Amulet",
                         "Flower Amulet",
                         "Golden Magnet",
                         "Violet Jewel",
                         "Gold Chain"
                     ), world.player, 3))
            # Require 3 items for logic for Halicar's shop since it's a long trip to get one at a time

    # Set rules for non-victory event locations
    set_rule(world.get_location("Rob the Master of Frogs"), lambda state: state.has("Illusion Spell Gem", world.player))

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
