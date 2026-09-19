from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, Rule
from .options import SimplifyNinja

if TYPE_CHECKING:
    from .world import DeathtrapDungeonWorld


def set_all_rules(world: DeathtrapDungeonWorld) -> None:

    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: DeathtrapDungeonWorld) -> None:

    # Set the rules for always-present locations; other rules are handled by region access
    set_location_rule(world, "Shop in the Tunnel", Has("Gold Piece"))

    # Set the rules for championsanity
    if world.options.championsanity:
        set_location_rule(world, "Meeting the Knight", Has("Knight"))

    # Set the rules for simplify_ninja adding an item
    if world.options.simplify_ninja.value == SimplifyNinja.option_item:
        set_location_rule(world, "Taking the Ninja's Weapons", Has("Ninja's Weapons"))


def set_location_rule(world: DeathtrapDungeonWorld, name: str, rule: Rule) -> None:
    world.set_rule(world.get_location(name), rule)


def set_completion_condition(world: DeathtrapDungeonWorld) -> None:
    world.set_completion_rule(Has("Victory"))
