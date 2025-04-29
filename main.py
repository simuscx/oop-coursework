from Item import Item
from Character import Barbarian, Bard

# Create items
sword = Item("Sword", "A sharp blade for battle", 150)
lyre = Item("Lyre", "A musical instrument for inspiring allies", 100)

# Create characters
# hero = Barbarian("Grog")
# hero.add_item_to_inventory(sword)

# TODO: cleanup imports
from CharacterBuilder import CharacterBuilder

# Builder design pattern usage
builder = CharacterBuilder()
hero = (
    builder
    .set_name("Grog")
    .set_class("Barbarian")
    .set_stats({"STR": 99, "DEX": 1, "CON": 10})
    # TODO: gal reiktu pridet kad jei nevisi stats papasinti, reiktu defaultus paimt
    .build()
    # TODO: .set_inventory([sword])
)

# TODO: remove when .set_inventory([sword]) implemented
hero.add_item_to_inventory(sword)

bard = Bard("Scanlan")
bard.add_item_to_inventory(lyre)

# TODO: character saver class
# character_saver = CharacterSaver()
# character_saver.save_characters([hero, bard], "sunday_weekend_event.json")

# Display details
print(hero)
print(bard)

# Save characters to files
hero.save_to_file(file_name="hero.json")
bard.save_to_file(file_name="bard.json")

# TODO: load characters from file
# old_characters = character_saver.load_characters("saturday_event.json")
