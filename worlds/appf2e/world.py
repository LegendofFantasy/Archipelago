from collections.abc import Mapping
from typing import Any
import json

from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world, data


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

    origin_region_name = "Room 1"

    
    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.keys_used = []
        self.starting = {
            "Ancestries" : "",
            "Backgrounds" : "",
            "Classes" : "",
            "Weapons" : "",
            "Armors" : "",
            "Shields" : ""
        }
        self.rooms = {
            "Room 1" : {
                "Level": 1,
                "Difficulty": "",
                "Creatures": [],
                "Doors": [],
                "Keys": []
            }
        }

    def generate_early(self) -> None:

        # Universal Tracker Support
        slot_data: dict[str, Any] = {}
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data = re_gen_passthrough[self.game]

        # Fix any options that are going to cause issues by being too high or low
        if self.options.number_of_keys.value >= self.options.number_of_rooms.value:
            self.options.number_of_keys.value = int(self.options.number_of_rooms.value) - 1

        if self.options.maximum_level.value < self.options.starting_level.value:
            self.options.maximum_level.value = int(self.options.starting_level.value)

        if self.options.maximum_difficulty.value < self.options.minimum_difficulty.value:
            self.options.maximum_difficulty.value = int(self.options.minimum_difficulty.value)

        # Select the keys to be used for this generation
        self.keys_used = self.random.sample(sorted(data.KEY_NAMES), int(self.options.number_of_keys.value))

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
                new_ancestry = self.random.choice(data.ANCESTRIES[name])
                if "VH" in new_ancestry:
                    new_ancestry = new_ancestry.replace("VH", self.random.choice(data.VERSATILE_HERITAGES))
                ancestries.append(new_ancestry)

        self.starting["Ancestries"] = ", ".join(ancestries)

        # Select random Backgrounds
        backgrounds = []

        if self.options.background_blacklist.value:
            for background in data.BACKGROUNDS:
                if background["name"] in self.options.background_blacklist.value:
                    continue
                if (background["rarity"] == "Common" and
                        "_Common" in self.options.background_blacklist.value):
                    continue
                if (background["rarity"] == "Uncommon" and
                        "_Uncommon" in self.options.background_blacklist.value):
                    continue
                if (background["rarity"] == "Rare" and
                        "_Rare" in self.options.background_blacklist.value):
                    continue
                backgrounds.append(background["name"])

        if not backgrounds:
            backgrounds.extend(background["name"] for background in data.BACKGROUNDS)

        if len(backgrounds) >= 4:
            backgrounds = self.random.sample(backgrounds, 4)
        else:
            backgrounds = self.random.choices(backgrounds, k=4)

        self.starting["Backgrounds"] = ", ".join(backgrounds)

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
                classes.append(self.random.choice(data.CLASSES[name]))

        self.starting["Classes"] = ", ".join(classes)

        # Select starting equipment
        self.starting["Weapons"] = ", ".join(self.random.sample(
            [weapon["name"] for weapon in data.WEAPONS], 4 + int(self.options.extra_weapons.value)))
        self.starting["Armors"] = ", ".join(self.random.sample(
            [armor["name"] for armor in data.ARMORS], 4 + int(self.options.extra_armors.value)))
        self.starting["Shields"] = ", ".join(self.random.sample(
            [shield["name"] for shield in data.SHIELDS], int(self.options.starting_shields.value)))

        # Make a list of valid enemy creatures
        valid_creatures = []
        # Keep track of what levels we have creatures of
        added_levels = {level : False for level in range(max(self.options.starting_level.value - 4, -1),
                                                         self.options.maximum_level.value + 5)}

        for creature in data.CREATURES:

            # Discard any creatures that are from APs if the setting to do so is on
            if self.options.block_ap_creatures and creature["source"].startswith("Pathfinder #"):
                continue

            # Discard any creatures that don't have correct traits
            blacklisted = False
            valid = False

            for trait in self.options.creature_blacklist.value:
                if trait in creature["trait"]:
                    blacklisted = True
                    break

            for trait in self.options.valid_creatures.value:
                if trait in creature["trait"]:
                    valid = True
                    break

            if blacklisted or (not valid and self.options.valid_creatures.value):
                continue

            # Discard any creatures that aren't relevant to the level range
            level = int(creature["level"])

            if level not in added_levels.keys():
                continue

            valid_creatures.append(creature)
            added_levels[level] = True

        # If everything is blocked, add everything instead
        if not valid_creatures:
            for level in added_levels:
                added_levels[level] = True
            valid_creatures.extend(data.CREATURES)

        # Randomize the initial order of the creatures to not favour alphabetical order.
        self.random.shuffle(valid_creatures)

        # If there are levels not represented in valid_creatures, add more using the Weak and Elite templates
        complete = self.check_all_true(added_levels)

        while not complete:

            needed_levels = [level for level in added_levels if not added_levels[level]]
            self.random.shuffle(needed_levels)
            new_creatures = []

            for level in needed_levels:
                for creature in valid_creatures:

                    # We prefer Elite over Weak here because Elite enemies tend to be weaker than Weak ones
                    if int(creature["level"]) == level - 1:
                        new_creature = creature.copy()
                        new_creature["level"] = int(creature["level"]) + 1
                        new_creature["name"] = f"Elite {creature['name']}"
                        added_levels[level] = True
                        break

                    if int(creature["level"]) == level + 1:
                        new_creature = creature.copy()
                        new_creature["level"] = int(creature["level"]) - 1
                        new_creature["name"] = f"Weak {creature['name']}"
                        new_creatures.append(new_creature)
                        added_levels[level] = True
                        break

                self.random.shuffle(valid_creatures)

            for new_creature in new_creatures:
                valid_creatures.append(new_creature)
            self.random.shuffle(valid_creatures)
            complete = self.check_all_true(added_levels)

        # Make a list of valid difficulties
        difficulties = []

        if self.options.minimum_difficulty == 0:
            difficulties.append("Trivial")
        if self.options.minimum_difficulty <= 1 <= self.options.maximum_difficulty:
            difficulties.append("Low")
        if self.options.minimum_difficulty <= 2 <= self.options.maximum_difficulty:
            difficulties.append("Moderate")
        if self.options.minimum_difficulty <= 3 <= self.options.maximum_difficulty:
            difficulties.append("Severe")
        if self.options.maximum_difficulty == 4:
            difficulties.append("Extreme")

        # Make the rooms
        increment_factor = (int(self.options.number_of_rooms.value) /
                            (int(self.options.maximum_level.value) - int(self.options.starting_level.value) + 1))
        keys = self.keys_used.copy()

        for room_number in range(1, int(self.options.number_of_rooms.value)):
            room_name = f"Room {room_number}"
            level = int(self.options.starting_level.value) + int((room_number - 1) / increment_factor)
            difficulty = self.random.choice(difficulties)
            budget = data.DIFFICULTIES[difficulty]
            current = 0
            creatures = []
            offset = 5 if not level <= 2 else 10


            # Choose the creatures to appear in the room; we compare to budget - 5 because a level-3 creature
            # is worth 15 experience points, so we can otherwise end up stuck forever looking for 5 more experience.
            # The offset has to be 10 at levels 1 and 2 since there are no creatures that are level-4 either to give
            # 10 experience
            while current < budget - offset:
                for creature in valid_creatures:
                    creature_level = int(creature["level"])

                    # Discard if the creature is out of the level range
                    if not level - 4 <= creature_level <= level + 4:
                        continue

                    xp = data.XP_VALUES[creature_level - level]

                    if current + xp <= budget:
                        creatures.append(creature["name"])
                        current += xp

                    # Stop looping if we're done
                    if current >= budget - offset:
                        break

                # Shuffle the list of valid creatures for the next loop or the next room
                self.random.shuffle(valid_creatures)

            # Connect the room to one of the previous rooms and potentially add a key; Room 1 is accessible from the
            # start and doesn't need any connections back
            if not room_number == 1:
                source_room = self.random.choice(list(self.rooms.keys()))
                self.rooms[source_room]["Doors"].append(room_name)

                # If all remaining rooms must have keys, then add a key. Otherwise, randomly determine if a key
                # should be added
                if int(self.options.number_of_rooms.value) - room_number + 1 == len(keys):
                    self.rooms[source_room]["Keys"].append(keys.pop())
                elif self.random.randint(0, int(self.options.number_of_rooms.value) - room_number + 1) < len(keys):
                    self.rooms[source_room]["Keys"].append(keys.pop())
                else:
                    self.rooms[source_room]["Keys"].append("")

            self.rooms[room_name] = {
                "Level" : level,
                "Difficulty" : difficulty,
                "Creatures" : creatures,
                "Doors" : [],
                "Keys" : []
            }

        # The Boss Room works slightly differently so we do it separately
        level = int(self.options.maximum_level.value)
        difficulty = "Moderate"
        budget = data.DIFFICULTIES[difficulty]

        if self.options.boss_encounter == 0:
            difficulty = "Trivial"
            budget = data.DIFFICULTIES[difficulty]
        elif self.options.boss_encounter == 1:
            difficulty = "Low"
            budget = data.DIFFICULTIES[difficulty]
        elif self.options.boss_encounter == 2:
            difficulty = "Moderate"
            budget = data.DIFFICULTIES[difficulty]
        elif self.options.boss_encounter == 3:
            difficulty = "Severe"
            budget = data.DIFFICULTIES[difficulty]
        elif self.options.boss_encounter == 4:
            difficulty = "Extreme"
            budget = data.DIFFICULTIES[difficulty]
        elif self.options.boss_encounter == 5:
            difficulty = "Extreme"
            budget = -4
        elif self.options.boss_encounter == 6:
            difficulty = "Extreme+"
            budget = -5

        current = 0
        creatures = []
        offset = 5 if not level <= 2 else 10

        # If we're looking for a specific level of solo boss, find one and save it to creatures
        if budget == -4:
            for creature in valid_creatures:
                creature_level = int(creature["level"])

                if not creature_level == level + 4:
                    continue

                creatures.append(creature["name"])
                break

        if budget == -5:
            for creature in valid_creatures:
                creature_level = int(creature["level"])

                if not creature_level == level + 5:
                    continue

                creatures.append(creature["name"])
                break

        # If there were no possible solo bosses available, just give a regular Extreme encounter instead.
        if (not creatures) and budget < 0:
            difficulty = "Extreme"
            budget = data.DIFFICULTIES[difficulty]

        # Choose the creatures to appear in the room; we compare to budget - 5 because a level-3 creature
        # is worth 15 experience points, so we can otherwise end up stuck forever looking for 5 more experience.
        # The offset has to be 10 at levels 1 and 2 since there are no creatures that at level-4 either to give
        # 10 experience
        while current < budget - offset:
            for creature in valid_creatures:
                creature_level = int(creature["level"])

                # Discard if the creature is out of the level range
                if not level - 4 <= creature_level <= level + 4:
                    continue

                xp = data.XP_VALUES[creature_level - level]

                if current + xp <= budget:
                    creatures.append(creature["name"])
                    current += xp

                # Stop looping if we're done
                if current >= budget - offset:
                    break

            # Shuffle the list of valid creatures for the next loop or the next room
            self.random.shuffle(valid_creatures)

        # Connect the room to one of the previous rooms and potentially add a key
        source_room = self.random.choice(list(self.rooms.keys()))
        self.rooms[source_room]["Doors"].append("Boss Room")

        # If there is a key left to use, use it here
        if keys:
            self.rooms[source_room]["Keys"].append(keys.pop())
        else:
            self.rooms[source_room]["Keys"].append("")

        # The Boss Room may need to have a lot of locations to account for the minimum number of items in the case of
        # few rooms with a large level range and the maximum number of keys. Worst case requires 28 locations and every
        # additional room past the minimum (Room 1 and the Boss Room) lowers the requirement by 4
        locations_needed = max(5, 28 - (4 * (len(self.rooms) - 1)))

        self.rooms["Boss Room"] = {
            "Level": level,
            "Difficulty": difficulty,
            "Creatures": creatures,
            "Doors": [],
            "Keys": [],
            "Locations Needed": "ABCDEFGHIJKLMNOPQRSTUVWXYZab"[:locations_needed]
        }

        # Universal Tracker support
        if slot_data:
            for i in range(1, 20):
                if f"Room {i}" in slot_data:
                    self.rooms[f"Room {i}"] = json.loads(slot_data[f"Room {i}"])

            if "Boss Room" in slot_data:
                self.rooms["Boss Room"] = json.loads(slot_data["Boss Room"])

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.APPF2eItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data =  self.options.as_dict(
            "strict_logic",
            "use_abp",
            "include_exploration_activities"
        )

        slot_data["Ancestries"] = self.starting["Ancestries"]
        slot_data["Backgrounds"] = self.starting["Backgrounds"]
        slot_data["Classes"] = self.starting["Classes"]
        slot_data["Weapons"] = self.starting["Weapons"]
        slot_data["Shields"] = self.starting["Shields"]
        slot_data["Armors"] = self.starting["Armors"]

        for room in self.rooms:
            slot_data[room] = json.dumps(self.rooms[room])

        return slot_data

    def check_all_true(self, dictionary: Mapping[int, bool]) -> bool:
        """Returns True if all items are true, False otherwise."""
        for value in dictionary:
            if not dictionary[value]:
                return False
        return True

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a regen in UT
        return slot_data
