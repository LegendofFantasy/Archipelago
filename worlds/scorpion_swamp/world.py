from collections.abc import Mapping
from typing import Any

from BaseClasses import MultiWorld
from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as scorpion_swamp_options

class ScorpionSwampWorld(World):
    """
    Scorpion Swamp is a gamebook in the Fighting Fantasy series. Journey into the titular swamp to complete one of
    three quests given by one of three wizards. Only YOU can brave the Scorpion Swamp!
    """

    game = "Scorpion Swamp"

    web = web_world.ScorpionSwampWebWorld()

    options_dataclass = scorpion_swamp_options.ScorpionSwampOptions
    options: scorpion_swamp_options.ScorpionSwampOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    location_name_groups = locations.LOCATION_NAME_GROUPS
    item_name_to_id = items.ITEM_NAME_TO_ID
    item_name_groups = items.ITEM_NAME_GROUPS

    origin_region_name = "Fenmarge"

    ut_can_gen_without_yaml = True

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

        self.starting_wizard = ""

    def generate_early(self) -> None:

        if self.options.wizardsanity:
            self.starting_wizard = self.random.choice(["Selator", "Poomchukker", "Grimslade"])

        # Universal Tracker Support
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data = re_gen_passthrough[self.game]

            self.options.goal.value = slot_data["goal"]
            self.options.required_amulets.value = slot_data["required_amulets"]
            self.options.clearingsanity.value = slot_data["clearingsanity"]
            self.options.spellsanity.value = slot_data["spellsanity"]
            self.options.extra_locations.value = slot_data["extra_locations"]
            self.options.wizardsanity.value = slot_data["wizardsanity"]
            self.starting_wizard = slot_data["starting_wizard"]

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

    def create_item(self, name: str) -> items.ScorpionSwampItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        data =  self.options.as_dict(
            "goal", "required_amulets", "clearingsanity", "spellsanity", "wizardsanity", "extra_locations"
        )
        data["starting_wizard"] = self.starting_wizard
        return data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a regen in UT
        return slot_data
