class Item:
    def __init__(self, name: str, description: str, value: int):
        """
        Initialize an Item.

        :param name: str - The name of the item.
        :param description: str - A short description of the item.
        :param value (int): The item's value in the game's currency.
        """
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        """
        Return a string representation of the item.
        """
        return (
            f"{self.name} Description: {self.description}\n Value: {self.value} coins\n"
        )

    def is_valuable(self) -> bool:
        """
        Determine if the item is considered valuable.


        :return bool: True if the item's value is greater than 100, False otherwise.
        """
        return self.value > 100
