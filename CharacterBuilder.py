from __future__ import annotations
# future importas kad galetum typintint normaliai ^

# TODO: imports look better like this, possible even a few in one line
from Character import (
    Character,
    Barbarian,
    Bard,
    Cleric,
    Druid,
    Fighter,
    Monk,
    Paladin,
    Ranger,
    Rogue,
    Sorcerer,
    Warlock,
    Wizard
)


class CharacterBuilder:
    """
    Builder Design Pattern for creating Character objects step-by-step.
    """

    def __init__(self):
        """
        Initializes the builder with an empty Character object.
        """
        self.character = None

    def set_name(self, name: str) -> CharacterBuilder:
        """
        Sets the character's name.

        :param str name: The name of the character.
        :return CharacterBuilder: Returns the builder for chaining.
        """
        if self.character:
            self.character._name = name
        return self

    def set_class(self, char_class: str) -> CharacterBuilder:
        """
        Assigns a class type to the character by creating the relevant subclass.

        :param str char_class: The class of the character (e.g., Barbarian).
        :return CharacterBuilder: Returns the builder for chaining.
        """
        char_class_map = {
            "Barbarian": Barbarian,
            "Bard": Bard,
            "Cleric": Cleric,
            "Druid": Druid,
            "Fighter": Fighter,
            "Monk": Monk,
            "Paladin": Paladin,
            "Ranger": Ranger,
            "Rogue": Rogue,
            "Sorcerer": Sorcerer,
            "Warlock": Warlock,
            "Wizard": Wizard,
        }

        if char_class in char_class_map:
            self.character = char_class_map[char_class](name="Unnamed", stats={})

        if char_class not in char_class_map:
            raise ValueError(f"Unsupported character class: {char_class}")

        return self

    def set_stats(self, stats: dict) -> CharacterBuilder:
        """
        Sets the character's stats.

        :param dict stats: A dictionary containing character stats (e.g., STR, DEX).
        :return CharacterBuilder: Returns the builder for chaining.
        """
        if self.character:
            self.character._stats = stats
        return self

    def build(self) -> Character:
        """
        Completes the build process and returns the finished Character object.

        :return Character: The constructed Character object.
        """
        return self.character
