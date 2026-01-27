from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, ItemDict, Toggle


class Clearingsanity(Toggle):
    """
    Makes entering every clearing for the first time a location and adds items named "Clearing x" to
    the item pool where x is the clearing's number. These new items will be needed to access their respective
    clearing in the first place.
    """

    display_name = "Clearingsanity"


class Spellsanity(Toggle):
    """
    Adds all the places in the game where you can get Spell Gems as new locations and shuffles the
    vanilla Spell Gems into the item pool.
    """

    display_name = "Spellsanity"


class ExtraLocations(Toggle):
    """
    Adds additional locations for reaching all the bad endings in the game aside from running out of Stamina.

    If Progressive Statistics is on, this will be forced on as well.
    """

    display_name = "Extra Locations"


class ProgressiveStats(Toggle):
    """
    Adds additional items to the item pool that increase the minimum values of each of your stats at the beginning
    of each run. For example, if you have three Progressive Skill items your Skill will be in the range of 10-12
    instead of 7-12.
    """

    display_name = "Progressive Statistics"


class Goal(Choice):
    """
    The goal of the run.

    Selator/Poomchukker/Grimslade - Complete this quest in the game to win.

    Any - Any of the quests can be completed to win.

    All - All the quests must be separately completed to win.
    """

    display_name = "Goal"

    option_any = 0
    option_selator = 1
    option_poomchukker = 2
    option_grimslade = 3
    option_all = 4

    default = option_any

    alias_good = option_selator
    alias_neutral = option_poomchukker
    alias_evil = option_grimslade


class FillerWeights(ItemDict):
    """
    For any filler items that are added, these are the weights that each choice will be added. Any of the game's items
    can be added to this list if desired. Leave it as the default if you don't know what you're doing.

    If all weights are 0, the filler items will all be Stamina Spell Gems.
    """

    display_name = "Filler Weights"

    default = {
        "Skill Spell Gem" : 1,
        "Stamina Spell Gem" : 1,
        "Lucky Spell Gem" : 1
    }


@dataclass
class ScorpionSwampOptions(PerGameCommonOptions):
    goal : Goal
    clearingsanity : Clearingsanity
    spellsanity : Spellsanity
    extra_locations : ExtraLocations
    progressive_stats : ProgressiveStats
    filler_weights : FillerWeights


option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Goal, Clearingsanity, Spellsanity, ExtraLocations],
    ),
    OptionGroup(
        "Item Options",
        [ProgressiveStats, FillerWeights],
    ),
]

option_presets = {
    "maximum randomization": {
        "goal": Goal.option_all,
        "clearingsanity": True,
        "spellsanity": True,
        "extra_locations": True,
        "progressive_stats": True,
        "filler_weights": FillerWeights.default,
    },
}
