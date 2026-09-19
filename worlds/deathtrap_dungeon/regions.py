from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .options import Trialmastersanity, Championsanity, ExtraLocks, GemHunt

if TYPE_CHECKING:
    from .world import DeathtrapDungeonWorld


def create_and_connect_regions(world: DeathtrapDungeonWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: DeathtrapDungeonWorld) -> None:

    regions = [
        Region(region, world.player, world.multiworld) for region in {
            "Fang",
            "Entrance Area",
            "Barbarian's Room",
            "Pre-Throm Area",
            "Horath's Room",
            "Ian's Room",
            "Throm's Area",
            "Torgrim's Trial and the Troglodytes",
            "Servant's Encounter",
            "North Past Torgrim",
            "Far West Past Torgrim",
            "Past the Brass Key Door",
            "Elf's Room",
            "Past the Iron Key Door",
            "North Routes' Convergence",
            "Thomas's Encounter",
            "Ivy through Pre-Ninja Encounter",
            "Ninja's Encounter",
            "Bloodbeast and Manticore Encounters",
            "Igbut's Encounter",
            "Return to Fang"
        }
    ]

    world.multiworld.regions += regions


def connect_regions(world: DeathtrapDungeonWorld) -> None:

    connect(world, "Fang", "Entrance Area", "Entering Deathtrap Dungeon")
    connect(world, "Entrance Area", "Barbarian's Room", "Barbarian's Door",
            Has("Barbarian") | OptionFilter(Championsanity, False))
    connect(world, "Entrance Area", "Pre-Throm Area", "Entrance Area to Pre-Throm Area",
            Has("Copper Key") | OptionFilter(ExtraLocks, False))
    connect(world, "Pre-Throm Area", "Horath's Room", "Horath's Door",
            Has("Horath") | OptionFilter(Trialmastersanity, False))
    connect(world, "Pre-Throm Area", "Ian's Room", "Ian's Door",
            Has("Ian Livingstone") | OptionFilter(Trialmastersanity, False))
    connect(world, "Pre-Throm Area", "Throm's Area", "Encounter Throm",
            Has("Throm") | OptionFilter(Championsanity, False))
    connect(world, "Throm's Area", "Torgrim's Trial and the Troglodytes", "Torgrim's Door",
            Has("Torgrim") | OptionFilter(Trialmastersanity, False))
    connect(world, "Torgrim's Trial and the Troglodytes", "Servant's Encounter", "Meet the Servant",
            Has("Servant of the Trialmasters") | OptionFilter(Trialmastersanity, False))
    connect(world, "Torgrim's Trial and the Troglodytes", "North Past Torgrim",
            "Head North After the Trial", Has("Brass Key") | OptionFilter(ExtraLocks, False))
    connect(world, "North Past Torgrim", "North Routes' Convergence", "Continue North")
    connect(world, "North Past Torgrim", "Past the Brass Key Door", "Open the North Brass Key Door")
    connect(world, "North Routes' Convergence", "Bloodbeast and Manticore Encounters", "North Chute")
    connect(world, "Torgrim's Trial and the Troglodytes", "Far West Past Torgrim",
            "Head West After the Trial", Has("Brass Key") | OptionFilter(ExtraLocks, False))
    connect(world, "Far West Past Torgrim", "Bloodbeast and Manticore Encounters", "West Chutes")
    connect(world, "Far West Past Torgrim", "Past the Brass Key Door",
            "Open the West Brass Key Door")
    connect(world, "Torgrim's Trial and the Troglodytes", "Elf's Room", "Elf's Door",
            Has("Elf") | OptionFilter(Championsanity, False))
    connect(world, "Torgrim's Trial and the Troglodytes", "Past the Iron Key Door", "Iron Key Door",
            Has("Iron Key"))
    connect(world, "Past the Iron Key Door", "North Routes' Convergence",
            "Don't Go Up in the Basket")
    connect(world,"Past the Iron Key Door", "Thomas's Encounter", "Talk to Thomas",
            Has("Thomas") | OptionFilter(Trialmastersanity, False))
    connect(world, "Thomas's Encounter", "Ivy through Pre-Ninja Encounter", "Go Up In the Basket",
            Has("Ivy") | OptionFilter(Trialmastersanity, False))
    connect(world, "Ivy through Pre-Ninja Encounter", "Ninja's Encounter", "Fight the Ninja",
            Has("Ninja") | OptionFilter(Championsanity, False))
    connect(world, "Ninja's Encounter", "Bloodbeast and Manticore Encounters", "Post-Ninja Chute")
    connect(world, "Bloodbeast and Manticore Encounters", "Igbut's Encounter", "Talk to Igbut",
            Has("Igbut") | OptionFilter(Trialmastersanity, False))
    connect(world, "Igbut's Encounter", "Return to Fang", "Pass the Final Trial",
            HasAll("Emerald", "Diamond", "Sapphire") & (
                    HasAll("Pearl", "Topaz", "Ruby", "Garnet") | OptionFilter(GemHunt, False))
            )


def connect(world: DeathtrapDungeonWorld, source: str, target: str, name: str, rule: Rule = None) -> None:
    world.get_region(source).connect(world.get_region(target), name, rule)