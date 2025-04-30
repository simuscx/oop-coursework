class Item:
    def __init__(self, name: object, description: object, value: object, weight: object = 0, rarity: object = "Common") -> None:
        """
        Initialize an Item.

        :param name: str - The name of the item.

        # TODO: currently used
        Args: name(Str)

        # TODO: choose one style and stick to it

        Args:
            :param name: str - The name of the item.
            :param description: str - A short description of the item.
            value (int): The item's value in the game's currency.
            weight (int, optional): The weight of the item. Defaults to 0.
            rarity (str, optional): The rarity level of the item. Defaults to 'Common'.
        """
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
        self.rarity = rarity

    def __str__(self):
        """
        Return a string representation of the item.
        """
        return (f"{self.name} [{self.rarity}]\n"
                f"Description: {self.description}\n"
                f"Value: {self.value} coins\n"
                f"Weight: {self.weight} kg")

    def is_valuable(self):
        """
        Determine if the item is considered valuable.

        Returns:
            bool: True if the item's value is greater than 100, False otherwise.
        """
        return self.value > 100

    def is_lightweight(self):
        """
        Determine if the item is lightweight.

        Returns:
            bool: True if the item's weight is less than or equal to 2, False otherwise.
        """
        return self.weight <= 2
        # TODO: consider random numbers used at the top of the file as random constants for easier change, for example
        #  LIGHTWEIGHT_THRESHOLD = 2 / VALUABLE_THRESHOLD = 100 and then measure by that
