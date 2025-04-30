import abc
from Item import Item


class Character(abc.ABC):  # Abstraction - abstract class Character
    """
    Abstract Base Class for all Character types in the DND Helper.
    Represents the core attributes and behaviors of a DND character.

    :param str name: The name of the character.
    :param str character_class: The character's class (e.g., Barbarian, Bard).
    :param dict stats: A dictionary of the character's stats (e.g., STR, DEX).
    """

    def __init__(self, name: str, character_class: str, stats: dict) -> None:
        self._name = name
        self._character_class = character_class
        self.stats = stats

        default_items = {
            "Barbarian": [Item("Battle Axe", "A heavy weapon for brutal combat", 200)],
            "Bard": [Item("Lyre", "A musical instrument for inspiring allies", 100)],
            "Cleric": [Item("Holy Symbol", "A sacred item for divine magic", 150)],
            "Druid": [Item("Wooden Staff", "A staff infused with nature’s energy", 120)],
            "Fighter": [Item("Longsword", "A balanced weapon for skilled fighters", 175)],
            "Monk": [Item("Prayer Beads", "Symbol of meditation and discipline", 80)],
            "Paladin": [Item("Blessed Shield", "A shield blessed with divine protection", 180)],
            "Ranger": [Item("Hunting Bow", "A reliable bow for ranged combat", 160)],
            "Rogue": [Item("Dagger", "A quick weapon for stealth attacks", 130)],
            "Sorcerer": [Item("Arcane Tome", "A book containing powerful spells", 200)],
            "Warlock": [Item("Dark Amulet", "An artifact tied to a mysterious patron", 190)],
            "Wizard": [Item("Magic Wand", "A basic wand for casting spells", 150)],
        }
        # Encapsulation - inventory is private
        self._inventory = default_items.get(character_class, [])  # Composition: Inventory belongs to the character.

    @abc.abstractmethod
    def special_ability(self) -> str:
        """
        Abstract method that must be implemented by subclasses.
        Defines the special ability of each character class.

        :return str: The special ability description.
        """
        pass

    def add_item_to_inventory(self, item: Item) -> None:
        """
        Adds an item to the character's inventory.

        :param Item item: The item to be added.
        """
        self._inventory.append(item)

    def remove_item_from_inventory(self, item: Item) -> None:
        """
        Removes an item from the character's inventory.

        :param Item item: The item to be removed.
        """
        if item in self._inventory:
            self._inventory.remove(item)

    def to_dict(self) -> dict:
        """
        Converts the character object into a dictionary representation

        return: a dictionary containing the character's attributes
        param: name (str): The character's name
        param: character_class (str): The class of the character (e.g., Barbarian)
        param: stats (dict): A dictionary of the character's stats (e.g. STR)
        param: inventory (list): A list of item names representing the character's inventory.

        """
        return {
            "name": self._name,
            "character_class": self._character_class,
            "stats": self.stats,
            "inventory": [item.__dict__ for item in self._inventory]
        }

    def save_to_file(self, file_name: str) -> None:
        """
        Saves the character's details to a given file in JSON format.

        :param file_name: file name to write to
        """

        data = {
            "name": self._name,
            "character_class": self._character_class,
            "stats": self.stats,
            "inventory": [item.name for item in self._inventory]  # could be a method, self.get_inventory()
        }
        with open(file_name, "w") as file:
            json.dump(data, file, indent=2)  # indent=2 so that the json looks better

    def __str__(self) -> str:
        return (f"{self._name} the {self._character_class} - Stats: {self.stats}. "
                f"Inventory: {', '.join([item.name for item in self._inventory])}")  # or self.get_inventory()


class Barbarian(Character):
    # Inheritance - Barbarian class inherits from Character
    """
    Represents a Barbarian character class.
    Inherits from the abstract Character base class.
    """

    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 15, "DEX": 12, "CON": 14, "INT": 8, "WIS": 10, "CHA": 10}
        super().__init__(name, "Barbarian", stats if stats else default_stats)

    def special_ability(self) -> str:  # polymorphism - new special ability for each class
        return "Rage: Unleash devastating attacks with increased strength!"


