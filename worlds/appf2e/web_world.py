from BaseClasses import Tutorial

from worlds.AutoWorld import WebWorld

from .options import option_groups


class APPF2eWebWorld(WebWorld):
    game = "AP Pathfinder 2e"

    theme = "stone"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up AP Pathfinder 2e for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["LegendofFantasy"],
    )

    tutorials = [setup_en]

    # If we have option groups and/or option presets, we need to specify these here as well.
    option_groups = option_groups
    #options_presets = option_presets
