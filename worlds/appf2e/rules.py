from __future__ import annotations

from typing import TYPE_CHECKING

from ..generic.Rules import set_rule

if TYPE_CHECKING:
    from .world import APPF2eWorld

def requirements_by_level(world: APPF2eWorld, level: int) -> dict:

    requirements = {
        "Level Up" : 0,
        "Progressive Weapon Rune" : 0,
        "Progressive Armor Rune" : 0,
        "Apex Items Token" : 0
    }

    if level >= 2:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Weapon Rune"] += 1
    if level >= 3:
        requirements["Level Up"] += 1
    if level >= 4:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Weapon Rune"] += 1
    if level >= 5:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Armor Rune"] += 1
    if level >= 6:
        requirements["Level Up"] += 1
    if level >= 7:
        requirements["Level Up"] += 1
    if level >= 8:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Armor Rune"] += 1
    if level >= 9:
        requirements["Level Up"] += 1
    if level >= 10:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Weapon Rune"] += 1
    if level >= 11:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Armor Rune"] += 1
    if level >= 12:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Weapon Rune"] += 1
    if level >= 13:
       requirements["Level Up"] += 1
    if level >= 14:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Armor Rune"] += 1
    if level >= 15:
        requirements["Level Up"] += 1
    if level >= 16:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Weapon Rune"] += 1
    if level >= 17:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Apex Items Token"] += 1
    if level >= 18:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Armor Rune"] += 1
    if level >= 19:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Weapon Rune"] += 1
    if level >= 20:
        requirements["Level Up"] += 1
        if not world.options.use_abp: requirements["Progressive Armor Rune"] += 1

    return requirements


def set_all_rules(world: APPF2eWorld) -> None:

    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: APPF2eWorld) -> None:

    level_requirements = {level : requirements_by_level(world, level) for level in range(1, 21)}

    for room in world.rooms:
        level = world.rooms[room]["Level"]

        if not room == "Boss Room":
            for letter in "ABCDE":
                set_rule(world.get_location(f"{room} {letter}"),
                         lambda state, l=level: state.has_all_counts(level_requirements[l], world.player))
        else:
            for letter in world.rooms[room]["Locations Needed"]:
                set_rule(world.get_location(f"{room} {letter}"),
                         lambda state, l=level: state.has_all_counts(level_requirements[l], world.player))

            set_rule(world.get_location("Final Boss Defeated"),
                     lambda state, l=level: state.has_all_counts(level_requirements[l], world.player))


def set_completion_condition(world: APPF2eWorld) -> None:

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
