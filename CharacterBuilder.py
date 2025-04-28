from Character import Character, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard


class CharacterBuilder:
    """
    Builder Design Pattern for creating Character objects step-by-step.
    """

    def __init__(self):
        """
        Initializes the builder with an empty Character object.
        """
        self.character = None

    def set_name(self, name: str) -> "CharacterBuilder":
        """
        Sets the character's name.

        :param str name: The name of the character.
        :return CharacterBuilder: Returns the builder for chaining.
        """
        if self.character:
            self.character._name = name
        return self

    def set_class(self, char_class: str) -> "CharacterBuilder":
        """
        Assigns a class type to the character by creating the relevant subclass.

        :param str char_class: The class of the character (e.g., Barbarian).
        :return CharacterBuilder: Returns the builder for chaining.
        """
        if char_class == "Barbarian":
            self.character = Barbarian(name="Unnamed", stats={})

        if char_class == "Bard":
            self.character = Bard(name="Unnamed", stats={})

        if char_class == "Cleric":
            self.character = Cleric(name="Unnamed", stats={})

        if char_class == "Druid":
            self.character = Druid(name="Unnamed", stats={})

        if char_class == "Fighter":
            self.character = Fighter(name="Unnamed", stats={})

        if char_class == "Monk":
            self.character = Monk(name="Unnamed", stats={})

        if char_class == "Paladin":
            self.character = Paladin(name="Unnamed", stats={})

        if char_class == "Ranger":
            self.character = Ranger(name="Unnamed", stats={})

        if char_class == "Rogue":
            self.character = Rogue(name="Unnamed", stats={})

        if char_class == "Sorcerer":
            self.character = Sorcerer(name="Unnamed", stats={})

        if char_class == "Warlock":
            self.character = Warlock(name="Unnamed", stats={})

        if char_class == "Wizard":
            self.character = Wizard(name="Unnamed", stats={})

        return self

    def set_stats(self, stats: dict) -> "CharacterBuilder":
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
