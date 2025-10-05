from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, OptionSet

from . import data


class StrictLogic(DefaultOnToggle):
    """
    With strict logic the game will not allow the player to fight enemies who logically require a higher level or
    more weapon or armor runes. With this setting off, the player is free to fight any enemies that they can reach.
    """

    display_name = "Strict Logic"


class NumberOfRooms(Range):
    """
    Determines the number of rooms in the dungeon. This includes the final boss room. Setting this value low can
    cause issues with generation with large level ranges in single game worlds.
    """

    display_name = "Number of Rooms"

    range_start = 2
    range_end = 20
    default = 5


class NumberOfKeys(Range):
    """
    Determines the number of keys that lock doors in the dungeon. This should be lower than the number of rooms and if
    it is not will automatically be set to one less than the number of rooms.
    """

    display_name = "Number of Keys"

    range_start = 0
    range_end = 19
    default = 0


class StartingLevel(Range):
    """
    Determines what the starting level for the characters in the game will be.
    """

    display_name = "Starting Level"

    range_start = 1
    range_end = 20
    default = 1


class MaximumLevel(Range):
    """
    Determines what the maximum level that the characters will reach will be. This will be the level at which you will
    fight the final boss. This should be equal to or higher than the starting level and will be set equal to the
    starting level if it is not.
    """

    display_name = "Maximum Level"

    range_start = 1
    range_end = 20
    default = 1


class UseABP(Toggle):
    """
    With Automatic Bonus Progression on, your characters will be expected to be using the variant rule of the same
    name. This will remove progressive weapon and armor runes from the game and logic will no longer expect you to
    have them.
    """

    display_name = "Use Automatic Bonus Progression"


class BossEncounter(Choice):
    """
    Determines the specifications for the boss encounter found in the final room. This will ignore other settings that
    determine difficulty.

    - Trivial: The boss will be a Trivial budget fight.
    - Low: The boss will be a Low budget fight.
    - Moderate: The boss will be a Moderate budget fight.
    - Severe: The boss will be a Severe budget fight.
    - Extreme: The boss will be an Extreme budget fight, but won't necessarily be a solo boss like in Plus4. This can
    still be very difficult at lower levels.
    - Plus4: The boss will be a single creature four levels higher than the characters. This will be more manageable
    than Plus5 but will still be potentially extremely difficult at lower levels.
    - Plus5: The boss will be a single creature five levels higher than the characters. This will likely prove
    extremely difficult, especially at lower levels. Use with caution!
    """

    display_name = "Boss Encounter"

    option_trivial = 0
    option_low = 1
    option_moderate = 2
    option_severe = 3
    option_extreme = 4
    option_plus4 = 5
    option_plus5 = 6

    default = option_moderate


class MinimumDifficulty(Choice):
    """
    Determines the minimum difficulty that the encounters will be. Keep in mind that Severe and Extreme encounters can
    be very challenging at lower levels.
    """

    display_name = "Minimum Encounter Difficulty"

    option_trivial = 0
    option_low = 1
    option_moderate = 2
    option_severe = 3
    option_extreme = 4

    default = option_trivial


class MaximumDifficulty(Choice):
    """
    Determines the maximum difficulty that the encounters will be. Keep in mind that Severe and Extreme encounters can
    be very challenging at lower levels. This should be a higher difficulty than the minimum difficulty and if it isn't,
    it will be automatically set to the same as the minimum difficulty.
    """

    display_name = "Maximum Encounter Difficulty"

    option_trivial = 0
    option_low = 1
    option_moderate = 2
    option_severe = 3
    option_extreme = 4

    default = option_severe


class RandomizeHeritage(Toggle):
    """
    If this is on, the randomly generated Ancestries will also include a pre-selected random heritage. If this is off,
    you will only receive a list of random Ancestries with the heritages being up to you.
    """

    display_name = "Randomize Heritage"


class RandomizeSubclass(Toggle):
    """
    If this is on, the randomly generated classes will also include a pre-selected random subclass where applicable. If
    this is off, you will only receive a list of random classes with the subclasses being up to you.
    """

    display_name = "Randomize Subclass"


class AncestryBlacklist(OptionSet):
    """
    This prevents any Ancestries listed here from being randomly selected.

    Use "_Common", "_Uncommon", or "_Rare" as a shortcut for all Ancestries of that rarity.
    """

    display_name = "Ancestry Blacklist"

    valid_keys = (["_Common", "_Uncommon", "_Rare"]
                  + sorted(data.COMMON_ANCESTRIES + data.UNCOMMON_ANCESTRIES + data.RARE_ANCESTRIES))


class BackgroundBlacklist(OptionSet):
    """
    This prevents any Backgrounds listed here from being randomly selected.

    Use "_Common", "_Uncommon", or "_Rare" as a shortcut for all Backgrounds of that rarity.
    """

    display_name = "Background Blacklist"

    valid_keys = (["_Common", "_Uncommon", "_Rare"]
                  + sorted(data.BACKGROUNDS[background]["name"] for background in data.BACKGROUNDS))


class ClassBlacklist(OptionSet):
    """
    This prevents any Classes listed here from being randomly selected.
    """

    display_name = "Class Blacklist"

    valid_keys = sorted(class_name for class_name in data.CLASSES)


