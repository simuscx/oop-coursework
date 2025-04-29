from Item import Item
from CharacterBuilder import CharacterBuilder
from Character import CharacterSaver

# Create items
sword = Item("Sword", "A sharp blade for battle", 150)
lyre = Item("Lyre", "A musical instrument for inspiring allies", 100)

# Builder design pattern usage
builder = CharacterBuilder()
hero = (
    builder
    .set_name("m1000")
    .set_class("Wizard")
    .set_stats({"STR": 1, "DEX": 1, "CON": 1, "INT": 99})
    .build()
    # TODO: .set_inventory([sword])
)
# TODO: remove when .set_inventory([sword]) implemented
hero.add_item_to_inventory(sword)


bard = (
    builder
    .set_name("abcdefg")
    .set_class("Bard")
    .set_stats({"STR": 99})
    .build()
)

bard.add_item_to_inventory(lyre)

characters = [hero, bard]

character_saver = CharacterSaver()
character_saver.save_characters([hero, bard], "sunday_weekend_event.json")

hero.save_to_file(file_name="hero.json")
bard.save_to_file(file_name="bard.json")

old_characters = character_saver.load_characters("sunday_weekend_event.json")

for characters in old_characters:
    print(characters)