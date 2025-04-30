import abc
import json

from Item import Item


class Character(abc.ABC):  # Abstraction - abstract class Character
    """
    Abstract Base Class for all Character types in the DND Helper.
    Represents the core attributes and behaviors of a DND character.

    :param str name: The name of the character.
    :param str character_class: The character's class (e.g., Barbarian, Bard).
    :param dict stats: A dictionary of the character's stats (e.g., STR, DEX).
    :param dict health: The health of the character.
    """

    def __init__(self, name: str, character_class: str, stats: dict, health: int) -> None:
        self._name = name
        self._character_class = character_class
        self.stats = stats
        self.health = health

        default_items = {
            "Barbarian": [Item("Battle Axe", "A heavy weapon for brutal combat", 200)],
            "Bard": [Item("Lyre", "A musical instrument for inspiring allies", 100)],
            "Cleric": [Item("Holy Symbol", "A sacred item for divine magic", 150)],
            "Druid": [
                Item("Wooden Staff", "A staff infused with nature’s energy", 120)
            ],
            "Fighter": [
                Item("Longsword", "A balanced weapon for skilled fighters", 175)
            ],
            "Monk": [Item("Prayer Beads", "Symbol of meditation and discipline", 80)],
            "Paladin": [
                Item("Blessed Shield", "A shield blessed with divine protection", 180)
            ],
            "Ranger": [Item("Hunting Bow", "A reliable bow for ranged combat", 160)],
            "Rogue": [Item("Dagger", "A quick weapon for stealth attacks", 130)],
            "Sorcerer": [Item("Arcane Tome", "A book containing powerful spells", 200)],
            "Warlock": [
                Item("Dark Amulet", "An artifact tied to a mysterious patron", 190)
            ],
            "Wizard": [Item("Magic Wand", "A basic wand for casting spells", 150)],
        }
        # Encapsulation - inventory is private
        self._inventory = default_items.get(
            character_class, []
        )  # Composition: Inventory belongs to the character.

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
            "inventory": [item.__dict__ for item in self._inventory],
        }

    def __str__(self):
        return (
            f"{self._character_class} {self._name} with stats "
            f"{self.stats}. Inventory: {[item.name for item in self._inventory]}"
        )


class Barbarian(Character):
    # Inheritance - Barbarian class inherits from Character
    """
    Represents a Barbarian character class. (does the same for every other class)
    Inherits from the abstract Character base class.
    """

    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 15,
            "DEX": 12,
            "CON": 14,
            "INT": 8,
            "WIS": 10,
            "CHA": 10,
        }
        super().__init__(name, "Barbarian", stats if stats else default_stats, health=150)

    def special_ability(
        self,
    ) -> str:  # polymorphism - new special ability for each class
        return "Rage: Unleash devastating attacks with increased strength!"


class Bard(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 10,
            "DEX": 14,
            "CON": 12,
            "INT": 12,
            "WIS": 10,
            "CHA": 15,
        }
        super().__init__(name, "Bard", stats if stats else default_stats, health = 100)

    def special_ability(self) -> str:
        return "Inspiration: Uplift allies with captivating performances!"


class Cleric(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 12,
            "DEX": 10,
            "CON": 14,
            "INT": 10,
            "WIS": 15,
            "CHA": 12,
        }
        super().__init__(name, "Cleric", stats if stats else default_stats, health = 120)

    def special_ability(self) -> str:
        return "Divine Healing: Restore health through divine powers!"


class Druid(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 10,
            "DEX": 12,
            "CON": 12,
            "INT": 12,
            "WIS": 15,
            "CHA": 10,
        }
        super().__init__(name, "Druid", stats if stats else default_stats, health = 110)

    def special_ability(self) -> str:
        return "Wild Shape: Transform into animals for versatility in combat!"


class Fighter(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 15,
            "DEX": 12,
            "CON": 14,
            "INT": 10,
            "WIS": 10,
            "CHA": 10,
        }
        super().__init__(name, "Fighter", stats if stats else default_stats, health = 130)

    def special_ability(self) -> str:
        return "Second Wind: Recover quickly from injuries!"


