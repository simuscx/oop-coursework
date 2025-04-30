import unittest

from Character import CharacterManager
from CharacterBuilder import CharacterBuilder
from Item import Item


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.builder = CharacterBuilder()
        self.manager = CharacterManager()
        self.hero = (
            self.builder
            .set_name("m1000")
            .set_class("Wizard")
            .set_stats({"STR": 99, "DEX": 99, "CON": 99, "INT": 99})
            .set_inventory([
                Item("itemname", "desc", 999),
                Item("itemname2", "desc2", 150)
            ])
            .build()
        )


    def tearDown(self):
        del self.builder
        del self.manager
        del self.hero


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


    def test_example1(self):
        self.assertLess(1, 2)

if __name__ == '__main__':
    unittest.main()
