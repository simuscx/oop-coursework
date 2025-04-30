import unittest
import random
import string
from Character import CharacterManager
from CharacterBuilder import CharacterBuilder
from Item import Item


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.builder = CharacterBuilder()
        self.manager = CharacterManager()
        self.hero = (
            self.builder.set_name("m1000")
            .set_class("Wizard")
            .set_stats({"STR": 99, "DEX": 99, "CON": 99, "INT": 99})
            .set_inventory(
                [Item("itemname", "desc", 999), Item("itemname2", "desc2", 150)]
            )
            .build()
        )
        self.test_file = "test_character_save.json"

    def tearDown(self):
        del self.builder
        del self.manager
        del self.hero

    def test_inventory_holds_items(self):
        """
        Verify that the character's inventory holds the expected items"
        """
        self.assertEqual(len(self.hero._inventory), 2)
        self.assertEqual(self.hero._inventory[0].name, "itemname")
        self.assertEqual(self.hero._inventory[1].value, 150)

    def test_save_and_load(self):
        """
        Tests saving and loading persists the same hero details
        """
        file_name = "test1.json"
        self.manager.save_characters(characters=[self.hero], output_file=file_name)
        loaded_chars = self.manager.load_characters(file_name)

        # test that loaded characters are more than 0
        self.assertGreater(len(loaded_chars), 0)

        loaded_hero = loaded_chars[0]
        # self.assertEqual(self.hero, loaded_hero)
        self.assertEqual(self.hero.to_dict(), loaded_hero.to_dict())

    def test_partial_stats_keep_defaults(self):
        """
        Ensure default stats remain when not explicitly set.
        """
        random_override_value = int(18)
        rogue_default_str = int(10)

        partial_hero = (
            CharacterBuilder()
            .set_name("roguey")
            .set_class("Rogue")
            .set_stats({"DEX": random_override_value})
            .build()
        )
        self.assertEqual(partial_hero.stats["DEX"], random_override_value)
        self.assertEqual(partial_hero.stats["STR"], rogue_default_str)

    def test_loading_characters_off_nonexistent_file(self):
        """
        Ensure loading nonexistent files don't work.
        """
        file_name = "".join(random.choices(string.ascii_letters, k=10))
        self.assertRaises(
            FileNotFoundError, lambda: self.manager.load_characters(f"{file_name}.json")
        )


if __name__ == "__main__":
    unittest.main()