class Monk(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 12,
            "DEX": 15,
            "CON": 12,
            "INT": 10,
            "WIS": 14,
            "CHA": 10,
        }
        super().__init__(name, "Monk", stats if stats else default_stats, health = 115)

    def special_ability(self) -> str:
        return "Flurry of Blows: Attack multiple times with precision!"


class Paladin(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 14,
            "DEX": 10,
            "CON": 14,
            "INT": 10,
            "WIS": 12,
            "CHA": 15,
        }
        super().__init__(name, "Paladin", stats if stats else default_stats, health = 140)

    def special_ability(self) -> str:
        return "Divine Smite: Channel divine energy to deal massive damage!"


class Ranger(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 12,
            "DEX": 14,
            "CON": 12,
            "INT": 10,
            "WIS": 14,
            "CHA": 10,
        }
        super().__init__(name, "Ranger", stats if stats else default_stats, health = 120)

    def special_ability(self) -> str:
        return "Hunter's Mark: Track and deal extra damage to prey!"


class Rogue(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 10,
            "DEX": 15,
            "CON": 12,
            "INT": 12,
            "WIS": 10,
            "CHA": 14,
        }
        super().__init__(name, "Rogue", stats if stats else default_stats, health = 105)

    def special_ability(self) -> str:
        return "Sneak Attack: Exploit weaknesses to strike critical blows!"


class Sorcerer(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 10,
            "DEX": 12,
            "CON": 14,
            "INT": 10,
            "WIS": 12,
            "CHA": 15,
        }
        super().__init__(name, "Sorcerer", stats if stats else default_stats, health = 90)

    def special_ability(self) -> str:
        return "Spell-casting: Cast powerful spells fueled by innate magic!"


class Warlock(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 10,
            "DEX": 12,
            "CON": 12,
            "INT": 14,
            "WIS": 10,
            "CHA": 15,
        }
        super().__init__(name, "Warlock", stats if stats else default_stats, health = 95)

    def special_ability(self) -> str:
        return "Eldritch Blast: Unleash arcane power granted by your patron!"


class Wizard(Character):
    def __init__(self, name: str, stats: dict = None):
        default_stats = {
            "STR": 8,
            "DEX": 12,
            "CON": 10,
            "INT": 15,
            "WIS": 14,
            "CHA": 10,
        }
        super().__init__(name, "Wizard", stats if stats else default_stats, health = 80)

    def special_ability(self) -> str:
        return "Arcane Mastery: Harness deep knowledge to control magic!"


class CharacterManager:
    """
    A utility class for managing character data in the DND Helper.
    Handles saving and loading character instances from JSON files.
    Provides methods to serialize and deserialize character objects.
    """

    @staticmethod
    def save_characters(characters, output_file):
        """
        Saves a list of characters to JSON file.
        Iterates through the provided characters, converting them to dictionary
        format, and writes the data to a JSON file.

        :param list characters: a list of character instances to be saved
        :param str output_file: the file path where the character data should be stored
        """
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
                print(f"\nCharacter data saved to {output_file}")
        except Exception as e:
            print(f"Error writing to {output_file}: {e}")

    @staticmethod
    def load_characters(json_file):
        """
        Loads characters from a JSON file and reconstructs them.
        Reads character data from the provided JSON file and recreates Character
        objects using the CharacterBuilder class.

        :param str json_file: the file path of the JSON file containing Character data.
        :return: A list of Character objects reconstructed from stored data.
        """
        from CharacterBuilder import CharacterBuilder

        characters: list[Character] = []
        try:
            with open(json_file, "r") as file:
                data = json.load(file)

                for char_data in data:
                    builder = CharacterBuilder()
                    builder.set_name(char_data.get("name", "Unnamed"))
                    builder.set_class(char_data.get("character_class", "Unknown"))

                    if "stats" in char_data:
                        builder.set_stats(char_data.get("stats", {}))

                    if "inventory" in char_data:
                        item_dicts = char_data["inventory"]
                        items = [Item(**item_data) for item_data in item_dicts]
                        builder.set_inventory(items)

                    characters.append(builder.build())

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: {json_file} not found.")

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {json_file}")

        return characters
