from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import APPF2eWorld

def create_and_connect_regions(world: APPF2eWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: APPF2eWorld) -> None:

    world.multiworld.regions += [Region(room_name, world.player, world.multiworld) for room_name in world.rooms]


def connect_regions(world: APPF2eWorld) -> None:

    for room in world.rooms:
        doors = world.rooms[room]["Doors"]
        keys = world.rooms[room]["Keys"]
        for i in len(doors):
            if keys[i]:
                world.get_region(room).connect(doors[i], f"{room} to {doors[i]}",
                                               lambda state, j=i: state.has(keys[j], world.player))
            else:
                world.get_region(room).connect(doors[i], f"{room} to {doors[i]}")
