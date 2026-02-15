from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class ScorpionSwampWebWorld(WebWorld):

    game = "Scorpion Swamp"

    theme = "dirt"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Scorpion Swamp for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["LegendofFantasy"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
