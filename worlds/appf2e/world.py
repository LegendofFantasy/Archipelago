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
    starting = {
        "Ancestries" : "",
        "Backgrounds" : "",
        "Classes" : "",
        "Weapons" : "",
        "Armors" : "",
        "Shields" : ""
    }

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

        # Select random Ancestries
        ancestries = []

        if self.options.ancestry_blacklist.value:
            if "_Common" not in self.options.ancestry_blacklist.value:
                ancestries.extend(data.COMMON_ANCESTRIES)
            if "_Uncommon" not in self.options.ancestry_blacklist.value:
                ancestries.extend(data.UNCOMMON_ANCESTRIES)
            if "_Rare" not in self.options.ancestry_blacklist.value:
                ancestries.extend(data.RARE_ANCESTRIES)
            for ancestry in self.options.ancestry_blacklist.value:
                if ancestry in ancestries:
                    ancestries.remove(ancestry)
        # Catches both the no blacklist case and the case where the blacklist blocks everything
        if not ancestries:
            ancestries.extend(data.COMMON_ANCESTRIES + data.UNCOMMON_ANCESTRIES + data.RARE_ANCESTRIES)

        # Keep the chosen ancestries unique if there are enough options, otherwise choose anything
        if len(ancestries) >= 4:
            ancestries = self.random.sample(ancestries, 4)
        else:
            ancestries = self.random.choices(ancestries, k=4)

        if self.options.randomize_heritage:
            names = ancestries.copy()
            ancestries.clear()

            for name in names:
                ancestries.append(self.random.sample(data.ANCESTRIES[name], 1))

        self.starting["Ancestries"] = f"{ancestries[0]}, {ancestries[1]}, {ancestries[2]}, and {ancestries[3]}"

        # Select random Backgrounds
        backgrounds = []

        if self.options.background_blacklist.value:
            for background in data.BACKGROUNDS:
                if data.BACKGROUNDS[background]["name"] in self.options.background_blacklist.value:
                    continue
                if (data.BACKGROUNDS[background]["rarity"] == "Common" and
                        "_Common" in self.options.background_blacklist.value):
                    continue
                if (data.BACKGROUNDS[background]["rarity"] == "Uncommon" and
                        "_Uncommon" in self.options.background_blacklist.value):
                    continue
                if (data.BACKGROUNDS[background]["rarity"] == "Rare" and
                        "_Rare" in self.options.background_blacklist.value):
                    continue
                backgrounds.append(data.BACKGROUNDS[background]["name"])

        if not backgrounds:
            backgrounds.extend(data.BACKGROUNDS[background]["name"] for background in data.BACKGROUNDS)

        if len(backgrounds) >= 4:
            backgrounds = self.random.sample(backgrounds, 4)
        else:
            backgrounds = self.random.choices(backgrounds, k=4)

        self.starting["Backgrounds"] = f"{backgrounds[0]}, {backgrounds[1]}, {backgrounds[2]}, and {backgrounds[3]}"

        # Select random Classes
        classes = []

        if self.options.class_blacklist.value:
            for class_name in data.CLASSES:
                if class_name in self.options.class_blacklist.value:
                    continue
                classes.append(class_name)

        if not classes:
            classes.extend(data.CLASSES.keys())

        if len(classes) >= 4:
            classes = self.random.sample(classes, 4)
        else:
            classes = self.random.choices(classes, k=4)

        if self.options.randomize_subclass:
            names = classes.copy()
            classes.clear()

            for name in names:
                classes.append(self.random.sample(data.CLASSES[name], 1))

        self.starting["Classes"] = f"{classes[0]}, {classes[1]}, {classes[2]}, and {classes[3]}"

        # Select starting equipment
        self.starting["Weapons"] = ", ".join(self.random.sample(
            [data.WEAPONS[weapon]["name"] for weapon in data.WEAPONS], 4 + self.options.extra_weapons.value))
        self.starting["Armors"] = ", ".join(self.random.sample(
            [data.ARMORS[armor]["name"] for armor in data.ARMORS], 4 + self.options.extra_armors.value))
        self.starting["Shields"] = ", ".join(self.random.sample(
            [data.SHIELDS[shield]["name"] for shield in data.SHIELDS], self.options.starting_shields.value))


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

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data =  self.options.as_dict(
            "strict_logic",
            "use_abp"
        )

        slot_data["Ancestries"] = self.starting["Ancestries"]
        slot_data["Backgrounds"] = self.starting["Backgrounds"]
        slot_data["Classes"] = self.starting["Classes"]
        slot_data["Weapons"] = self.starting["Weapons"]
        slot_data["Shields"] = self.starting["Shields"]
        slot_data["Armors"] = self.starting["Armors"]

        return slot_data
