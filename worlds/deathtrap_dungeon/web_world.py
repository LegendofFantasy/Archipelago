from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class DeathtrapDungeonWebWorld(WebWorld):

    game = "Deathtrap Dungeon"

    theme = "stone"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Deathtrap Dungeon for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["LegendofFantasy"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