class ExtraWeapons(Range):
    """
    Determines how many extra weapons you will start with. The base amount is 4 and this amount is added to that.
    """

    display_name = "Extra Starting Weapons"

    range_start = 0
    range_end = 20
    default = 0


class ExtraArmors(Range):
    """
    Determines how many extra armors you will start with. The base amount is 4 and this amount is added to that.
    """

    display_name = "Extra Starting Armors"

    range_start = 0
    range_end = 10
    default = 0


class StartingShields(Range):
    """
    Determines how many shields you start with. There is no base amount so this amount alone determines how many you
    get.
    """

    display_name = "Starting Shields"

    range_start = 0
    range_end = 10
    default = 2


class ValidCreatureTraits(OptionSet):
    """
    Only creatures with these traits will be able to appear in random encounters. Leaving this empty is the same as
    allowing every trait.

    If you only allow a small number of traits then there may be issues creating encounters at certain level ranges.
    If this happens, this will be reverted to allowing all traits.
    """

    display_name = "Valid Creature Traits"

    valid_keys = sorted(data.TRAITS)


class CreatureTraitBlacklist(OptionSet):
    """
    This prevents any creatures with traits listed here from appearing in random encounters. The default settings
    block the Unique and Mythic traits because the former are typically NPCs from prewritten adventures and as such are
    blocked to avoid spoilers while the latter require you to be playing with the Mythic variant rules. Feel free to
    enable these traits if you wish. Note: If you have a maximum level of 20 and have set your boss to be Plus5, you
    must enable at least Unique as currently all Level 25 creatures have that trait.
    """

    display_name = "Creature Trait Blacklist"

    valid_keys = sorted(data.TRAITS)

    default = {"Unique", "Mythic"}


class BlockAPCreatures(DefaultOnToggle):
    """
    With this on, all creatures that have only appeared in the prewritten Adventure Paths will be prevented from
    appearing in random encounters.
    """

    display_name = "Block Adventure Path Creatures"


class IncludeHeroPoints(Toggle):
    """
    With this on, an item that provides one Hero Point to each of your characters will be added as a potential filler
    item.
    """

    display_name = "Include Hero Points"


class IncludeAncestryFeatTokens(Toggle):
    """
    With this on, an item that can be redeemed for a bonus Ancestry feat for one of your characters will be added as a
    potential filler item.
    """

    display_name = "Include Ancestry Feat Tokens"


class IncludeGeneralFeatTokens(Toggle):
    """
    With this on, an item that can be redeemed for a bonus General feat for one of your characters will be added as a
    potential filler item.
    """

    display_name = "Include General Feat Tokens"


class IncludeSkillTrainingTokens(Toggle):
    """
    With this on, an item that can be redeemed for a bonus skill training for one of your characters will be added as a
    potential filler item.
    """

    display_name = "Include Skill Training Tokens"


class IncludeExplorationActivities(Toggle):
    """
    With this on, items that unlock various exploration activities will be added to the item pool.
    """

    display_name = "Include Exploration Activities"


@dataclass
class APPF2eOptions(PerGameCommonOptions):
    strict_logic: StrictLogic
    number_of_rooms: NumberOfRooms
    number_of_keys: NumberOfKeys
    starting_level: StartingLevel
    maximum_level: MaximumLevel
    use_abp: UseABP
    boss_encounter: BossEncounter
    minimum_difficulty: MinimumDifficulty
    maximum_difficulty: MaximumDifficulty
    randomize_heritage: RandomizeHeritage
    randomize_subclass: RandomizeSubclass
    ancestry_blacklist: AncestryBlacklist
    background_blacklist: BackgroundBlacklist
    class_blacklist: ClassBlacklist
    extra_weapons: ExtraWeapons
    extra_armors: ExtraArmors
    starting_shields: StartingShields
    valid_creatures: ValidCreatureTraits
    creature_blacklist: CreatureTraitBlacklist
    block_ap_creatures: BlockAPCreatures
    include_hero_points: IncludeHeroPoints
    include_ancestry_feat_tokens: IncludeAncestryFeatTokens
    include_general_feat_tokens: IncludeGeneralFeatTokens
    include_skill_training_tokens: IncludeSkillTrainingTokens
    include_exploration_activities: IncludeExplorationActivities


option_groups = [
    OptionGroup(
        "Dungeon Options",
        [NumberOfRooms, NumberOfKeys, StartingLevel, MaximumLevel, UseABP,
         BossEncounter, MinimumDifficulty, MaximumDifficulty, StrictLogic],
    ),
    OptionGroup(
        "Character Options",
        [RandomizeHeritage, RandomizeSubclass, AncestryBlacklist, BackgroundBlacklist, ClassBlacklist,
         ExtraWeapons, ExtraArmors, StartingShields],
    ),
    OptionGroup(
        "Creature Options",
        [ValidCreatureTraits, CreatureTraitBlacklist, BlockAPCreatures],
    ),
    OptionGroup(
        "Extra Item Options",
        [IncludeHeroPoints, IncludeAncestryFeatTokens, IncludeGeneralFeatTokens, IncludeSkillTrainingTokens,
         IncludeExplorationActivities],
    )
]

