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

    def __init__(self, name: str, character_class: str, stats: dict):
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

    def special_ability(self) -> str:
        return "Rage: Unleash devastating attacks with increased strength!"
