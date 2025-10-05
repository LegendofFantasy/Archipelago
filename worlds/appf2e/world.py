from collections.abc import Mapping
from typing import Any
import settings

from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world, data


class APPF2eSettings(settings.Group):
    class ConnectionsDirectory(settings.UserFolderPath):
        """Path to the connections folder which is found in the game folder at your game's install location."""
        description = "AP Pathfinder 2e connections Directory"

    connections_directory: ConnectionsDirectory = ConnectionsDirectory("")


# The world class is the heart and soul of an apworld implementation.
# It holds all the data and functions required to build the world and submit it to the multiworld generator.
# You could have all your world code in just this one class, but for readability and better structure,
# it is common to split up world functionality into multiple files.
# This implementation in particular has the following additional files, each covering one topic:
# regions.py, locations.py, rules.py, items.py, options.py and web_world.py.
# It is recommended that you read these in that specific order, then come back to the world class.
class APPF2eWorld(World):
    """
    AP Pathfinder 2e is a game that randomly generates a dungeon for you to go through, fighting randomly generated
    encounters using a randomly generated party of characters, all using the Pathfinder 2e system.
    """

    game = "AP Pathfinder 2e"

    web = web_world.APPF2eWebWorld()

    options_dataclass = options.APPF2eOptions
    options: options.APPF2eOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    keys_used = []

    def generate_early(self) -> None:

        # Fix any options that are going to cause issues by being too high or low
        if self.options.number_of_keys.value >= self.options.number_of_rooms.value:
            self.options.number_of_keys.value = self.options.number_of_rooms.value - 1

        if self.options.maximum_level.value < self.options.minimum_level.value:
            self.options.maximum_level.value = self.options.minimum_level.value

        if self.options.maximum_difficulty.value < self.options.minimum_difficulty.value:
            self.options.maximum_difficulty.value = self.options.minimum_difficulty.value

        # Select the keys to be used for this generation
        self.keys_used = self.random.sample(data.KEY_NAMES, self.options.number_of_keys)


    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self, self.keys_used)

    def create_item(self, name: str) -> items.APPF2eItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
        )