class Bard(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 10, "DEX": 14, "CON": 12, "INT": 12, "WIS": 10, "CHA": 15}
        super().__init__(name, "Bard", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Inspiration: Uplift allies with captivating performances!"


class Cleric(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 12, "DEX": 10, "CON": 14, "INT": 10, "WIS": 15, "CHA": 12}
        super().__init__(name, "Cleric", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Divine Healing: Restore health through divine powers!"


class Druid(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 10, "DEX": 12, "CON": 12, "INT": 12, "WIS": 15, "CHA": 10}
        super().__init__(name, "Druid", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Wild Shape: Transform into animals for versatility in combat!"


class Fighter(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 15, "DEX": 12, "CON": 14, "INT": 10, "WIS": 10, "CHA": 10}
        super().__init__(name, "Fighter", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Second Wind: Recover quickly from injuries!"


class Monk(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 12, "DEX": 15, "CON": 12, "INT": 10, "WIS": 14, "CHA": 10}
        super().__init__(name, "Monk", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Flurry of Blows: Attack multiple times with precision!"


class Paladin(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 14, "DEX": 10, "CON": 14, "INT": 10, "WIS": 12, "CHA": 15}
        super().__init__(name, "Paladin", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Divine Smite: Channel divine energy to deal massive damage!"


class Ranger(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 12, "DEX": 14, "CON": 12, "INT": 10, "WIS": 14, "CHA": 10}
        super().__init__(name, "Ranger", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Hunter's Mark: Track and deal extra damage to prey!"


class Rogue(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 10, "DEX": 15, "CON": 12, "INT": 12, "WIS": 10, "CHA": 14}
        super().__init__(name, "Rogue", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Sneak Attack: Exploit weaknesses to strike critical blows!"


class Sorcerer(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 10, "DEX": 12, "CON": 14, "INT": 10, "WIS": 12, "CHA": 15}
        super().__init__(name, "Sorcerer", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Spell-casting: Cast powerful spells fueled by innate magic!"


class Warlock(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 10, "DEX": 12, "CON": 12, "INT": 14, "WIS": 10, "CHA": 15}
        super().__init__(name, "Warlock", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Eldritch Blast: Unleash arcane power granted by your patron!"


class Wizard(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 8, "DEX": 12, "CON": 10, "INT": 15, "WIS": 14, "CHA": 10}
        super().__init__(name, "Wizard", stats if stats else default_stats)

    def special_ability(self) -> str:
        return "Arcane Mastery: Harness deep knowledge to control magic!"


# TODO: imports at the top
import json


# TODO: consider new file for this class & CharacterManager maybe sound better? Cause it also loads the file
class CharacterSaver:
    @staticmethod
    def save_characters(characters, output_file):
        combined_data = []

        for char in characters:
            try:
                data = char.to_dict()
                combined_data.append(data)
            except Exception as e:
                print(f"Error processing character: {e}")

        try:
            with open(output_file, "w") as out_file:
                json.dump(combined_data, out_file, indent=2)

            # TODO: what if i only save single character? Is it still combined?
            print(f"\nCombined character data saved to {output_file}")
        except Exception as e:
            print(f"Error writing to {output_file}: {e}")

    @staticmethod
    def load_characters(json_file):
        # TODO: ah, solving circular imports, two ways to solve this:
        #  1. import here but it's a hacky solution
        #  2. use pyproject to import anything from root dir
        #   but this is very NICE TO HAVE for a project like this and not needed tbh

        from CharacterBuilder import CharacterBuilder
        characters: list[Character] = []
        try:
            with open(json_file, "r") as file:
                data = json.load(file)

                for char_data in data:
                    builder = CharacterBuilder()
                    builder.set_name(char_data.get('name', 'Unnamed'))
                    builder.set_class(char_data.get('character_class', 'Unknown'))

                    if "stats" in char_data:
                        builder.set_stats(char_data.get("stats", {}))

                    if "inventory" in char_data:
                        item_dicts = char_data["inventory"]
                        items = [Item(**item_data) for item_data in item_dicts]
                        builder.set_inventory(items)

                    characters.append(builder.build())

        except FileNotFoundError:
            print(f"Error: {json_file} not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {json_file}")

        # TODO: for future: PEP8: no newline at end of file
        return characters
