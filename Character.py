import abc
import json
from Item import Item


class Character(abc.ABC):
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
        self._stats = stats
        self._inventory = []  # Composition: Inventory belongs to the character.

    @abc.abstractmethod
    def special_ability(self) -> str:
        """
        Abstract method that must be implemented by subclasses.
        Defines the special ability of each character class.

        :return str: The special ability description.
        """
        pass

    def add_item_to_inventory(self, item: "Item") -> None:
        """
        Adds an item to the character's inventory.

        :param Item item: The item to be added.
        """
        self._inventory.append(item)

    def remove_item_from_inventory(self, item: "Item") -> None:
        """
        Removes an item from the character's inventory.

        :param Item item: The item to be removed.
        """
        if item in self._inventory:
            self._inventory.remove(item)

    def save_to_file(self, textfile) -> None:
        """
        Saves the character's details to a given file in JSON format.

        :param textfile: The file object opened in text mode to save data into.
        """
        if not textfile.writable():
            raise ValueError("Provided file must be writable")

        data = {
            "name": self._name,
            "character_class": self._character_class,
            "stats": self._stats,
            "inventory": [item.name for item in self._inventory]
        }
        json.dump(data, textfile)

    def __str__(self) -> str:
        return f"{self._name} the {self._character_class} - Stats: {self._stats}"


class Barbarian(Character):
    """
    Represents a Barbarian character class.
    Inherits from the abstract Character base class.
    """

    def __init__(self, name: str, stats: dict = None):
        default_stats = {"STR": 15, "DEX": 12, "CON": 14, "INT": 8, "WIS": 10, "CHA": 10}
        super().__init__(name, "Barbarian", stats if stats else default_stats)

    def special_ability(self) -> str:
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
        return "Spellcasting: Cast powerful spells fueled by innate magic!"


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
