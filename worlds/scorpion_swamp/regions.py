from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ScorpionSwampWorld


def create_and_connect_regions(world: ScorpionSwampWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ScorpionSwampWorld) -> None:

    regions = [
        Region("Fenmarge", world.player, world.multiworld),
        Region("Willowbend", world.player, world.multiworld),
    ]

    regions.extend([
        Region(f"Clearing {i}", world.player, world.multiworld) for i in range(1, 36) if i not in {2, 22, 31}
    ])

    world.multiworld.regions += regions


def connect_regions(world: ScorpionSwampWorld) -> None:

    # Connect Fenmarge
    world.get_region("Fenmarge").connect(world.get_region("Clearing 1"), "Fenmarge to Clearing 1")

    # Connect Willowbend
    # You always need Clearing 10 to get to Willowbend so we don't need to check clearingsanity; we can always go back
    world.get_region("Willowbend").connect(world.get_region("Clearing 10"), "Willowbend to Clearing 10")

    # Connect Clearing 1
    connect_clearings(world, 1, [12, 4])

    # Connect Clearing 3
    connect_clearings(world, 3, [13, 21, 26])

    # Connect Clearing 4
    connect_clearings(world, 4, [34])
    # Clearing 1 doesn't ever have an item requirement
    world.get_region("Clearing 4").connect(world.get_region("Clearing 1"), "Clearing 4 to Clearing 1")

    # Connect Clearing 5
    connect_clearings(world, 5, [9, 29, 24])

    # Connect Clearing 6
    connect_clearings(world, 6, [18])

    # Connect Clearing 7
    connect_clearings(world, 7, [11, 30, 32, 15, 19])

    # Connect Clearing 8
    connect_clearings(world, 8, [26])

    # Connect Clearing 9
    connect_clearings(world, 9, [5, 13, 20])

    # Connect Clearing 10
    connect_clearings(world, 10, [28])
    # Willowbend doesn't ever have an item requirement
    world.get_region("Clearing 10").connect(world.get_region("Willowbend"), "Clearing 10 to Willowbend")

    # Connect Clearing 11
    connect_clearings(world, 11, [7])

    # Connect Clearing 12
    connect_clearings(world, 12, [17, 25])
    # Clearing 1 doesn't ever have an item requirement
    world.get_region("Clearing 12").connect(world.get_region("Clearing 1"), "Clearing 12 to Clearing 1")

    # Connect Clearing 13
    connect_clearings(world, 13, [9, 35, 3])

    # Connect Clearing 14
    connect_clearings(world, 14, [23])
    # Clearing 14 connects to 16 only if the goal is Selator or Poomchukker
    if world.options.goal.value in {1, 2}:
        world.get_region("Clearing 14").connect(world.get_region("Clearing 16"), "Clearing 14 to Clearing 16",
                               lambda state: state.has("Clearing 16", world.player))

    # Connect Clearing 15
    connect_clearings(world, 15, [19, 28, 7, 32])

    # Connect Clearing 16
    connect_clearings(world, 16, [35, 32, 30])

    # Connect Clearing 17
    connect_clearings(world, 17, [24, 12])

    # Connect Clearing 18
    connect_clearings(world, 18, [6, 29, 34])

    # Connect Clearing 19
    connect_clearings(world, 19, [27, 15, 32, 7])

    # Connect Clearing 20
    connect_clearings(world, 20, [33, 9])

    # Connect Clearing 21
    connect_clearings(world, 21, [3])

    # Connect Clearing 23
    connect_clearings(world, 23, [14, 29])

    # Connect Clearing 24
    connect_clearings(world, 24, [5, 26, 17])

    # Connect Clearing 25
    connect_clearings(world, 25, [12])

    # Connect Clearing 26
    connect_clearings(world, 26, [3, 8, 24])

    # Connect Clearing 27
    connect_clearings(world, 27, [19])

    # Connect Clearing 28
    connect_clearings(world, 28, [10, 15])

    # Connect Clearing 29
    connect_clearings(world, 29, [23, 33, 5, 18])

    # Connect Clearing 30
    connect_clearings(world, 30, [16, 7])

    # Connect Clearing 32
    connect_clearings(world, 32, [16, 15, 19, 7])

    # Connect Clearing 33
    connect_clearings(world, 33, [29, 20])

    # Connect Clearing 34
    connect_clearings(world, 34, [18, 4])

    # Connect Clearing 35
    connect_clearings(world, 35, [13, 16])

def connect_clearings(world: ScorpionSwampWorld, source: int, targets: list[int]):
    current_region = world.get_region(f"Clearing {source}")
    if world.options.clearingsanity:
        for target in targets:
            current_region.connect(world.get_region(f"Clearing {target}"),
                                   f"Clearing {source} to Clearing {target}",
                                   lambda state, t=target: state.has(f"Clearing {t}", world.player))
    else:
        for target in targets:
            current_region.connect(world.get_region(f"Clearing {target}"),
                                   f"Clearing {source} to Clearing {target}")