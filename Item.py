class Item:
    """
    Represents an item (e.g., Weapon, Armor, Consumable) in the game.

    :param str name: The name of the item.
    :param str item_type: The type of the item (e.g., Weapon, Armor).
    """

    def __init__(self, name: str, item_type: str):
        self.name = name
        self.item_type = item_type

    def __str__(self) -> str:
        return f"{self.name} ({self.item_type})"