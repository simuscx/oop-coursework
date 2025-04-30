from CharacterBuilder import CharacterBuilder
from Character import CharacterManager
from Item import Item

# Builder design pattern usage
builder = CharacterBuilder()
hero = (
    builder
    .set_name("m1000")
    .set_class("Wizard")
    .set_stats({"STR": 99, "DEX": 99, "CON": 99, "INT": 99})
    .set_inventory([
        Item("itemname", "desc", 999),
        Item("itemname2", "desc2", 150)
    ])
    .build()
)

bard = (
    builder
    .set_name("abcdefg")
    .set_class("Bard")
    .set_stats({"STR": 99})
    .set_inventory([
        Item("abcdefg", "abcdefg", 50)
    ])
    .build()
)

characters = [hero, bard]

hero.save_to_file(file_name="hero.json")
bard.save_to_file(file_name="bard.json")

character_manager = CharacterManager()
character_manager.save_characters([hero, bard], "sunday_weekend_event.json")

old_characters = character_manager.load_characters("sunday_weekend_event.json")
for characters in old_characters:
    print(characters)
