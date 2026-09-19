from collections.abc import Mapping
from typing import Any, ClassVar

from BaseClasses import MultiWorld
from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as deathtrap_dungeon_options

class DeathtrapDungeonWorld(World):
    """
    Scorpion Swamp is a gamebook in the Fighting Fantasy series. Journey into the titular swamp to complete one of
    three quests given by one of three wizards. Only YOU can brave the Scorpion Swamp!
    """

    game = "Deathtrap Dungeon"

    web = web_world.DeathtrapDungeonWebWorld()

    options_dataclass = deathtrap_dungeon_options.DeathtrapDungeonOptions
    options: deathtrap_dungeon_options.DeathtrapDungeonOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    location_name_groups = locations.LOCATION_NAME_GROUPS
    item_name_to_id = items.ITEM_NAME_TO_ID
    item_name_groups = items.ITEM_NAME_GROUPS

    origin_region_name = "Fang"

    ut_can_gen_without_yaml = True
    tracker_world: ClassVar[dict[str, Any]] = {
        "map_page_folder": "tracker",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": "locations/locations.json",
        "map_page_groups": [('Main', ['main'])],
    }

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

    def generate_early(self) -> None:

        # Universal Tracker Support
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data = re_gen_passthrough[self.game]

            self.options.gem_hunt.value = slot_data["gem_hunt"]
            self.options.shuffle_shield.value = slot_data["shuffle_shield"]
            self.options.shuffle_potion.value = slot_data["shuffle_potion"]
            self.options.trialmastersanity.value = slot_data["trialmastersanity"]
            self.options.championsanity.value = slot_data["championsanity"]
            self.options.extra_locks.value = slot_data["extra_locks"]
            self.options.extra_locations.value = slot_data["extra_locations"]
            self.options.simplify_ninja.value = slot_data["simplify_ninja"]

        # Sanitize options
        if self.options.progressive_stats and not self.options.extra_locations:
            self.options.extra_locations.value = True

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.DeathtrapDungeonItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        data =  self.options.as_dict(
            "gem_hunt", "shuffle_shield", "shuffle_potion", "trialmastersanity",
            "championsanity", "extra_locks", "extra_locations", "pack_size", "simplify_ninja"
        )
        return data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a regen in UT
        return slot_data
