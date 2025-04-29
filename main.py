from CharacterBuilder import CharacterBuilder
from Character import CharacterSaver

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
# hero.add_item_to_inventory(sword)


bard = (
    builder
    .set_name("abcdefg")
    .set_class("Bard")
    .set_stats({"STR": 99})
    .build()
)

rogue = (
    builder
    .set_name("pozne")
    .set_class("Rogue")
    .set_stats({"DEX": 99})
    .build()
)

characters = [hero, bard, rogue]

character_saver = CharacterSaver()
character_saver.save_characters([hero, bard, rogue], "sunday_weekend_event.json")

hero.save_to_file(file_name="hero.json")
bard.save_to_file(file_name="bard.json")
rogue.save_to_file(file_name="rogue.json")

old_characters = character_saver.load_characters("sunday_weekend_event.json")

for characters in old_characters:
    print(characters)